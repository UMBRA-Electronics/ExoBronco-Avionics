import time
import board
import neopixel

# Define the number of NeoPixels
num_pixels = 1

# Define the pin for the NeoPixel data line
pixel_pin = board.IO15

# Create the NeoPixel object
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.05, auto_write=False)

# Define the rainbow function
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

# Define the wheel function to generate colors
def wheel(pos):
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

# Main loop
while True:
    rainbow_cycle(0.005)  # Rainbow cycle with a delay of 1 millisecond between color changes
