import time
import board
import busio
import adafruit_bno055
import bitbangio


i2c = busio.I2C(scl=board.IO9, sda=board.IO8,frequency=30000)  # default clock is 100kHz
#i2c = busio.I2C(scl=board.SCL1, sda=board.SDA1, frequency=400000)

imu = adafruit_bno055.BNO055_I2C(i2c, 0x28)

calibrated = False
while True:
    time.sleep(1)
    if not calibrated:
        calibrated = imu.calibrated
        print('Calibration required: sys {} gyro {} accel {} mag {}'.format(*imu.calibration_status))
    print('Temperature {}°C'.format(imu.temperature))
    print('Mag       x {:5.0f}    y {:5.0f}     z {:5.0f}'.format(*imu.magnetic))
    print('Gyro      x {:5.0f}    y {:5.0f}     z {:5.0f}'.format(*imu.gyro))
    print('Accel     x {:5.1f}    y {:5.1f}     z {:5.1f}'.format(*imu.acceleration))
    print('Lin acc.  x {:5.1f}    y {:5.1f}     z {:5.1f}'.format(*imu.linear_acceleration))
    print('Gravity   x {:5.1f}    y {:5.1f}     z {:5.1f}'.format(*imu.gravity))
    print('Heading     {:4.0f} roll {:4.0f} pitch {:4.0f}'.format(*imu.euler))