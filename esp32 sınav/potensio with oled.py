from machine import Pin, SoftI2C
import ssd1306
from time import sleep
from machine import Pin, ADC


i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

pot = ADC(Pin(32))
pot.width(ADC.WIDTH_10BIT)
pot.atten(ADC.ATTN_11DB)

while True:
    oled.fill(0)
    pot_res = pot.read()
    oled.text(str(pot_res),0,0)
    sleep(0.2)
    oled.show()
from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(32))
pot.width(ADC.WIDTH_10BIT)
pot.atten(ADC.ATTN_11DB)

while True:
    pot_res = pot.read()
    print(pot_res)
    sleep(0.2)