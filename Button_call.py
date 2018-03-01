from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

class Fejkbiljett(App):

    def build(self):
        self.gen_btn = Button(text='Generera',
                         size_hint=(.10, .10),
                         pos=(5, 5),
                         font_size=21)
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
		
if __name__ == "__main__":
    Fejkbiljett().run()