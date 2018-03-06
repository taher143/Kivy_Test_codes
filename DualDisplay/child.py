from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
import os
os.environ["KIVY_BCM_DISPMANX_ID"] = "5"

class ChildApp(App):
    def build(self):
		#return Label(text='Child!!')
		return Image(source='wild-birds.jpg')

if __name__ == '__main__':
    ChildApp().run()