from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWin(Screen):
    pass


class MenuWin(Screen):
    pass


class WinManager(ScreenManager):
    pass


kv = Builder.load_file('guimain.kv')


class GuiMain(App):
    def build(self):
        return kv


if __name__ == "__main__":
    GuiMain().run()
