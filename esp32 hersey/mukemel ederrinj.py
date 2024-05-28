from machine import Pin, SoftI2C , ADC
import ssd1306
from time import sleep


relay1 = Pin(26, Pin.OUT)
relay2 = Pin(25, Pin.OUT)



i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
pot = ADC(Pin(34))
pot.width(ADC.WIDTH_10BIT)
pot.atten(ADC.ATTN_11DB)


oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)



def hesaplama(pot_res):
    return ((100 * (pot_res)) / 1024)
    

while True:
    oled.fill(0)
    pot_res = pot.read()
    x = hesaplama(pot_res)

    oled.text(str(x),0,0)
    oled.show()
    if 1<x<20:
        relay1.value(0)
        relay2.value(1)
        sleep(0.2)
    elif x>84:
        relay1.value(1)
        relay2.value(0)
        sleep(0.2)
    else:
        relay1.value(1)
        relay2.value(1)
