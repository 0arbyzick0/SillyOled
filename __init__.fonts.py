from sillyGFX.fonts.font5x7 import DATA as font5x7_data, WIDTH as font5x7_width, HEIGHT as font5x7_height
from sillyGFX.fonts.font8x16 import DATA as font8x16_data, WIDTH as font8x16_width, HEIGHT as font8x16_height

def get_font_5x7():
    return font5x7_data, font5x7_width, font5x7_height

def get_font_8x16():
    return font8x16_data, font8x16_width, font8x16_height

__all__ = ['get_font_5x7', 'get_font_8x16']