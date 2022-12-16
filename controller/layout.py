from kivy.uix.screenmanager import ScreenManager
from kivymd.toast import toast
import json as j


with open("media/media.json") as k:
    data = j.load(k)




class My_Layout_encrypt(ScreenManager):

    data_m_encrypt = data["media_m_encrypt"]["1"]
    data_m_decrypt = data["media_m_decrypt"]["1"]
    data_bg = data["media_bg"]["1"]
    data_logo = data["media_logo"]["1"]
    data_seconde_bg = data["media_seconde_bg"]["1"]

    #definition des coeficients de transformations
    DIE = 128    #code 128 parametre
    KEY = (7, 3, 55)  #coefficient

    def __init__(self, **kwargs):
        super(My_Layout_encrypt, self).__init__(**kwargs)


    def push_process(self, id_textfield_encrypt):
        toast("déclanchement du processus...")
        self.ids.id_textfield_decrypt.text = "".join(map(self.decryptChar, id_textfield_encrypt))




    def encryptChar(self, char):
        K1, K2, kI = self.KEY
        return chr((K1 * ord(char) + K2) % self.DIE)

    def encrypt(self, string):
        return "".join(map(self.encryptChar, string))

    def decryptChar(self, char):
        K1, K2, KI = self.KEY
        return chr(KI * (ord(char) - K2) % self.DIE)



