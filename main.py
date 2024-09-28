"""
Script for managing hot reloading of the project.
For more details see the documentation page -

https://kivymd.readthedocs.io/en/latest/api/kivymd/tools/patterns/create_project/

To run the application in hot boot mode, execute the command in the console:
DEBUG=1 python main.py
"""

# import importlib
# import os

# from kivy import Config

# from PIL import ImageGrab

# # TODO: You may know an easier way to get the size of a computer display.

# resolution = ImageGrab.grab().size

# # Change the values of the application window size as you need.
# # Config.set("graphics", "height", resolution[1])
# # Config.set("graphics", "width", "200")


# from kivy.core.window import Window

# # Place the application window on the right side of the computer screen.
# Window.top = 0
# Window.left = resolution[0] - Window.width

# from kivymd.tools.hotreload.app import MDApp
# from kivymd.uix.screenmanager import MDScreenManager


# class KWMAPP(MDApp):
#     KV_DIRS = [os.path.join(os.getcwd(), "View")]

#     def build_app(self) -> MDScreenManager:
#         """
#         In this method, you don't need to change anything other than the
#         application theme.
#         """
#         # green btn hex: background: var(--G1, #69BD3D);  secondarycolor hex: background: var(--B1, #0C222F);
#         self.theme_cls.primary_palette = "Green"  # This is to set a general palette.
#         self.theme_cls.primary_hue = "900"  # Use the hue as "500" for a mid-range green color.
#         # self.theme_cls.primary_color = [0.41, 0.74, 0.24, 1]  # Set the primary color to #69BD3D (as RGBA)

#         import View.screens

#         self.manager_screens = MDScreenManager()
#         Window.bind(on_key_down=self.on_keyboard_down)
#         importlib.reload(View.screens)
#         screens = View.screens.screens

#         for i, name_screen in enumerate(screens.keys()):
#             model = screens[name_screen]["model"]()
#             controller = screens[name_screen]["controller"](model)
#             view = controller.get_view()
#             view.manager_screens = self.manager_screens
#             view.name = name_screen
#             self.manager_screens.add_widget(view)

#         return self.manager_screens

#     def on_keyboard_down(self, window, keyboard, keycode, text, modifiers) -> None:
#         """
#         The method handles keyboard events.

#         By default, a forced restart of an application is tied to the
#         `CTRL+R` key on Windows OS and `COMMAND+R` on Mac OS.
#         """

#         if "meta" in modifiers or "ctrl" in modifiers and text == "r":
#             self.rebuild()


# KWMAPP().run()

# After you finish the project, remove the above code and uncomment the below
# code to test the application normally without hot reloading.

# """
# The entry point to the application.
# 
# The application uses the MVC template. Adhering to the principles of clean
# architecture means ensuring that your application is easy to test, maintain,
# and modernize.
# 
# You can read more about this template at the links below:
# 
# https://github.com/HeaTTheatR/LoginAppMVC
# https://en.wikipedia.org/wiki/Model–view–controller
# """
# 
import os
os.environ["KIVY_TEXT"] = "pil"
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.config import Config

from kivy.factory import Factory
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from View.screens import screens
from kivy.metrics import dp
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.lang import Builder
from libs.api import API 
from kivy.storage.jsonstore import JsonStore

Config.set('kivy', 'exit_on_escape', 1)


class Navigation:

    def __init__(self, master: MDScreenManager):
        self.screens = []
        self.master = master
        self.manager = master.manager_screens
        self.count = 0
        self.screens_not_to_recall = ['mobile verification screen', 'otp verification screen']

    def prev(self):
        print('Prev Screens', self.screens)
        try:
            if len(self.screens) > 1:
                self.screens.pop()
                self.count = 0
            else:
                self.count += 1
                MDSnackbar(
                    MDSnackbarText(
                        text="Press again to exit app.",
                    ),
                    y=dp(24),
                    pos_hint={"center_x": 0.5},
                    size_hint_x=0.8,
                ).open()
                if self.count == 2:
                    self.master.stop()
            self.manager.current = self.screens[-1]
        except IndexError as e:
            print(e)
            self.count += 1
            if self.count == 2:
                pass
                # self.master.stop()

    def add_screen(self, screen_name):
        if not screen_name in self.screens_not_to_recall:
            self.screens.append(screen_name)
        return True

    def back(self):
        print(self.screens)
        try:
            self.screens.pop()
            print(self.screens)
            return self.screens[-1]
        except IndexError:
            # returns the boarding screen
            return 'onboarding screen'


class KWMAPP(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.theme_cls.primary_palette = "Green"  # This is to set a general palette.
        self.theme_cls.primary_hue = "900"  # Use the hue as "500" for a mid-range green color.
        self.theme_cls.primary_color = [0.41, 0.74, 0.24, 1]  # Set the primary color to #69BD3D (as RGBA)

        self.api = API
        self.store = JsonStore('user_token.json')
        self.root = MDScreenManager()
        self.manager_screens = self.root
        self.nav = Navigation(self)

        spinner = Factory.MDCircularProgressIndicator(line_width=dp(1.5))
        self.dialog = ModalView(
            auto_dismiss=False,
            background="",
            background_color=[0] * 4,
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            on_pre_open=lambda _: setattr(spinner, "active", True),
            on_dismiss=lambda _: setattr(spinner, "active", False)
        )
        Clock.schedule_once(lambda _: self.dialog.add_widget(spinner), 0)
        # Clock.schedule_once(lambda _: self.add_screen('track order screen', first=True), 0)
        Clock.schedule_once(lambda _: self.add_screen('onboarding screen', first=True), 0)
        # self.add_screen('onboarding screen', first=True)
        Window.bind(on_key_down=self.on_keyboard_down)

    def add_screen(self, name_screen, switch=True, first=False):
        if first:
            self.load_screen(name_screen, switch, first)
            return
        if not self.root.has_screen(name_screen):
            self.dialog.open()
            Clock.schedule_once(lambda _: self.load_screen(name_screen, switch, first=True), 0)
        elif switch:
            Clock.schedule_once(lambda _: self.change_screen(name_screen), 0)

    def load_screen(self, name_screen, switch, first):
        try:
            # if first:
            Builder.load_file(screens[name_screen]["kv"])
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)

            view = controller.get_view()
            view.name = name_screen
            self.manager_screens.add_widget(view)
            print(view)
            if switch:
                Clock.schedule_once(lambda _: self.change_screen(name_screen), 0)
            if first:
                Clock.schedule_once(self.dialog.dismiss, 1)
        except KeyError as e:
            print(e)

    def change_screen(self, name: str):
        if self.manager_screens.current != name:
            self.manager_screens.current = name
        self.nav.add_screen(name)

    def on_keyboard_down(self, window, keyboard, keycode, text, modifiers) -> None:
        """
        The method handles keyboard events.
        """
        # Esc keyboard == 27 keycode == 41
        if keyboard == 27:
            self.nav.prev()
            # self.manager_screens.current = self.nav.back()
            return True
        return False
    
    def store_token(self, token):
        self.store.put('auth', token=token)

    def get_token(self):
        return self.store.get('auth')['token']

    def get_headers(self):
        if self.get_token:
            return {
                "Content-Type": "application/json",
                "Authorization": "Token " + str(self.get_token())
                }
        else:
            return {
                "Content-Type": "application/json"
                }

    def snackbar_notification(self, msg):
        MDSnackbar(
            MDSnackbarText(
                text=f"{msg}",
            ),
            y=dp(24),
            adaptive_size=True,
            pos_hint={"center_x": 0.5, "top": .15},
            size_hint_x=0.8,
        ).open()

KWMAPP().run()
