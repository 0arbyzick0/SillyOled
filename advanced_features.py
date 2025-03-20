# advanced_features.py
from machine import I2C, Pin
from sillyOled import SillyOled
import time

# Инициализация I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# Инициализация дисплея
oled = SillyOled(i2c, width=128, height=64)

# Очистка экрана
oled.clear()

# Вывод текста
oled.text("Расширенные функции", 10, 10, align="center")

# Изменение контраста
for i in range(0, 256, 16):
    oled.contrast(i)
    time.sleep_ms(100)

# Инверсия цветов
oled.invert(True)
time.sleep(1)
oled.invert(False)

# Выключение дисплея
oled.power(False)
time.sleep(1)
oled.power(True)

# Обновление экрана
oled.show()
