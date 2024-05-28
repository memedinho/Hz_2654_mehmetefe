from machine import Pin, SoftI2C , ADC
import ssd1306
from time import sleep


i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
pot = ADC(Pin(34))
pot.width(ADC.WIDTH_10BIT)
pot.atten(ADC.ATTN_11DB)

led=Pin(14,Pin.OUT)
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    oled.fill(0)
    pot_res = pot.read()
    oled.text(str(pot_res),0,0)
    oled.show()
    if 500<pot_res<700:
        led.on()
    elif pot_res<500:
        led.off()
    elif pot_res>700:
        led.off()
    sleep(0.2)