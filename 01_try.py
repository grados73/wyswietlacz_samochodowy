import kivy
from kivy.app import App
from kivy.uix.image import Image
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
oldNum = 1

class MainApp(App):
    def build(self):
        img = Image(source='/home/pi/Documents/kivv/wyswietlacz_samochodowy-main/calosc.png',
                    size_hint=(1, 1),
                    pos_hint={'center_x':.5, 'center_y':.5})

        return img

if __name__ == '__main__':
    app = MainApp()
    app.run()

while True:
    if(ser.in_waiting > 0):
        line = ser.readline()
        a_string = line.decode("utf-8") ##zmiana typu z bytes na string
        for i in a_string:
            if(i == '\r' or i =='\n' or i == '\r\n' or i == ' '): ##omijam znaki nowej lini
                continue
            num = int(a_string.rstrip()) ## ucinam spacje i zmieniam na int
        if (oldNum != num): ##jezli sie cos zmienilo
            print(num)
            oldNum = num
## ZMIANA w GITHUB
