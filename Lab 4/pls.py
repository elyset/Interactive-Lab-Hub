from __future__ import print_function
import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime
import qwiic_joystick
import sys

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
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

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 35)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

myJoystick = qwiic_joystick.QwiicJoystick()
myJoystick.begin()


def has_moved_left(joystick):
    if joystick.horizontal == 0 and joystick.vertical == 506:
        return True
    return False

def has_moved_right(joystick):
    if joystick.horizontal == 1023 and joystick.vertical == 506:
        return True
    return False


def display_dog_bone():
    image = Image.open("dog_bone7.jpeg")
    image_ratio = image.height / image.width

    screen_ratio = height / width
    if screen_ratio < image_ratio:
        scaled_width = image.height * width // image.width
        scaled_height = width
    else:
        scaled_width = height
        scaled_height = image.width * height // image.height
    image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

    # Crop and center the image
    x = scaled_width // 2 - height // 2
    y = scaled_height // 2 - width // 2
    image = image.crop((x, y, x + height, y + width))
    print(image.width, image.height)
    # Display image.
    disp.image(image)

def display_dog_ball():
    image = Image.open("tennisball.jpg")
    image_ratio = image.height / image.width

    screen_ratio = height / width
    if screen_ratio < image_ratio:
        scaled_width = image.height * width // image.width
        scaled_height = width
    else:
        scaled_width = height
        scaled_height = image.width * height // image.height
    image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

    # Crop and center the image
    x = scaled_width // 2 - height // 2
    y = scaled_height // 2 - width // 2
    image = image.crop((x, y, x + height, y + width))
    print(image.width, image.height)
    # Display image.
    disp.image(image)


while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py
    y = top
    display_text = "Please toggle left or"
    draw.text((x, y), display_text, font=font, fill="#FF00FF")
    display_text2 = "right to choose desired toy."
    draw.text((x, y), display_text2, font=font, fill="#FF00FF")

    # Display image.
    disp.image(image, rotation)
    time.sleep(1)

    if has_moved_left(myJoystick):
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
        display_dog_bone()
        time.sleep(50)

    if has_moved_right(myJoystick):
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
        display_dog_ball()
        time.sleep(3)
