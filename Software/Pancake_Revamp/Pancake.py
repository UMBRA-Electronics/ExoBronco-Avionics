import time
from time import sleep
import board
import digitalio
import busio
from adafruit_ms8607 import MS8607
from analogio import AnalogIn
import adafruit_adxl37x
import adafruit_lis331
import adafruit_bno055
import bitbangio
import storage
import adafruit_rfm9x
import adafruit_sdcard
import adafruit_bmp3xx
import neopixel
import simpleio
import adafruit_gps
import rtc



class BroncoStack:
    def __init__(self):
        # Define dictionary with all the sensors on the board
        self.hardware = {
            'IMU1': False,
            'IMU2': False,
            'BARO1': False,
            'BARO2': False,
            'ACCEL1': False,
            'ACCEL2': False,
            'GPS': False,
            'RADIO': False,
            'SD': False,
        }

        # Define dictionary with all burn ports
        self.BurnPorts = {
            'PORT1': False,
            'PORT2': False,
            'PORT3': False,
            'PORT4': False,
            'PORT5': False,
            'PORT6': False,
        }

        # Define I2C bus
        self.i2c = busio.I2C(board.IO9, board.IO8,frequency=30000)

        # Define Uart
        self.UART1 = busio.UART(board.IO43, board.IO44, baudrate=9600, timeout=10)

        # Define SPI for Radio
        self.spi = busio.SPI(board.IO12, MOSI=board.IO13, MISO=board.IO11)
        self.CS = digitalio.DigitalInOut(board.IO10)
        self.RESET = digitalio.DigitalInOut(board.IO21)

        # Define Radio FREQ
        self.RADIO_FREQ_MHZ = 433.0

        # Define CS pin for SDCARD
        self.cs_SD = digitalio.DigitalInOut(board.IO1)

        # Define and initilizeNEOPIXEL
        self.pixels = neopixel.NeoPixel(board.IO15, 1,brightness=0.05)

        #Define Buzzer
        self.buzzer_Pin = board.IO16

        # Define Vbatt (Find Pin and Define it)
        self.Vbat = AnalogIn(board.IO14)

        self.Avionics_State = 'Commissioning'

        self.last_val = 0xFFFF

        # Define PYRO channel pins
        self.PYRO1 = digitalio.DigitalInOut(board.IO41)
        self.PYRO2 = digitalio.DigitalInOut(board.IO40)
        self.PYRO3 = digitalio.DigitalInOut(board.IO39)
        self.PYRO4 = digitalio.DigitalInOut(board.IO42)

        self.PYRO1.direction = digitalio.Direction.OUTPUT
        self.PYRO2.direction = digitalio.Direction.OUTPUT
        self.PYRO3.direction = digitalio.Direction.OUTPUT
        self.PYRO4.direction = digitalio.Direction.OUTPUT

        

        # Define continuity channel pins
        self.CONT1 = AnalogIn(board.IO4)
        self.CONT2 = AnalogIn(board.IO5)
        self.CONT3 = AnalogIn(board.IO6)
        self.CONT4 = AnalogIn(board.IO7)
        

        # Init accel1
        try:
            self.ACCEL1 = adafruit_adxl37x.ADXL375(self.i2c, 0x1d)
            self.hardware['ACCEL1'] = True

        except Exception as e:
            print("ERROR Accelerometer 1", e)

        # Init IMU1
        try:
            self.IMU1 = adafruit_bno055.BNO055_I2C(self.i2c,0x28)
            self.hardware['IMU1'] = True
        except Exception as e:
            print("ERROR IMU1", e)

        # Init IMU2
        try:
            self.IMU2 = adafruit_bno055.BNO055_I2C(self.i2c, 0x29)
            self.hardware['IMU2'] = True
        except Exception as e:
            print("ERROR IMU2", e)

        # Init accel2
        try:
            self.ACCEL2 = adafruit_lis331.H3LIS331(self.i2c, 0x19)
            self.hardware['ACCEL2'] = True
        except Exception as e:
            print("ERROR Accelerometer 2", e)

        # Init baro1
        try:
            self.BARO1 = MS8607(self.i2c)
            self.hardware['BARO1'] = True
        except Exception as e:
            print("ERROR barometer 1", e)

        # Init baro2
        try:
            self.BARO2 = adafruit_bmp3xx.BMP3XX_I2C(self.i2c)
            self.BARO2.pressure_oversampling = 8
            self.BARO2.temperature_oversampling = 2
            self.hardware['BARO2'] = True
        except Exception as e:
            print("ERROR barometer 2", e)

        # Init Radio
        try:
            self.rfm9x = adafruit_rfm9x.RFM9x(self.spi, self.CS, self.RESET, self.RADIO_FREQ_MHZ)
            self.rfm9x.tx_power = 23
            self.hardware['RADIO'] = True
        except Exception as e:
            print("ERROR Radio", e)

        # Init SD_Card
        try:
            self.sdcard = adafruit_sdcard.SDCard(self.spi, self.cs_SD)
            self.vfs = storage.VfsFat(self.sdcard)
            storage.mount(self.vfs, "/sd")
            self.fs = self.vfs
            self.logfile = "/sd/log.txt"
            self.hardware['SD'] = True
        except Exception as e:
            print("ERROR barometer 1", e)
        
        # Init GPS
        try:
            
            self.gps = adafruit_gps.GPS(self.UART1, debug=False)
            self.gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
            self.gps.send_command(b"PMTK220,500")
            rtc.set_time_source(self.gps)
            self.the_rtc = rtc.RTC()
            self.hardware['GPS'] = True

        except Exception as e:
            print("ERROR GPS", e)

    def pressure_B1(self):
        """
        Returns the pressure readings from BARO1
        :return: Float
        """
        if self.hardware['BARO1']:
            return self.BARO1.pressure

    def pressure_B2(self):
        """
        Returns the pressure readings from BARO2
        :return: Float
        """
        if self.hardware['BARO2']:
            return self.BARO2.pressure

    def temperature_B1(self):
        """
        Returns the temperature readings from BARO1
        :return: Float
        """
        if self.hardware['BARO1']:
            return self.BARO1.temperature

    def temperature_B2(self):
        """
        Returns the temperature readings from BARO2
        :return: Float
        """
        if self.hardware['BARO2']:
            return self.BARO2.temperature

    def relative_humidity_B1(self):
        """
        Returns the relative humidity readings from BARO1
        :return: Float
        """
        if self.hardware['BARO1']:
            return self.BARO1.relative_humidity

    def acceleration_1(self):
        """
        Returns the acceleration readings from ACCEL1
        :return: Float
        """
        if self.hardware['ACCEL1']:
            return self.ACCEL1.acceleration

    def acceleration_2(self):
        """
        Returns the acceleration readings from ACCEL2
        :return: Float
        """
        if self.hardware['ACCEL2']:
            return self.ACCEL2.acceleration

    def gyro_1(self):
        """
        Returns the rotational speeds along all three axis from IMU1
        :return: Float
        """
        if self.hardware['IMU1']:
            return self.IMU1.gyro

    def gyro_2(self):
        """
        Returns the rotational speeds along all three axis from IMU2
        :return: Float
        """
        if self.hardware['IMU2']:
            return self.IMU2.gyro

    def mag_1(self):
        """
        Returns the magnetic field readings from IMU1
        :return: Float
        """
        if self.hardware['IMU1']:
            return self.IMU1.magnetic

    def mag_2(self):
        """
        Returns the magnetic field readings from IMU2
        :return: Float
        """
        if self.hardware['IMU2']:
            return self.IMU2.magnetic
    
    def IMU1_ACCEL(self):
        """
        Returns the acceleration readings from IMU1
        :return: Float
        """
        if self.hardware['IMU1']:
            return self.IMU1.acceleration
    
    def IMU2_ACCEL(self):
        """
        Returns the acceleration readings from IMU2
        :return: Float
        """
        if self.hardware['IMU2']:
            return self.IMU2.acceleration
    
    def IMU1_LINACCEL(self):
        """
        Returns the linear acceleration readings from IMU1
        :return: Float
        """
        if self.hardware['IMU1']:
            return self.IMU1.linear_acceleration
    
    def IMU2_LINACCEL(self):
        """
        Returns the linear acceleration readings from IMU1
        :return: Float
        """
        if self.hardware['IMU2']:
            return self.IMU2.linear_acceleration

    def radio_send(self, message):
        """
        Takes in str message as input and send it over radio
        :param message: String
        :return: None
        """
        if self.hardware['RADIO']:
            self.rfm9x.send(bytes(str(message), "utf-8"))

    def radio_receive(self):
        """
        receives radio message and returns packet
        (needs update to output string instead of packet data)
        :return: String
        """
        if self.hardware['RADIO']:
            return self.rfm9x.receive()

    def SD_Write(self, data):
        """
        takes in data in str form and writes it to
        file on sd card called logile
        :param data: String
        :return: None
        """
        with open(self.logfile, "w") as f:
            t = int(time.monotonic())
            f.write('{},{}\n'.format(t, data))

    def SD_Read(self):
        """
        reads line from logfile file on sdcard
        :return: None
        """
        with open(self.logfile, "r") as f:
            print("Read line from file:")
            print(f.readline(), end='')
    
    def Buzzer(self,tone,pduration):
        """
        takes in tone and duration and plays that tone for that duration
        :return: None
        """
        simpleio.tone(self.buzzer_Pin, tone,duration=pduration)
    
    def Neo(self,RGB1,RGB2,RGB3):
        """
        takes in 3 value RGB value and displays that color on the neopixel
        :return: None
        """
        self.pixels[0] = (RGB1,RGB2,RGB3)
    
    def GPS_Lat(self):
        """
        Returns the GPS Latitude readings
        :return: Float
        """
        if self.hardware['GPS']:
            self.gps.update()
            if self.gps.has_fix:
                return self.gps.latitude
    
    def GPS_Long(self):
        """
        Returns the GPS Latitude readings
        :return: Float
        """
        if self.hardware['GPS']:
            self.gps.update()
            if self.gps.has_fix:
                return self.gps.longitude
    
    def GPS_Alt(self):
        """
        Returns the GPS Latitude readings
        :return: Float
        """
        if self.hardware['GPS']:
            self.gps.update()
            if self.gps.has_fix:
                return self.gps.altitude_m
    
    def GPS_Sats(self):
        """
        Returns the GPS Latitude readings
        :return: Float
        """
        if self.hardware['GPS']:
            self.gps.update()
            if self.gps.has_fix:
                return self.gps.satellites
    
    def _format_datetime(self,datetime):
        return "{:02}/{:02}/{} {:02}:{:02}:{:02}".format(
            datetime.tm_mon,
            datetime.tm_mday,
            datetime.tm_year,
            datetime.tm_hour,
            datetime.tm_min,
            datetime.tm_sec,
    )
    
    def GPS_RTC(self):
        """
        Returns the GPS Latitude readings
        :return: Float
        """
        if self.hardware['GPS']:
            self.gps.update()
            if self.gps.has_fix:
                return self._format_datetime(self.the_rtc.datetime)
                



    def avionic_state(self, state):
        """
        takes in state and sets Avionics_state to
        input state
        (needs to update to include more states)
        :param state: String
        :return: None
        """
        if 'Commissioning' in state:
            self.Avionics_State = 'Commissioning'
        if 'OnPad' in state:
            self.Avionics_State = 'OnPad'
        if 'Motor1Burn' in state:
            self.Avionics_State = 'Motor1Burn'
        if 'Coast1' in state:
            self.Avionics_State = 'Coast1'
        if 'Motor2Burn' in state:
            self.Avionics_State = 'Motor2Burn'
        if 'Motor2Ignition' in state:
            self.Avionics_State = 'Motor2Ignition'
        if 'Coast2' in state:
            self.Avionics_State = 'Coast2'
        if 'DrogueDeploy' in state:
            self.Avionics_State = 'DrogueDeploy'
        if 'MainDeploy' in state:
            self.Avionics_State = 'MainDeploy'
        if 'Landed' in state:
            self.Avionics_State = 'Landed'

    def activate_burn(self, port):
        """
        takes in burn port and activates inputted burn port
        (function needs to be actually written
        also needs to figure out timing for FETS )
        :param port: Port
        :return: None
        """
        if port == 1:
            self.Neo(255,0,0)
            self.PYRO1.value = True
            time.sleep(0.5)
            self.PYRO1.value = False
            self.Neo(0,128,0)
        elif port == 2:
            self.Neo(255,0,0)
            self.PYRO2.value = True
            time.sleep(0.5)
            self.PYRO2.value = False
            self.Neo(0,128,0)
        elif port == 3:
            self.Neo(255,0,0)
            self.PYRO3.value = True
            time.sleep(0.5)
            self.PYRO3.value = False
            self.Neo(0,128,0)
        elif port == 4:
            self.Neo(255,0,0)
            self.PYRO4.value = True
            time.sleep(0.5)
            self.PYRO4.value = False
            self.Neo(0,128,0)

        return
    
    def Continuity(self,port):
        """
        takes in port number and reads the continuity value at that port
        and declares it open or closed
        :param port: Port
        :return: string

        """
        if port == 1:
            if self.CONT1.value == 0:
                return "open"
            elif self.CONT1.value > 100:
                return "closed"
        if port == 2:
            if self.CONT2.value == 0:
                return "open"
            elif self.CONT2.value > 100:
                return "closed"
        if port == 3:
            if self.CONT3.value == 0:
                return "open"
            elif self.CONT3.value > 100:
                return "closed"
        if port == 4:
            if self.CONT4.value == 0:
                return "open"
            elif self.CONT4.value > 100:
                return "closed"




pancake = BroncoStack()
