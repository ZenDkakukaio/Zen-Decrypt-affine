from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.config import Config

from controller.layout import My_Layout_encrypt

import json as jj

Config.set("kivy", "window_icon", "")


with open("media/media.json") as m:
    data_logo = jj.load(m)


class My_APP_main(MDApp):
    def build(self):
        self.title = "Test_Encrypt"
        self.icon = data_logo["media_logo"]["1"]
        self.load_all_file_kv()
        return My_Layout_encrypt()


    def load_all_file_kv(self):
        Builder.load_file('view/layout.kv')




if __name__ ==  "__main__":
    obj_app = My_APP_main()
    obj_app.run()