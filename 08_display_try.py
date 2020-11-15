import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import time
from kivy.uix.image import Image
from kivy.clock import Clock
import serial


ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)
oldNum = 0

class Background(Widget):
    tribe_texture = ObjectProperty(None)


    def __init__(self, **kwargs):
            super().__init__(**kwargs)
            #create texture
            self.tribe_texture = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\R_active.png").texture
            print("pierwsze wyswietlenie")

    def zmien_tryb(self, time_passed):

        licznik = 1
        oldNum =0
        num = 0
        if (ser.in_waiting > 0):
            line = ser.readline()
            a_string = line.decode("utf-8")  ##zmiana typu z bytes na string
            for i in a_string:
                if (i == '\r' or i == '\n' or i == '\r\n' or i == ' '):  ##omijam znaki nowej lini
                    continue
                num = int(a_string.rstrip())  ## ucinam spacje i zmieniam na int
            if (oldNum != num):  ##jezli sie cos zmienilo
                print(num)
                oldNum = num
            if num == 401:
                self.tribe_texture = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\D_active.png").texture
            elif num == 411:
                self.tribe_texture = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\R_active.png").texture
            elif num == 410:
                self.tribe_texture = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\P_active.png").texture




class MainApp(App):
    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.zmien_tryb, 1/5)
        pass
    pass

if __name__ == "__main__":
    MainApp().run()






#ser = serial.Serial('/dev/ttyACM0', 9600)


#    if(ser.in_waiting > 0):
#        line = ser.readline()
#        a_string = line.decode("utf-8") ##zmiana typu z bytes na string
#        for i in a_string:
#            if(i == '\r' or i =='\n' or i == '\r\n' or i == ' '): ##omijam znaki nowej lini
#                continue
#            num = int(a_string.rstrip()) ## ucinam spacje i zmieniam na int
#        if (oldNum != num): ##jezli sie cos zmienilo
#            print(num)
#            oldNum = num
#