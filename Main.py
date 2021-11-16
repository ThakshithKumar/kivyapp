import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen


def pressed(instance):
    print("Generator is pressed")


def pressed2(instance):
    print("Scanner is pressed")


class MainWindow(Screen):
    pass


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


'''class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.rows = 2

        self.button = Button(text="Generator")
        self.add_widget(self.button)
        self.button.bind(on_press=pressed)

        self.button2 = Button(text="Scanner")
        self.add_widget(self.button2)
        self.button2.bind(on_press=pressed2)
'''

kv = Builder.load_file("my.kv")


class Main(App):
    def build(self):
        return kv


if __name__ == "__main__":
    Main().run()
