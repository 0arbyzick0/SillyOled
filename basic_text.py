# basic_text.py
from machine import I2C, Pin
from sillyOled import SillyOled

# Инициализация I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# Инициализация дисплея
oled = SillyOled(i2c, width=128, height=64)

# Очистка экрана
oled.clear()

# Вывод текста с разным выравниванием
oled.text("Привет, мир!", 10, 10, align="left")
oled.text("Центр", 64, 20, align="center")
oled.text("Справа", 128, 30, align="right")

# Обновление экрана
oled.show()
