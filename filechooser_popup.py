import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
import subprocess

Builder.load_string('''
<ConfirmPopup>:
    BoxLayout:
		orientation: 'vertical'
		FileChooserListView:
			id: filechooser
			filters: ['*.zip']
		BoxLayout:	
			size_hint: 1,0.2
			Button:
				text: 'OK'
				on_release: root.dispatch('on_answer',filechooser.selection)
				size_hint: 1,0.2
			Button:
				text: 'Cancel'
				on_release: root.dispatch('on_answer', 'Cancel')
				size_hint: 1,0.2
''')

class ConfirmPopup(BoxLayout):
	text = StringProperty()
	[0]
	
	def __init__(self,**kwargs):
		self.register_event_type('on_answer')
		super(ConfirmPopup,self).__init__(**kwargs)
		
	def on_answer(self, filename):
		print "selected: %s" % filename
		if filename != "Cancel" :
                        print subprocess.call(['unzip',filename[0],'-d','/home/pi/nkonnect/3D_Printer/test_4/temp_zip'])

class PopupTest(App):
	def build(self):
		content = ConfirmPopup()
		content.bind(on_answer=self._on_answer)
		self.popup = Popup(title="Select .zip file",
							content=content,
							size_hint=(None, None),
							size=(480,400),
							auto_dismiss= False)
		self.popup.open()
		
	def _on_answer(self, instance, answer):
		print "USER ANSWER: " , repr(answer)
		self.popup.dismiss()
		
if __name__ == '__main__':
	PopupTest().run()
