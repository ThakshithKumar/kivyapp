import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy_garden.zbarcam import ZBarCam


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


class GeneratorWindow(Screen):
    pass


class ScannerWindow(Screen):
    pass


kv = Builder.load_file("my.kv")


class Main(App):
    def build(self):
        return kv


if __name__ == "__main__":
    Main().run()
