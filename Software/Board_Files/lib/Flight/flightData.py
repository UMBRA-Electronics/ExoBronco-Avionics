import csv
from Flight.Pancake import pancake

adxl375_x_acceleration = pancake.ACCEL1.acceleration[0]
adxl375_y_acceleration = pancake.ACCEL1.acceleration[1]
adxl375_z_acceleration = pancake.ACCEL1.acceleration[2]

def initialize():
    with open(pancake.logfile, "w") as file:
        csv_writer = csv.writer(file)

        csv_writer.writerow(['ADXL375_X_Acceleration', 'ADXL375_Y_Acceleration', 'ADXL375_Z_Acceleration', 
                            'H3LIS331_X_Acceleration', 'H3LIS331_Y_Acceleration', 'H3LIS331_Z_Acceleration', 
                            'BNO055_X_Acceleration', 'BNO055_Y_Acceleration', 'BNO055_Z_Acceleration', 
                            'BNO055_X_Gyro', 'BNO055_Y_Gyro', 'BNO055_Z_Gyro', 
                            'BNO055_X_Linear_Acceleration', 'BNO055_Y_Linear_Acceleration', 'BNO055_Z_Linear_Acceleration', 
                            'BNO055_X_Gravity', 'BNO055_Y_Gravity', 'BNO055_Z_Gravity', 
                            'BNO055_1_Euler', 'BNO055_2_Euler', 'BNO055_3_Euler', 
                            'BNO055_1_Quaternion', 'BNO055_2_Quaternion', 'BNO055_3_Quaternion', 'BNO055_4_Quaternion', 
                            '2BNO055_X_Acceleration', '2BNO055_Y_Acceleration', '2BNO055_Z_Acceleration', 
                            '2BNO055_X_Gyro', '2BNO055_Y_Gyro', '2BNO055_Z_Gyro', 
                            '2BNO055_X_Linear_Acceleration', '2BNO055_Y_Linear_Acceleration', '2BNO055_Z_Linear_Acceleration', 
                            '2BNO055_X_Gravity', '2BNO055_Y_Gravity', '2BNO055_Z_Gravity', 
                            '2BNO055_1_Euler', '2BNO055_2_Euler', '2BNO055_3_Euler', 
                            '2BNO055_1_Quaternion', '2BNO055_2_Quaternion', '2BNO055_3_Quaternion', '2BNO055_4_Quaternion', 
                            'MS8607_Temp', 'MS8607_Pressure', 'BMP390_Temp', 'BMP390_Pressure', 
                            'Vbatt', 'Py1', 'Py2', 'Py3', 'Py4',
                            'Latitude', 'Longitude', '# Satellites', 'Altitude', 'Speed', 
                            'Commissioning', 'On Pad', 'Motor 1 Burn', 'Coast 1', 'Motor 2 Burn', 'Coast 2', 'Drouge_Deployed', 'Main_Deployed', 'Touchdown'])

def write():
    with open(pancake.logfile, "a") as file:
        csv_writer = csv.writer(file)

        adxl375_x_acceleration, adxl375_y_acceleration, adxl375_z_acceleration = pancake.acceleration_1()

        h3lis331_x_acceleration, h3lis331_y_acceleration, h3lis331_z_acceleration = pancake.acceleration_2()

        bno055_x_acceleration, bno055_y_acceleration, bno055_z_acceleration = pancake.IMU1_ACCEL()

        bno055_x_gyro, bno055_y_gyro, bno055_z_gyro = pancake.gyro_1()

        bno055_x_linear_acceleration, bno055_y_linear_acceleration, bno055_z_linear_acceleration = pancake.IMU1_LINACCEL()

        bno055_x_gravity, bno055_y_gravity, bno055_z_gravity = pancake.IMU1_GRAVITY()

        bno055_1_euler, bno055_2_euler, bno055_3_euler = pancake.IMU1_EULER()

        bno055_1_quaternion, bno055_2_quaternion, bno055_3_quaternion, bno055_4_quaternion = pancake.IMU1_QUATERNION()

        bno055_2_x_acceleration, bno055_2_y_acceleration, bno055_2_z_acceleration = pancake.IMU2_ACCEL()

        bno055_2_x_gyro, bno055_2_y_gyro, bno055_2_z_gyro = pancake.gyro_2()

        bno055_2_x_linear_acceleration, bno055_2_y_linear_acceleration, bno055_2_z_linear_acceleration = pancake.IMU2_LINACCEL()

        bno055_2_x_gravity, bno055_2_y_gravity, bno055_2_z_gravity = pancake.IMU2_GRAVITY()

        bno055_2_1_euler, bno055_2_2_euler, bno055_2_3_euler = pancake.IMU2_EULER()

        bno055_2_1_quaternion, bno055_2_2_quaternion, bno055_2_3_quaternion, bno055_2_4_quaternion = pancake.IMU2_QUATERNION()

        ms8607_temp, ms8607_pressure = pancake.BARO1.temperature, pancake.pressure_B1()

        bmp390_temp, bmp390_pressure = pancake.BARO2.temperature, pancake.pressure_B2()

        vbatt = pancake.VBATT()

        latitude, longitude, satellites, altitude, speed = pancake.GPS_Lat(), pancake.GPS_Long(), pancake.GPS_Sats(), pancake.GPS_Alt(), pancake.GPS_Speed

        commissioning, onpad, motor1burn = pancake.get_avionic_state("Commissioning"), pancake.get_avionic_state("OnPad"), pancake.get_avionic_state("Motor1Burn")

        coast1, motor2burn, coast2 = pancake.get_avionic_state("Coast1"), pancake.get_avionic_state("Motor2Burn"), pancake.get_avionic_state("Coast2")

        drouge_deployed, main_deployed, touchdown = pancake.get_avionic_state("DrogueDeploy"), pancake.get_avionic_state("MainDeploy"), pancake.get_avionic_state("Landed")

        csv_writer.writerow([adxl375_x_acceleration, adxl375_y_acceleration, adxl375_z_acceleration, 
                            h3lis331_x_acceleration, h3lis331_y_acceleration, h3lis331_z_acceleration, 
                            bno055_x_acceleration, bno055_y_acceleration, bno055_z_acceleration, 
                            bno055_x_gyro, bno055_y_gyro, bno055_z_gyro, 
                            bno055_x_linear_acceleration, bno055_y_linear_acceleration, bno055_z_linear_acceleration, 
                            bno055_x_gravity, bno055_y_gravity, bno055_z_gravity, 
                            bno055_1_euler, bno055_2_euler, bno055_3_euler, 
                            bno055_1_quaternion, bno055_2_quaternion, bno055_3_quaternion, bno055_4_quaternion, 
                            bno055_2_x_acceleration, bno055_2_y_acceleration, bno055_2_z_acceleration, 
                            bno055_2_x_gyro, bno055_2_y_gyro, bno055_2_z_gyro, 
                            bno055_2_x_linear_acceleration, bno055_2_y_linear_acceleration, bno055_2_z_linear_acceleration, 
                            bno055_2_x_gravity, bno055_2_y_gravity, bno055_2_z_gravity, 
                            bno055_2_1_euler, bno055_2_2_euler, bno055_2_3_euler,
                            bno055_2_1_quaternion, bno055_2_2_quaternion, bno055_2_3_quaternion, bno055_2_4_quaternion, 
                            ms8607_temp, ms8607_pressure, bmp390_temp, bmp390_pressure, 
                            vbatt, "N/A", "N/A", "N/A", "N/A", 
                            latitude, longitude, satellites, altitude, speed,
                            commissioning, onpad, motor1burn, 
                            coast1, motor2burn, coast2, 
                            drouge_deployed, main_deployed, touchdown])

def read():
    with open(pancake.logfile, "r") as file:
        print(file.readlines())


def transmit(input_string):
    with open(pancake.logfile, "r") as file:
        file.real_transmit(input_string)

