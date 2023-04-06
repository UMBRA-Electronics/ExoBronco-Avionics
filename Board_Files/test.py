import time
import board
import microcontroller
import busio
import adafruit_adxl37x
import adafruit_bmp3xx
import adafruit_lis331
import adafruit_ms8607

# Initialize I2C bus
i2c = busio.I2C(board.IO9, board.IO8)

# Check for connected I2C devices
while not i2c.try_lock():
    pass
devices = i2c.scan()
i2c.unlock()

# Test each I2C device
for device in devices:
    try:
        print()
        print("-------------------------------------------------------")
        print("Testing device at address: ", hex(device))
        if device == 0x76:
            sensor = adafruit_ms8607.MS8607(i2c)
            print("MS8607 P/T sensor found!")
            print("Temperature: ", sensor.temperature)
            print("Pressure: ", sensor.pressure)
        elif device == 0x40:
            sensor = adafruit_ms8607.MS8607(i2c)
            print("MS8607 H sensor found!")
            print("Humidity: ", sensor.relative_humidity)
        elif device == 0x77:
            sensor = adafruit_bmp3xx.BMP3XX_I2C(i2c, 0x77)
            print("BMP390 sensor found!")
            print("Temperature: ", sensor.temperature)
            print("Pressure: ", sensor.pressure)
        elif device == 0x1d:
            sensor = adafruit_adxl37x.ADXL375(i2c, 0x1d)
            print("ADXL375 accelerometer found!")
            print("Acceleration (m/s^2): X=%0.3f, Y=%0.3f, Z=%0.3f" % sensor.acceleration)
        elif device == 0x19:
            sensor = adafruit_lis331.LIS331HH(i2c, 0x19)
            print("LIS331 accelerometer found!")
            print("Acceleration (m/s^2): X=%0.3f, Y=%0.3f, Z=%0.3f" % sensor.acceleration)
        else:
            raise ValueError("Unknown device at address: ", hex(device))
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print("Error testing device at address ", hex(device), ": ", e)

    time.sleep(0.5) # Pause between sensor tests
print()
print("-------------------------------------------------------")
