# +------------------------------------------------------------+
# | This Python file uses the following encoding: utf-8        |
# +------------------------------------------------------------+

import sys

from kivy.app import App
from kivy.graphics.cgl import Config, platform
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

from os import environ

from server import Server
from threading import Thread


# Resizing Window on Desktop
is_android = 'ANDROID_STORAGE' in environ
if not is_android:
    Config.set('graphics', 'width', '412')
    Config.set('graphics', 'height', '700')


class MainWindow(BoxLayout):
    try:
        DEFAULT_PATH = StringProperty(f"{environ['HOME']}")
    except Exception as e:
        print("ERR_29_WIS", e)
        DEFAULT_PATH = StringProperty(f"{environ['ANDROID_STORAGE']}")

    server_status = StringProperty("Not serving\n" )
    addr = StringProperty("http://192.168.__.__:_____" )
    #stop_btn = ObjectProperty()
    server = Server()

    def start_server(self):
        self.server_status = "Server started\n"
        self.addr = f"\nhttp://{self.server.get_ip()}:{Server.PORT}"
        self.ids.status_label.bold = True

        #self.th = Thread(target=self.server.start_server)
        #self.th.start()

        self.ids.choose_dir_btn.disabled = True
        self.ids.start_btn.disabled = True
        self.ids.stop_btn.disabled = False

    def stop_server(self):
        self.th.join()

        self.server_status = "Server stopped\n"
        self.ids.choose_dir_btn.disabled = False
        self.ids.start_btn.disabled = False
        self.ids.stop_btn.disabled = True

    def choose_directory(self):
        pass


class DirectoryChooser(Popup):

    def select(self, *args):
        try:
            PATH = args #[1][0]
            print(PATH)
        except Exception as e:
            print("ERROR: ", e)



class WiShareApp(App):
    pass


# Run the App
if __name__ == "__main__":
    WiShareApp().run()