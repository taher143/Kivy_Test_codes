import kivy
kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class MyApp(App):

    def btn_callback(self, *args):

        # This callback changes the image source
        if self.wimg.source == "wild-birds.jpg":
            self.wimg.source = "image_3.png"
        else:
            self.wimg.source = "wild-birds.jpg"

    def build(self):
        # Set up the layout:
        layout = GridLayout(cols=5, spacing=30, padding=30, row_default_height=150)

        # Create the image
        self.wimg = Image(source='wild-birds.jpg')

        # Create a button
        btn = Button(text="Click Me")

        # Bind it to a callback function
        btn.bind(on_press=self.btn_callback)

        # Add the UI elements to the layout:
        layout.add_widget(self.wimg)
        layout.add_widget(btn)

        return layout

if __name__ == '__main__':
        MyApp().run()