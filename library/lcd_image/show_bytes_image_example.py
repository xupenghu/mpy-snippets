import os
from machine import LCD
import gc

def lcd_image_show(lcd, x, y, img_length, img_wide, path):
    read_size = 0
    file_size = os.stat(path)[6]

    if file_size > 1024:
        read_size = img_length * 2 * 2
        img_wide = 2
    else:
        read_size = file_size

    with open(path, 'rb') as infile:
        while True:
            result = infile.read(read_size)
            if result == b'':
                break

            lcd.show_image(x, y, img_length, img_wide, result)
            y += 2

def main():
    lcd = LCD()
    lcd.light(True)
    lcd.set_color(lcd.WHITE, lcd.BLACK)

    image_buf = bytearray([
    0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFD,0XFF,0XDA,0XFE,0X73,0XF6,0X72,0XFF,0XF9,0XFF,0XFD,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFF,0XFF,0XDF,0XFF,0XBE,0XFF,0XFE,0XFF,0XFD,0XFF,0XDD,0XFF,0XFD,
    0XFF,0XFD,0XFF,0XFB,0XFF,0X56,0XD4,0X89,0XCC,0X88,0XFF,0X55,0XFF,0XDB,0XFF,0XFD,
    0XFF,0XFD,0XFF,0XFD,0XFF,0XFD,0XFF,0XFE,0XFF,0XBE,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFE,0XFF,0X98,0XDD,0XCF,0XFF,0X14,0XFF,0XB8,
    0XFF,0XF9,0XFF,0XD7,0XE4,0XA6,0XF4,0X83,0XF4,0X83,0XE4,0X85,0XFF,0XB6,0XFF,0XF9,
    0XFF,0XD8,0XFF,0X35,0XE5,0XCF,0XFF,0X57,0XFF,0XDD,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XDD,0XFF,0X76,0XCC,0XA8,0XD4,0X86,0XD4,0XA7,
    0XF6,0X0F,0XE5,0X8C,0XE4,0X85,0XEC,0X84,0XF4,0X84,0XE4,0X85,0XE5,0X6B,0XF6,0X0F,
    0XD4,0XA8,0XD4,0XA7,0XD4,0XA7,0XFF,0X34,0XFF,0XBC,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XDF,0XFF,0XFF,0XFF,0XDD,0XFF,0X76,0XD4,0XC7,0XEC,0XC4,0XEC,0XC4,
    0XD4,0X66,0XD5,0X0A,0XF6,0X31,0XFE,0XB3,0XFE,0X93,0XF6,0X30,0XD5,0X0B,0XD4,0X87,
    0XEC,0XC5,0XEC,0XC4,0XDC,0XA6,0XFF,0X34,0XFF,0XFD,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFF,0XFF,0XDF,0XFF,0XDB,0XFF,0X75,0XD4,0X86,0XE4,0XC5,0XDC,0XC6,
    0XFF,0X33,0XFF,0XD8,0XFF,0XFB,0XFF,0XFD,0XFF,0XFC,0XFF,0XDB,0XFF,0XD8,0XFF,0X33,
    0XE4,0XE7,0XE4,0XC5,0XDC,0X85,0XFF,0X53,0XFF,0XFB,0XFF,0XFE,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFE,0XFF,0XFD,0XFF,0XDA,0XFF,0X52,0XDC,0X86,0XE5,0X8D,0XFF,0XD9,
    0XFF,0XFB,0XFF,0XDC,0XFF,0XFE,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XBD,0XFF,0XFC,
    0XFF,0XFA,0XE5,0X8E,0XDC,0XA7,0XFF,0X11,0XFF,0XD9,0XFF,0XFC,0XFF,0XFF,0XF7,0XFF,
    0XFF,0XFC,0XFF,0XDB,0XFE,0XB4,0XE5,0X4D,0XDC,0XA7,0XDC,0XE9,0XFF,0XDA,0XFF,0XFD,
    0XFF,0XFE,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFE,0XFF,0XDA,0XE5,0X0A,0XDC,0X66,0XE5,0X6C,0XFE,0XB3,0XFF,0XFB,0XFF,0XFD,
    0XFE,0XF4,0XC4,0X68,0XE4,0XA5,0XEC,0XA5,0XDC,0X67,0XFF,0X56,0XFF,0XDD,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFF,0XFF,0XFE,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFC,0XFF,0X76,0XDC,0X86,0XEC,0XC5,0XDC,0X84,0XC4,0X88,0XFE,0XF3,
    0XFF,0XD8,0XDD,0X2A,0XF4,0XA3,0XF4,0XA3,0XED,0X2B,0XFF,0XBA,0XFF,0XDE,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFF,0XFF,0XFE,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XDD,0XFF,0XD9,0XED,0X6C,0XF4,0X83,0XF4,0XA4,0XDD,0X0A,0XFF,0XB6,
    0XFF,0XDD,0XFF,0XB9,0XD4,0X65,0XE4,0XA5,0XFE,0X51,0XFF,0XDB,0XFF,0XFE,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFE,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFE,0XFF,0XFC,0XFE,0X93,0XE4,0X86,0XDC,0X46,0XFF,0X98,0XFF,0XDC,
    0XFF,0XDF,0XFF,0XDB,0XFF,0X10,0XD4,0X85,0XFF,0X15,0XFF,0XFC,0XFF,0XFE,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFF,0XFF,0XFD,0XFF,0X37,0XDC,0X67,0XFE,0X90,0XFF,0XDB,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XBB,0XFF,0X72,0XD4,0XA5,0XFF,0X15,0XFF,0XFD,0XFF,0XFE,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XDF,0XFF,0XFE,0XFF,0X37,0XDC,0X66,0XFF,0X11,0XFF,0XDB,0XFF,0XFF,
    0XFF,0XFD,0XFF,0XD9,0XDC,0XC6,0XDC,0XC5,0XF6,0X92,0XFF,0XFC,0XFF,0XFE,0XFF,0XDF,
    0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFF,0XFF,0XFD,0XFE,0XD4,0XDC,0X86,0XE4,0XC7,0XFF,0XB9,0XFF,0XFD,
    0XFF,0X98,0XF5,0XAD,0XEC,0XA3,0XEC,0XA3,0XED,0XCD,0XFF,0XDA,0XFF,0XFE,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFE,0XFF,0XDA,0XF5,0XCD,0XEC,0X84,0XEC,0X84,0XED,0X6B,0XFF,0XB6,
    0XFF,0X15,0XC4,0X68,0XEC,0XA5,0XEC,0XA4,0XD4,0X87,0XFF,0XD7,0XFF,0XDD,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XDC,0XFF,0XD7,0XD4,0X87,0XEC,0XC5,0XE4,0XA5,0XCC,0X88,0XFE,0XB2,
    0XFF,0XDC,0XFF,0X37,0XED,0XEF,0XD4,0XA7,0XDC,0X86,0XED,0X6B,0XFF,0XDC,0XFF,0XDF,
    0XFF,0XDF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFE,0XFF,0XFB,0XED,0X8D,0XD4,0X86,0XD4,0XC8,0XED,0XEF,0XFF,0X16,0XFF,0XFB,
    0XFF,0XFF,0XFF,0XFD,0XFF,0XFA,0XFF,0XD7,0XFE,0XCF,0XD4,0X66,0XF5,0XF1,0XFF,0XDB,
    0XFF,0XDC,0XFF,0XDD,0XFF,0XFE,0XFF,0XFE,0XFF,0XFF,0XFF,0XFF,0XFF,0XDE,0XFF,0XDD,
    0XFF,0XDA,0XFE,0X72,0XD4,0X67,0XFE,0X8F,0XFF,0XD7,0XFF,0XFA,0XFF,0XFD,0XFF,0XFD,
    0XFF,0XFF,0XFF,0XFF,0XFF,0XFD,0XFF,0XFA,0XFF,0X54,0XE4,0X87,0XE4,0X86,0XF5,0X8B,
    0XFF,0XB7,0XFF,0XDA,0XFF,0XFC,0XFF,0XFD,0XFF,0XFE,0XFF,0XFD,0XFF,0XDB,0XFF,0XD7,
    0XFD,0XCC,0XDC,0X85,0XE4,0X86,0XFF,0X13,0XFF,0XFB,0XFF,0XFD,0XFF,0XFE,0XFF,0XFF,
    0XFF,0XDF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFC,0XFF,0X56,0XDC,0X87,0XF4,0XC5,0XE4,0XA4,
    0XCC,0X88,0XED,0XD0,0XFF,0X15,0XFF,0X57,0XFF,0X57,0XFE,0XF6,0XE5,0XF0,0XCC,0XA9,
    0XE4,0XA5,0XEC,0XC4,0XDC,0X86,0XFF,0X54,0XFF,0XDC,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFD,0XFF,0X56,0XD4,0X88,0XE4,0XA6,0XDC,0XA6,
    0XDD,0X0B,0XD4,0XEA,0XE4,0XA6,0XEC,0X84,0XEC,0X85,0XE4,0XA7,0XD4,0XCA,0XDD,0X2B,
    0XD4,0X86,0XE4,0XC6,0XD4,0XA7,0XFF,0X13,0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFF,0XFF,0XDF,0XFF,0XFD,0XFF,0X78,0XCC,0XEC,0XFE,0X50,0XFF,0X75,
    0XFF,0XD8,0XFF,0XB6,0XE4,0X64,0XFC,0XA3,0XF4,0X83,0XDC,0X44,0XFF,0XB6,0XFF,0XD8,
    0XFF,0X96,0XFE,0X71,0XCC,0XEB,0XFF,0X77,0XFF,0XFD,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XDF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFD,0XFF,0XDC,0XFF,0XFC,0XFF,0XFC,
    0XFF,0XFD,0XFF,0XDB,0XFE,0XD2,0XDC,0X86,0XD4,0X86,0XFE,0XD0,0XFF,0XFA,0XFF,0XFD,
    0XFF,0XFD,0XFF,0XDC,0XFF,0XFC,0XFF,0XFD,0XFF,0XFE,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
    0XFF,0XDF,0XFF,0XDF,0XFF,0XFF,0XFF,0XFF,0XF7,0XFE,0XFF,0XFF,0XFF,0XFF,0XF7,0XFF,
    0XFF,0XFF,0XFF,0XFD,0XFF,0XB8,0XF5,0XAD,0XED,0XCB,0XFF,0XF6,0XFF,0XFC,0XFF,0XFF,
    0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFE,0XFF,0XFF,0XFF,0XFF,0XFF,0XDF,0XFF,0XFF])

    lcd.show_image(25, 25, 24, 24, image_buf)  # x, y, length, wide
    lcd_image_show(lcd, 70, 70, 100, 100, "ball.img")
    gc.collect()

if __name__ == '__main__':
    main()
