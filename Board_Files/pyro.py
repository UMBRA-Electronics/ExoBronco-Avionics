import time
import digitalio
import board
import neopixel

# Define the number of NeoPixels
num_pixels = 1

# Define the pin for the NeoPixel data line
pixel_pin = board.IO15

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.05)

yellow = (255, 255, 0)
orange = (255, 165, 0)
red = (255, 0, 0)




py1 = digitalio.DigitalInOut(board.IO42)
py2 = digitalio.DigitalInOut(board.IO41)
py3 = digitalio.DigitalInOut(board.IO40)
py4 = digitalio.DigitalInOut(board.IO39)

py1.direction = digitalio.Direction.OUTPUT
py2.direction = digitalio.Direction.OUTPUT
py3.direction = digitalio.Direction.OUTPUT
py4.direction = digitalio.Direction.OUTPUT

pixels[0] = (255, 255, 0)
time.sleep(30)
pixels[0] = (255, 165, 0)
time.sleep(20)
pixels[0] = (255, 0, 0)

py1.value = True
time.sleep(.05)
py1.value = False
time.sleep(2)
py2.value = True
time.sleep(.05)
py2.value = False
time.sleep(2)
py3.value = True
time.sleep(.05)
py3.value = False
time.sleep(2)
py4.value = True
time.sleep(.05)
py4.value = False
time.sleep(2)