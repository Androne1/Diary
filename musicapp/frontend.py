from kivy.core.window import Window
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (400, 600)
Window.clearcolor = (6/255, 6/255, 117/255)
Window.title = "What to listen"

class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
class MusicApp(App):
    def buid(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main_screen"))
        
MusicApp().run()