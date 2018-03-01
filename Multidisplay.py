from multiprocessing import Process, Manager, Event

def display_process(dict_global, is_master, exit_event):    
	import os
	if is_master == 5:
		print "---if---hdmi---5----"
		os.environ["KIVY_BCM_DISPMANX_ID"] = "5"

	elif is_master == 4:
		print "---elif---dsi---4---"
		os.environ["KIVY_BCM_DISPMANX_ID"] = "4"

	else:
		print "---elsr---else------"
		
	# kivy module imports go here
	import kivy
	from kivy.app import App
	from kivy.uix.image import Image
	from kivy.uix.button import Button
	print "Hello"
    # ButtonDIPO, LabelD, and MyApp class definitions
	class DsiApp(App):
		#def build(self):
			#return Image(source='/home/pi/nkonnect/dsi.jpg')
		def build(self):
			return Button(text='Hello!',background_color=(0, 0, 1, 1),font_size=150)
			
	class HdmiApp(App):
		def build(self):
			return Image(source='/home/pi/nkonnect/hdmi.jpg')
			
	if is_master == 5:
		HdmiApp().run()
	elif is_master == 4:
		DsiApp().run()
	#DsiApp().run()
	
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