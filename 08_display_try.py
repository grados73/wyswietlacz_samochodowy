#import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import time
from kivy.uix.image import Image
from kivy.clock import Clock
import serial
from kivy.properties import NumericProperty
from kivy.lang import Builder

ser = serial.Serial('COM3', baudrate=9600, timeout=1)
oldNum = 0
cv = 0


class Background(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # create texture
        self.tribe_texture = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\P_active.png").texture
        print("pierwsze wyswietlenie")


class Tribe(Widget, App):
    tribe_textureN = ObjectProperty(None)
    tribe_textureD = ObjectProperty(None)
    tribe_textureR = ObjectProperty(None)
    speed_texture1 = ObjectProperty(None)
    speed_texture10 = ObjectProperty(None)
    turn_left = ObjectProperty(None)
    turn_right = ObjectProperty(None)
    light_day = ObjectProperty(None)
    battery_lvl = ObjectProperty(None)
    distance1 = ObjectProperty(None)
    distance10 = ObjectProperty(None)
    distance100 = ObjectProperty(None)
    angle = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # create texture INICJALIZACJA
        self.tribe_textureN = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\EN_active.png").texture #TRYBY JAZDY
        self.tribe_textureD = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\empty_tribe.jpg").texture #TRYBY JAZDY
        self.tribe_textureR = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\empty_tribe.jpg").texture #TRYBY JAZDY
        self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_0.png").texture #PREDKOSC WARTOSC JEDNOSCI
        self.angle = 0
        self.speed_texture10 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_0.png").texture #PREDKOSC WARTOSC DZIESIĄTEK
        self.turn_left = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\empty_turn_left.jpg").texture #KIERUNKOWSKAZ LEWY
        self.turn_right = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\empty_turn_right.jpg").texture #KIERUNKOWSKAZ PRAWY
        self.light_day = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\empty_lights.jpg").texture #ŚWIATŁA
        self.battery_lvl = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\empty_battery.jpg").texture  #BATERIA

    def zmien_tryb(self, time_passed):
        licznik = 1
        oldNum = 0
        num = 0
## cześć dotycząca obrabiania danych z uart
        if (ser.in_waiting > 0):
            line = ser.readline()
            a_string = line.decode("utf-8")  ##zmiana typu z bytes na string
            for i in a_string:
                if (i == '\r' or i == '\n' or i == '\r\n' or i == ' '):  ##omijam znaki nowej lini
                    continue
                num = int(a_string.rstrip())  ## ucinam spacje i zmieniam na int
            if (oldNum != num):  ##jezli sie cos zmienilo
                print(num)
                oldNum = num ## num to jest końcowa wartosc otrzymana z uart
## CZĘŚĆ DOTYCZĄCA RYSOWANIA NA WYSWIETLACZU - REAGOWANIE NA OTRZYMANE WIADOMOSCI
    ## ZMIANA TRYBÓW JAZDY
            if num == 401: #TRYB D
                self.tribe_textureD = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\D_active.png").texture
                self.tribe_textureD = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\D_active.png").texture
                self.tribe_textureN = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\empty_tribe.jpg").texture
                self.tribe_textureR = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\empty_tribe.jpg").texture
            elif num == 411: #TRYB N
                self.tribe_textureN = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\EN_active.png").texture
                self.tribe_textureD = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\empty_tribe.jpg").texture
                self.tribe_textureR = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\empty_tribe.jpg").texture
            elif num == 410: #TRYB R
                self.tribe_textureR = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\R_active.png").texture
                self.tribe_textureN = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\empty_tribe.jpg").texture
                self.tribe_textureD = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\empty_tribe.jpg").texture
    ##ZMIANA PRĘDKOSCI
        #WARTOSCI OD 0 DO 10 KM /H
            if num >=200 and num <= 209:
                self.speed_texture10 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_0.png").texture
                if num == 200:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_0.png").texture
                    self.angle = 0
                    global cv
                    cv=1
                elif num == 201:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_1.png").texture
                    self.angle = 10
                elif num == 202:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_2.png").texture
                    self.angle = 20
                elif num == 203:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_3.png").texture
                    self.angle = 30
                elif num == 204:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_4.png").texture
                    self.angle = 40
                elif num == 205:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_5.png").texture
                    self.angle = 50
                elif num == 206:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_6.png").texture
                    self.angle = 60
                elif num == 207:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_7.png").texture
                    self.angle = 70
                elif num == 208:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_8.png").texture
                    self.angle = 0
                elif num == 209:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_9.png").texture

        #WARTOSCI OD 10 DO 99 KM/H
            elif num >= 210 and num <= 299:
                predkosc = num - 200
                if predkosc >= 90:
                    self.speed_texture10 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_9.png").texture
                elif predkosc >= 80:
                    self.speed_texture10 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_8.png").texture
                elif predkosc >= 70:
                    self.speed_texture10 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_7.png").texture
                elif predkosc >= 60:
                    self.speed_texture10 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_6.png").texture
                elif predkosc >= 50:
                    self.speed_texture10 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_5.png").texture
                elif predkosc >= 40:
                    self.speed_texture10 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_4.png").texture
                elif predkosc >= 30:
                    self.speed_texture10 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_3.png").texture
                elif predkosc >= 20:
                    self.speed_texture10 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_2.png").texture
                elif predkosc >= 10:
                    self.speed_texture10 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_1.png").texture
            #JEDNOSCI DLA WARTOSCI OD 10 DO 99 KM/H
                jednosci = predkosc % 10
                if jednosci == 0:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_0.png").texture
                elif jednosci == 1:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_1.png").texture
                elif jednosci == 2:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_2.png").texture
                elif jednosci == 3:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_3.png").texture
                elif jednosci == 4:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_4.png").texture
                elif jednosci == 5:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_5.png").texture
                elif jednosci == 6:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_6.png").texture
                elif jednosci == 7:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_7.png").texture
                elif jednosci == 8:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_8.png").texture
                elif jednosci == 9:
                    self.speed_texture1 = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\speed_9.png").texture
        #KIERUNKOWSKAZY
            elif num == 51: #prawy kierunkowskaz on
                self.turn_right = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\kturn_right.png").texture
            elif num == 50: #prawy kierunkowskaz off
                self.turn_right = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\empty_turn_right.jpg").texture
            elif num == 61: # lewy kierunkowskaz on
                self.turn_left = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\kturn_left.png").texture
            elif num == 60: #lewy kierunkowskaz off
                self.turn_left = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\empty_turn_right.jpg").texture
        #ŚWIATŁA
            elif num == 71: #włącz światła
                self.light_day = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\lights.png").texture
            elif num == 70: #wyłącz światła
                self.light_day = Image(source="D:\Projekty\wyswietlacz_samochodowy\png\empty_lights.jpg").texture
        #BATERIA
            elif num >= 300 and num <= 399:
                pass
        #KĄT OBROTU

        #NIEZNANA WIADOMOSC
            else:
                pass

class MainApp(App):
    def on_start(self):
        Clock.schedule_interval(self.root.ids.tribe.zmien_tryb, 1 / 200)
#        Clock.schedule_interval(self.root.ids.speed.zmien_predkosc, 1 / 10)
        pass

    pass


if __name__ == "__main__":
    MainApp().run()
