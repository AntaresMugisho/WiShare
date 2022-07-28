# +------------------------------------------------------------+
# | This Python file uses the following encoding: utf-8        |
# +------------------------------------------------------------+



from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from server import Server
from threading import Thread

PATH = ""
class MainWindow(BoxLayout):

    addr = StringProperty("Link : nothing is shared now ..." )
    server = Server()

    def start_server(self):
        self.addr = f"Type this link in your browser : http://{self.server.get_ip()}:{Server.PORT}"
        th = Thread(target=self.server.launch_server)
        th.start()

    def stop_server(self):
        try:
            self.server.close_server()
        except Exception as e:
            print(e)

    def choose_directory(self):
        pass


class DirectoryChooser(BoxLayout):

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