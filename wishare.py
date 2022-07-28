# +------------------------------------------------------------+
# | This Python file uses the following encoding: utf-8        |
# +------------------------------------------------------------+



from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from server import Server
from threading import Thread

PATH = ""
class MainWindow(BoxLayout):

    addr = StringProperty("Link : nothing is shared now ..." )
    #stop_btn = ObjectProperty()
    server = Server()

    def start_server(self):
        self.addr = f"Type this link in your browser : http://{self.server.get_ip()}:{Server.PORT}"
        Thread(target=self.server.start_server).start()

        self.ids.start_btn.disabled = True
        self.ids.stop_btn.disabled = False

    def stop_server(self):
        self.server.close_server()

        self.ids.start_btn.disabled = False
        self.ids.stop_btn.disabled = True

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