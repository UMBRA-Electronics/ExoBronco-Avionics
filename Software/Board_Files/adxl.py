import time
import board
import busio
import adafruit_adxl37x

# Initialize I2C bus and accelerometer sensor
i2c = busio.I2C(board.IO9, board.IO8)
accelerometer = adafruit_adxl37x.ADXL375(i2c, 0x1d)

# Define number of calibration samples to take
CALIBRATION_SAMPLES = 1000

# Define calibration values
calibration_x = 0
calibration_y = 0
calibration_z = 0

# Take calibration samples
for i in range(CALIBRATION_SAMPLES):
    x, y, z = accelerometer.acceleration
    calibration_x += x
    calibration_y += y
    calibration_z += z
    time.sleep(0.01)

# Calculate average calibration values
calibration_x /= CALIBRATION_SAMPLES
calibration_y /= CALIBRATION_SAMPLES
calibration_z /= CALIBRATION_SAMPLES

# Print sensor information
print("-------------------------------------------------------")
print("Sensor: ADXL375")
print("Connection: I2C")
print("Calibration values:")
print("X:", calibration_x)
print("Y:", calibration_y)
print("Z:", calibration_z)
print("-------------------------------------------------------")

# Initialize previous acceleration values
prev_x = None
prev_y = None
prev_z = None

# Loop to continuously read and print acceleration values
while True:
    # Read acceleration values
    x, y, z = accelerometer.acceleration

    # Apply calibration values
    x -= calibration_x
    y -= calibration_y
    z -= calibration_z

    # Check if acceleration values have changed
    if (x != prev_x) or (y != prev_y) or (z != prev_z):
        # Print new acceleration values
        print("\rAcceleration: X:{:.2f} Y:{:.2f} Z:{:.2f}".format(x, y, z), end='')

        # Save new acceleration values
        prev_x = x
        prev_y = y
        prev_z = z

    # Wait a short time before repeating loop
    time.sleep(0.5)