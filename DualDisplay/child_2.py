import kivy
kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from functools import partial
import os
os.environ["KIVY_BCM_DISPMANX_ID"] = "5"
class MyApp(App):
	def __init__(self,**kwargs):
		super(MyApp,self).__init__(**kwargs)
		Clock.schedule_interval(self.btn_callback,5)
	
	image_num = 0
	
	def btn_callback(self, *args):
		# This callback changes the image source
		print self.image_num
		if self.image_num < 4:
			self.wimg.source = str(self.image_num)+".jpg"
			self.image_num = self.image_num + 1
		elif self.image_num > 3:
			self.image_num = 0
			raise SystemExit, "job Done!!\r\nWe're Leaving......"
		#if self.wimg.source == "wild-birds.jpg":
		#	self.wimg.source = "image_3.png"
		#else:
		#	self.wimg.source = "wild-birds.jpg"
			
	def build(self):
        # Set up the layout:
		layout = GridLayout(cols=5, spacing=30, padding=30, row_default_height=150)

        # Create the image
		self.wimg = Image(source='wild-birds.jpg')

        # Create a button
        #btn = Button(text="Click Me")

        # Bind it to a callback function
        #btn.bind(on_press=self.btn_callback)
		
        # Add the UI elements to the layout:
		layout.add_widget(self.wimg)
        #layout.add_widget(btn)
		return layout

if __name__ == '__main__':
        MyApp().run()