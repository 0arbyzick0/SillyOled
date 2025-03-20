# bitmap.py
from machine import I2C, Pin
from sillyOled import SillyOled

# Инициализация I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# Инициализация дисплея
oled = SillyOled(i2c, width=128, height=64)

# Очистка экрана
oled.clear()

# Данные bitmap-изображения (8x8 пикселей)
bitmap_data = [
    0b00011000,
    0b00111100,
    0b01111110,
    0b11111111,
    0b11111111,
    0b01111110,
    0b00111100,
    0b00011000,
]

# Отображение bitmap-изображения
oled.bitmap(10, 10, bitmap_data, 8, 8)

# Обновление экрана
oled.show()
