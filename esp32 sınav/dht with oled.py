from machine import Pin, SoftI2C
import ssd1306
from time import sleep
import dht

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))


oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
sensor = dht.DHT11(Pin(14))
while True:
  try:
    oled.fill(0)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    oled.text(str(temp),0,0)
    oled.text(str(temp_f),0,10)
    oled.text(str(hum),0,20)
    oled.show()
    sleep(2)
  except OSError as e:
    print('Failed to read sensor.')