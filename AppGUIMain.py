import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="length: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="softness: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="price: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.submit = Button(text="confirm", font_size=30)
        self.add_widget(self.submit)


class GuiMain(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    GuiMain().run()
