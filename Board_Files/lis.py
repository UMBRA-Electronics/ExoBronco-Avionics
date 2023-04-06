import time
import board
import busio
import adafruit_lis331

i2c = busio.I2C(board.IO9, board.IO8)
lis = adafruit_lis331.LIS331HH(i2c, 0x19)

# Set up calibration variables
x_offset = 0
y_offset = 0
z_offset = 0
num_samples = 1000

# Perform calibration
print("Calibrating accelerometer...")
for i in range(num_samples):
    x, y, z = lis.acceleration
    x_offset += x
    y_offset += y
    z_offset += z
    time.sleep(0.01)

x_offset /= num_samples
y_offset /= num_samples
z_offset /= num_samples


print("-------------------------------------------------------")
print("Sensor: H3L")
print("Connection: I2C")
print("Calibration values:")
print("X:", x_offset)
print("Y:", y_offset)
print("Z:", z_offset)
print("-------------------------------------------------------")

# Main loop
while True:
    # Read acceleration data and apply calibration offsets
    x, y, z = lis.acceleration
    x -= x_offset
    y -= y_offset
    z -= z_offset

    # Print acceleration data without a newline
    print("\rAcceleration (m/s^2): X=%0.2f Y=%0.2f Z=%0.2f" % (x, y, z), end='')

    # Delay for 0.1 seconds
    time.sleep(0.5)