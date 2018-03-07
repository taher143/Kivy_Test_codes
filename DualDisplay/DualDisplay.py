import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
import subprocess
class MyApp(App):
	def build(self):
		Label(text='Child!!')
		b = Button(text='Launch Child App',font_size=32,size_hint=(1, 0.20))
		b.bind(on_press=self.launchChild)
		
		return b
		
	def launchChild(self, button):
		#return 
		p=subprocess.Popen(["python", "child_2.py"])
		
		"""
		A None value indicates that the process hasn't terminated yet.
		"""
		poll = p.poll()
		if poll == None:
			print "child is running.....\r\n"
		else:
			print "child died...........\r\n"
	#def build(self):
		#return Image(source='/home/pi/nkonnect/hdmi.jpg')

MyApp().run()