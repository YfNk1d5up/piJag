import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

import piJagClimv1_ui
from arduinoReader import SerialReaderThread
from arduinoWriter import SerialWriterThread
from utils_infpy310 import arduinoSimul, temp, fan, air, temp2tempDial
import serial
import serial.tools.list_ports
import time


class piJagClimateGUI(QMainWindow, piJagClimv1_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Initialize and connect to serial or simulate

        self.comPorts = serial.tools.list_ports.comports()
        self.nameList = list(port.device for port in self.comPorts)
        if len(self.nameList) > 0:
            self.arduino = serial.Serial(port=self.nameList[0], baudrate=115200, timeout=.1)
            self.simul = False
        else:
            self.arduino = arduinoSimul()
            self.simul = True

        # Serial threads

        self.serialReaderThread = SerialReaderThread(serial=self.arduino)
        self.serialReaderThread.receivedPacketSignal.connect(self.serialPacketReceiverCallback)
        self.serialWriterThread = SerialWriterThread(serial=self.arduino)
        self.serialReaderThread.start()
        self.serialWriterThread.start()

        # Label Values

        self._temp = ""
        self._fan = ""
        self._air = ""
        self._tempDial = 15
        self._fanDial = 5


        # Temperature

        #self.tempDial.setValue(21)
        #self.tempValueLabel.setText("26.5")
        #self.temp = self.tempDial.value()

        self.tempDial.valueChanged.connect(self.changeTemp)
        self.tempPlusButton.clicked.connect(self.plusTemp)
        self.tempMinusButton.clicked.connect(self.minusTemp)
        self.tempAutoButton.clicked.connect(self.autoTemp)
        self.tempACButton.clicked.connect(self.tempAC)

        # Fan

        #self.fanDial.setValue(5)
        #self.fan = self.fanDial.value()

        self.fanDial.valueChanged.connect(self.changeFan)
        self.fanMinusButton.clicked.connect(self.minusFan)
        self.fanPlusButton.clicked.connect(self.plusFan)
        self.fanAutoButton.clicked.connect(self.autoFan)

        # Controls

        self.airFaceButton.clicked.connect(self.airFace)
        self.airFeetButton.clicked.connect(self.airFeet)
        self.airFeetFaceButton.clicked.connect(self.airFeetFace)
        self.airFrontDefrostButton.clicked.connect(self.airFront)
        self.airRearDefrostButton.clicked.connect(self.airRear)
        self.airRecyclingButton.clicked.connect(self.airRecycle)

        time.sleep(1.5) # Wait for threads to initialize
        self.write(b'\x10') # Ask for values

    def serialPacketReceiverCallback(self, packet):
        self._temp = temp(packet)
        self._fan = fan(packet)
        self._air = air(packet)
        self.tempValueLabel.setText(self._temp)
        self.fanValueLabel.setText(self._fan)
        self.airValueLabel.setText(self._air)
        self._tempDial = temp2tempDial(self._temp)
        self.tempDial.setValue(self._tempDial)
        self.tempDial.changeColor(self._tempDial)
        if self._fan != 'Auto':
            self._fanDial = int(self._fan)
            self.fanDial.setValue(self._fanDial)
            self.fanDial.changeColor(self._fanDial)


    def write(self, x):
        self.serialWriterThread.write(x)
    # Temperature
    def plusTemp(self, fromChange = False):
        self.write(b'\x03')
    def minusTemp(self, fromChange = False):
        self.write(b'\x02')

    def changeTemp(self):
        _temp = self.tempDial.value()
        diff = int(_temp) - int(self._tempDial)
        for i in range(abs(diff)):
            if diff < 0:
                self.minusTemp(True)
            else:
                self.plusTemp(True)
    def autoTemp(self):
        self.write("?")
    def tempAC(self):
        self.write(b'\x0a')

    # Fan
    def plusFan(self, fromChange = False):
        self.write(b'\x0d')
    def minusFan(self, fromChange = False):
        self.write(b'\x0e')
    def changeFan(self):
        _fan = self.fanDial.value()
        diff = int(_fan) - int(self._fanDial)
        for i in range(abs(diff)):
            if diff < 0:
                self.minusFan()
            else:
                self.plusFan()
    def autoFan(self):
        self.write(b'\x04')

    def airFace(self):
        self.write(b'\x06')
    def airFeet(self):
        self.write(b'\x08')
    def airFeetFace(self):
        self.write(b'\x07')

    def airFront(self):
        self.write(b'\x05')
    def airRear(self):
        self.write(b'\x0b')
    def airRecycle(self):
        self.write(b'\x0c')


def main():
    app = QApplication(sys.argv)
    gui = piJagClimateGUI()

    gui.show()
    app.setStyle('Fusion')
    app.exec_()

if __name__ == '__main__':
    main()