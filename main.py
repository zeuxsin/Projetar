import os, sys
from kivy.resources import resource_add_path, resource_find
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from screens.login_screen.loginscreen import LoginScreen
from screens.mainmenu_screen.mainmenuscreen import MainMenuScreen
from screens.perfil_screen.perfilscreen import PerfilScreen
from screens.register_screen.registerscreen import RegisterScreen
from screens.main_screen.mainscreen import MainScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivymd.uix.behaviors import RectangularRippleBehavior, BackgroundColorBehavior, CircularRippleBehavior, FakeRectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window

Window.size = (310, 580)

class ProfileCard(MDFloatLayout, FakeRectangularElevationBehavior):
    pass

class SearchBar(MDFloatLayout, FakeRectangularElevationBehavior):
    pass

class ProfileButton(Image, Button):
    pass

class LiveApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        self.sm = MDScreenManager()
    def build(self):
        self.sm.add_widget(MainScreen())
        self.sm.add_widget(LoginScreen())
        self.sm.add_widget(PerfilScreen())
        self.sm.add_widget(RegisterScreen())
        self.sm.add_widget(MainMenuScreen())
        return self.sm

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    LiveApp().run()