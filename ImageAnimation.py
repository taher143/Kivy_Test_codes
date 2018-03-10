from kivy.app import App
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
import functools
import os
os.environ["KIVY_BCM_DISPMANX_ID"] = "5"
class ImageAnimation(BoxLayout):
	def __init__(self, **kwargs):
		super(ImageAnimation, self).__init__(**kwargs)
#		self.content = BoxLayout()
		self.orientation = 'vertical' 
		self.anim_image = Image(source = '18719.jpg')
		self.anim_button = Button(on_press=self.animate_image,text="Click Me",size_hint=(0.2,0.10))
		self.add_widget(self.anim_image)
		self.add_widget(self.anim_button)
	def animate_image(self, *args, **kwargs):
		image_animate = Animation()
		
		def f(i, w):
			w.source = 'image%d.jpg' % i #vds_000#0.png
			
		for i in range(10):
			a = Animation(x = (i + 10), duration=(0.10),
							)
			a.on_complete = functools.partial(f, i)
			
			image_animate += a
		
		image_animate.start(self.anim_image)
#		raise SystemExit, "job Done!!\r\nWe're Leaving......"

class Test(App):
	def build(self):
		return ImageAnimation()
		
if __name__ == '__main__':
	Test().run()
