# shapes.py
from machine import I2C, Pin
from sillyOled import SillyOled

# Инициализация I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# Инициализация дисплея
oled = SillyOled(i2c, width=128, height=64)

# Очистка экрана
oled.clear()

# Отрисовка прямоугольника
oled.rect(10, 10, 50, 30, fill=True)

# Отрисовка круга
oled.circle(64, 32, 20, fill=True)

# Отрисовка линии
oled.line(0, 0, 128, 64)

# Отрисовка треугольника
oled.triangle(10, 40, 50, 40, 30, 60, fill=True)

# Обновление экрана
oled.show()
