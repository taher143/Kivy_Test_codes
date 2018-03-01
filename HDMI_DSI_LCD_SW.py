from multiprocessing import Process, Manager, Event

def display_process(dict_global, is_master, exit_event):    
	import os
	if is_master == 5:
		print "---if---hdmi---5----"
		os.environ["KIVY_BCM_DISPMANX_ID"] = "5"

	elif is_master == 4:
		print "---elif---dsi---4---"
		os.environ["KIVY_BCM_DISPMANX_ID"] = "4"

	# kivy module imports go here
	import kivy
	from kivy.app import App
	from kivy.uix.boxlayout import BoxLayout
	from kivy.uix.button import Button
	from kivy.uix.image import Image

	class Fejkbiljett(App):
		def build(self):
			self.gen_btn = Button(text='Generera',size_hint=(.10, .10),pos=(5, 5),font_size=21)
			self.gen_btn.bind(on_press=self.getMessageFejkbiljett)
			l = BoxLayout()
			l.add_widget(self.gen_btn)
			return l

		def getMessageFejkbiljett(self, *args):
			print "1. this is called on the method getMessageFejkbiljett of Fejkbiljett"
			st = StockholmTicket()
			st.getMessage(self)


	class StockholmTicket():

		def getMessage(self, source):
			source.gen_btn.text = "the event was called"
			print "2. this is called on the method getMessage of StockholmTicket"
	
	class HdmiApp(App):
		def build(self):
			return Image(source='hdmi.jpg')
	if is_master == 5:
		HdmiApp().run()
	elif is_master == 4:
		Fejkbiljett().run()
		
	
	
if __name__ == '__main__':
    m = Manager()
    dict_main = m.dict()
    ev = Event()
    dict_main['counter'] = 0
    proc_master = Process(target=display_process, args=(dict_main,5, ev))
    proc_slave = Process(target=display_process, args=(dict_main,4, ev))
    proc_master.start()
    proc_slave.start()
    proc_master.join()
    proc_slave.join()
   