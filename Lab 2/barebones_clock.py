from datetime import datetime
import time
from num2words import num2words
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime
from adafruit_rgb_display.rgb import color565
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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

button_a_color = "#FF00FF"
button_b_color = "#FFFFFF"

less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six","Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen","Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen","Nineteen"]
tens = ["","Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty","Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]

def number_to_eng_words(num):
  if num == 0:
     return "Zero"
  ans = ""
  i = 0
  while num > 0:
     if num % 1000 != 0:
        ans = helper(num % 1000) + thousands[i] + " " + ans
        i += 1
        num //= 1000
     return ans.strip()

def helper(n):
  if n == 0:
     return ""
  elif n < 20:
     return less_than_20[n] + " "
  elif n < 100:
     return tens[n//10] + " " + helper(n % 10)
  else:
     return less_than_20[n // 100] + " Hundred " + helper(n % 100)

prev_x = x

def find_optimal_end_index(start, end, word_list):
    for i in range(end, start, -1):
        if prev_x + font.getsize("".join(word_list[start:i]))[0] < disp.height:
           return i
    return end

y = top
button_color = button_a_color
while True:
    # Draw a black filled box to clear the image.
    x = 0

    if buttonB.value and not buttonA.value:  # just button A pressed
        button_color = button_a_color
        time.sleep(1)
    if buttonA.value and not buttonB.value:  # just button B pressed 
        button_color = button_b_color 
        time.sleep(1)

    # Prevents text overflowing
    if y >= bottom - 50:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        y = 0
        prev_x = x
        
    today_dt = datetime.today()
    now = datetime.now()
    seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    
    time_to_words = num2words(int(seconds_since_midnight))
    time_to_words_x_len = font.getsize(time_to_words)[0]
    if time_to_words_x_len > disp.height:
        time_to_words_list = list(time_to_words)    
        needed_lines_num = time_to_words_x_len / disp.height
        if needed_lines_num > 1:
            line_start, line_end = 0, len(time_to_words_list) - 1
            j = int(needed_lines_num) + 1
            # Increment j by one for edge cases in which the entire phrase is not complete
            for i in range(j + 1):
                new_end = find_optimal_end_index(line_start, line_end, time_to_words_list)
                if new_end == len(time_to_words_list) - 1:
                    draw.text((prev_x, y), "".join(time_to_words_list[line_start:]), font=font, fill=button_color)
                    prev_x = x + font.getsize("".join(time_to_words_list[line_start:]))[0]
                    break

                draw.text((prev_x,y), "".join(time_to_words_list[line_start:new_end]), font=font, fill=button_color)
                y += font.getsize("".join(time_to_words_list[line_start:new_end]))[1]
                line_start = new_end
                if new_end != line_end:
                    prev_x = x   

    # Display image
    
    disp.image(image, rotation)
    time.sleep(1)
    
