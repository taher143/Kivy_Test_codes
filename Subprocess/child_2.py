import kivy
kivy.require('1.7.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from functools import partial
from kivy.uix.label import Label
from kivy.properties import StringProperty
import os
import time
import sys



#print "Total files in folder:"
#print len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
os.environ["KIVY_BCM_DISPMANX_ID"] = "5"
class MyApp(App):
	def __init__(self,**kwargs):
		self.image_on = 1
		super(MyApp,self).__init__(**kwargs)
		
		Clock.schedule_interval(self.new_fn,2)
#		Clock.schedule_interval(self.btn_callback,1)
	
	def new_fn(self,*args):
		#while True :
	#s = raw_input("Enter command: ")
		s = sys.stdin.readline()
#			print "Recieved: {}".format(s)
		if "ls" in s:
			self.image_on = 1
			print "Hello"
		else:
			self.image_on = 0
			print "World"
		sys.stdout.flush()
		sys.stdin.flush()
		self.btn_callback()
			
	def btn_callback(self, *args):
		if self.image_on :
			self.wimg.source = "space.png"
#			self.image_on = 0
		else:
			self.wimg.source = "heart.png"
#			self.image_on = 1
		
		
	def build(self):
        # Set up the layout:
		self.layout = GridLayout(cols=5, spacing=30, padding=30, row_default_height=150)

        # Create the image
		self.wimg = Image(source = "")
	
        # Add the UI elements to the layout:
		self.layout.add_widget(self.wimg)
        
		#layout.add_widget(btn)
		return self.layout
	

if __name__ == '__main__':
        MyApp().run()
