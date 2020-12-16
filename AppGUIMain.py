from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout


class PopWin(FloatLayout):
    pass


class MainWin(Screen):
    def btn(self):
        showPopUp()


class MenuWin(Screen):
    pass


class WinManager(ScreenManager):
    pass


def showPopUp():
    show = PopWin()
    popup_window = Popup(title="window", content="show",
                         size_hint=(None, None), size=(400, 400))
    popup_window.open()


kv = Builder.load_file('guimain.kv')


class GuiMain(App):
    def build(self):
        return kv


if __name__ == "__main__":
    GuiMain().run()
