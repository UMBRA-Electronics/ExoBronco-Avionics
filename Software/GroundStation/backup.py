import csv
import time

#Variable Initalization
#Boolean Values
onPad = "n/a"
motor1 = "n/a"
coast1 = "n/a"
motor2 = "n/a"
coast2 = "n/a"
drouge = "n/a"
main = "n/a"
landed = "n/a"
channel1 = "n/a"
channel2 = "n/a"
channel3 = "n/a"
channel4 = "n/a"
channel5 = "n/a"
channel6 = "n/a"

#Float Values
rocketState = "n/a"
missionElapseTimer = "n/a"
connectionStatus = "n/a"
RSSI = "n/a"
packetNumber = "n/a"
frequency = "n/a"
velocity = "n/a"
acceleration = "n/a"
altitude = "n/a"
latitude = "n/a"
longitude = "n/a"
satellites = "n/a" 
pressure1 = "n/a" #Beginning of Flight Stage Values
pressure2 = "n/a"
tempB1 = "n/a"
tempB2 = "n/a"
humidity1 = "n/a"
ax1 = "n/a"
ay1 = "n/a"
az1 = "n/a"
ax2 = "n/a"
ay2 = "n/a"
az2 = "n/a"
alt1 = "n/a"
alt2 = "n/a"
gyroX1 = "n/a"
gyroY1 = "n/a"
gyroZ1 = "n/a"
gyroX2 = "n/a"
gyroY2 = "n/a"
gyroZ2 = "n/a"
pitch = "n/a"
roll = "n/a"
vbatt = "n/a"

booleanList = [onPad,
               motor1,
               coast1,
               motor2,
               coast2,
               drouge,
               main,
               landed,
               channel1,
               channel2,
               channel3,
               channel4,
               channel5,
               channel6]

floatList = [rocketState,
             missionElapseTimer,
             connectionStatus,
             RSSI,
             packetNumber,
             frequency,
             velocity,
             acceleration,
             altitude,
             latitude,
             longitude,
             satellites, 
             pressure1,
             pressure2,
             tempB1,
             tempB2,
             humidity1,
             ax1,
             ay1,
             az1,
             ax2,
             ay2,
             az2,
             alt1,
             alt2,
             gyroX1,
             gyroY1,
             gyroZ1,
             gyroX2,
             gyroY2,
             gyroZ2,
             pitch,
             roll,
             vbatt]

rows = [booleanList,floatList]

for i in range(len(booleanList)):
    booleanList[i] = i + 0

for i in range(len(floatList)):
    floatList[i] = i + 0
    
#PC with open(r"C:\Users\User\Desktop\ExoBronco-Avionics\Software\GroundStation\database.csv", 'w') as f:

while (True): 
    #USE FOR PC 
    with open(r"C:\Users\User\Desktop\ExoBronco-Avionics\Software\GroundStation\database.csv", 'w') as f:
    #USE FOR LAPTOP
    #with open(r"C:\Users\oldri\Desktop\BRONCOPROJECT\ExoBronco-Avionics\Software\GroundStation\database.csv", 'w') as f:
    
        write = csv.writer(f)
        write.writerows(rows)
        f.close()
        for i in range(len(booleanList)):
            booleanList[i] += 1
        
        #Updated code Will go here
        time.sleep(1)