import kivy
from kivy.app import App
from kivy.uix.image import Image
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

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
        a_string = line.decode("utf-8")
        print(a_string)
