import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
import subprocess
class MyApp(App):
	def build(self):
		b = Button(text='Launch Child App',font_size=32,size_hint=(1, 0.20))
		b.bind(on_press=self.launchChild)
		
		return b
		
	def launchChild(self, button):
		#return Label(text='Child!!')
		subprocess.Popen(["python", "child_2.py"])
		
	#def build(self):
		#return Image(source='/home/pi/nkonnect/hdmi.jpg')

MyApp().run()