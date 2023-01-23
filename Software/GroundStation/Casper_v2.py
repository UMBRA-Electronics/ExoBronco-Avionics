import PyQt5
import PyQt5.QtGui
from PyQt5.QtGui import QIcon
import pyqtgraph
from pyqtgraph import PlotWidget
from PyQt5 import QtWidgets, uic
import sys
import serial.tools.list_ports
import time
import serial
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice

import os ,sys 

basedir = os.path.dirname(__file__)
try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


app = QtWidgets.QApplication([])
ui = uic.loadUi(os.path.join(basedir,'Casper_v2.ui'))
ui.setWindowTitle("Casper Test GUI")


serial = QSerialPort()
serial.setBaudRate(115200)
portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
    portList.append(port.portName())
ui.comboBox_3.addItems(portList)
ui.comboBox_4.addItems(portList)


ui.widget_1.setLabel('bottom', 'Time (S) ')
ui.widget_1.setLabel('left', 'Temp (C)')



pressure = list()
gtime = list()
i = 0

def onRead():
    global i
    if not serial.canReadLine(): return    
    rx = serial.readLine()
    rxs = str(rx, 'utf-8').strip()
    gtime.append(i)
    pressure.append(float(rxs))
    i = i+1
    ui.label_162.setText(rxs)
    ui.widget_1.plot(gtime, pressure)
    
    
    
    

def Open_Button():
    serial.setPortName(ui.comboBox_3.currentText())
    serial.setPortName(ui.comboBox_4.currentText())
    serial.open(QIODevice.ReadWrite)
def Close_Button():
    serial.close()



serial.readyRead.connect(onRead)
ui.pushButton_6.clicked.connect(Open_Button)
ui.pushButton_5.clicked.connect(Close_Button)
ui.pushButton_8.clicked.connect(Open_Button)
ui.pushButton_7.clicked.connect(Close_Button)




ui.setWindowIcon(QIcon(os.path.join(basedir,"Screenshot_20210202-191737_Video_Player.ico")))
ui.show()
app.exec()