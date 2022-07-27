# +------------------------------------------------------------+
# | This Python file uses the following encoding: utf-8        |
# +------------------------------------------------------------+


# User Interface importing

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

# Callbacks importing
from server import Server
from threading import Thread


class MainWindow(BoxLayout):

    addr = StringProperty("Link : nothing is shared now ..." )
    server = Server()

    def choose_directory(self):
        pass

    def start_server(self):
        self.addr = f"Type this link in your browser : http://{self.server.get_ip()}:{Server.PORT}"
        th = Thread(target=self.server.launch_server)
        th.start()

    def stop_server(self):
        try:
            self.server.close_server()
        except Exception as e:
            print(e)



class WiShareApp(App):
    pass

if __name__ == "__main__":
    WiShareApp().run()