import time
import board
import busio
import adafruit_ms8607

# Initialize I2C bus and MS8607 sensor
i2c = busio.I2C(board.IO9, board.IO8)
ms8607 = adafruit_ms8607.MS8607(i2c)

# Print sensor information
print("-------------------------------------------------------")
print("Sensor: MS8607")
print("Connection: I2C")
print("-------------------------------------------------------")

# Initialize variables to hold previous temperature, pressure, and humidity values
prev_temperature = None
prev_pressure = None
prev_humidity = None

while True:
    # Read temperature, pressure, and humidity data
    temperature = ms8607.temperature
    pressure = ms8607.pressure
    humidity = ms8607.relative_humidity

    # Print data to console if the values have changed
    if temperature != prev_temperature or pressure != prev_pressure or humidity != prev_humidity:
        print("\rTemperature: {:.2f} degrees C, Pressure: {:.2f} hPa, Humidity: {:.2f} %".format(temperature, pressure, humidity), end='')
        prev_temperature = temperature
        prev_pressure = pressure
        prev_humidity = humidity

    # Wait for 1 second
    time.sleep(1)