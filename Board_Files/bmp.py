import time
import board
import busio
import adafruit_bmp3xx

# Initialize I2C bus and BMP390 sensor
i2c = busio.I2C(board.IO9, board.IO8)
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c, 0x77)

# Set the pressure and temperature oversampling to the highest resolution
bmp.pressure_oversampling = 8
bmp.temperature_oversampling = 2

# Print sensor information
print("-------------------------------------------------------")
print("Sensor: BMP390")
print("Connection: I2C")
print("Temperature oversampling:", bmp.temperature_oversampling)
print("Pressure oversampling:", bmp.pressure_oversampling)
print("-------------------------------------------------------")

# Initialize variables to hold previous temperature and pressure values
prev_temperature = None
prev_pressure = None

while True:
    # Read temperature and pressure data
    temperature = bmp.temperature
    pressure = bmp.pressure

    # Print data to console if the values have changed
    if temperature != prev_temperature or pressure != prev_pressure:
        print("\rTemperature: {} degrees C, Pressure: {} hPa".format(temperature, pressure), end='')
        prev_temperature = temperature
        prev_pressure = pressure
    # Wait for 1 second
    time.sleep(.5)