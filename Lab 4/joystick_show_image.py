# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
Be sure to check the learn guides for more usage information.

This example is for use on (Linux) computers that are using CPython with
Adafruit Blinka to support CircuitPython libraries. CircuitPython does
not support PIL/pillow (python imaging library)!

Author(s): Melissa LeBlanc-Williams for Adafruit Industries
"""
from __future__ import print_function
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789  # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import
import qwiic_joystick
import time
import sys




def has_moved_left(joystick):
    if joystick.horizontal == 0 and joystick.vertical == 506:
        return True
    return False

# def runExample():
#     myJoystick = qwiic_joystick.QwiicJoystick()

#     if myJoystick.connected == False:
#         print("The Qwiic Joystick device isn't connected to the system. Please check your connection",
#               file=sys.stderr)
#         return

#     myJoystick.begin()

#     print("Initialized. Firmware Version: %s" % myJoystick.version)

#     while True:
#         if has_moved_left(myJoystick):


#     time.sleep(.5)


# if __name__ == '__main__':
# 	try:
# 		runExample()
# 	except (KeyboardInterrupt, SystemExit) as exErr:
# 		print("\nEnding Example 1")
# 		sys.exit(0)
# Configuration for CS and DC pins (these are PiTFT defaults):


cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# pylint: disable=line-too-long
# Create the display:
# disp = st7789.ST7789(spi, rotation=90,                            # 2.0" ST7789
# disp = st7789.ST7789(spi, height=240, y_offset=80, rotation=180,  # 1.3", 1.54" ST7789
# disp = st7789.ST7789(spi, rotation=90, width=135, height=240, x_offset=53, y_offset=40, # 1.14" ST7789
# disp = hx8357.HX8357(spi, rotation=180,                           # 3.5" HX8357
# disp = st7735.ST7735R(spi, rotation=90,                           # 1.8" ST7735R
# disp = st7735.ST7735R(spi, rotation=270, height=128, x_offset=2, y_offset=3,   # 1.44" ST7735R
# disp = st7735.ST7735R(spi, rotation=90, bgr=True,                 # 0.96" MiniTFT ST7735R
# disp = ssd1351.SSD1351(spi, rotation=180,                         # 1.5" SSD1351
# disp = ssd1351.SSD1351(spi, height=96, y_offset=32, rotation=180, # 1.27" SSD1351
# disp = ssd1331.SSD1331(spi, rotation=180,                         # 0.96" SSD1331
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)
# pylint: enable=line-too-long

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height
image = Image.new("RGB", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image)

image = Image.open("dog_bone3.jpeg")
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True



text_image = Image.new("RGB", (135, 240))
text_draw = ImageDraw.Draw(text_image)
text_draw.rectangle((0, 0, 135, 240), outline=0, fill=(0, 0, 0))
# disp.image(text_image, 90)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.


# Scale the image to the smaller screen dimension
image_ratio = image.width / image.height
screen_ratio = width / height
if screen_ratio < image_ratio:
    scaled_width = image.width * height // image.height
    scaled_height = height
else:
    scaled_width = width
    scaled_height = image.height * width // image.width
image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

# Crop and center the image
x = scaled_width // 2 - width // 2
y = scaled_height // 2 - height // 2
image = image.crop((x, y, x + width, y + height))

myJoystick = qwiic_joystick.QwiicJoystick()

if myJoystick.connected == False:
    print("The Qwiic Joystick device isn't connected to the system. Please check your connection", file=sys.stderr)


myJoystick.begin()

print("Initialized. Firmware Version: %s" % myJoystick.version)

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

while True:

    # Draw a black filled box to clear the image.
    text_draw.rectangle((0, 0, width, height), outline=0, fill=0)

    display_text = "Please toggle left to choose your desired toy."
    text_draw.text((0, 50), display_text, font=font, fill="#FF00FF")

    # Display image.
    disp.image(text_image)

    if has_moved_left(myJoystick):
        text_draw.rectangle((0, 0, width, height), outline=0, fill=0)
        print('inside')
        disp.image(image)
        # Display image.
