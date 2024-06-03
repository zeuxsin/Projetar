from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from screens.login_screen.loginscreen import LoginScreen
from screens.register_screen.registerscreen import RegisterScreen
from screens.main_screen.mainscreen import MainScreen
from kivy.uix.button import Button

class LiveApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        self.sm = MDScreenManager()
    def build(self):
        self.sm.add_widget(MainScreen())
        self.sm.add_widget(LoginScreen())
        self.sm.add_widget(RegisterScreen())
        return self.sm


LiveApp().run()