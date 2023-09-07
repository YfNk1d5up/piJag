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

        # Label default values
        self._temp = ""
        self._fan = ""
        self._air = ""

        # Dial default values
        self._tempDial = 15
        self._fanDial = 5

        # "on" default value
        self._on = 'Off'

        # OnOff
        self.onoffButton.clicked.connect(self.onoff)

        # Temperature
        self.tempDial.sliderReleased.connect(self.changeTemp)
        self.tempDial.valueChanged.connect(self.changeTempColor)
        self.tempPlusButton.clicked.connect(self.plusTemp)
        self.tempMinusButton.clicked.connect(self.minusTemp)
        self.tempAutoButton.clicked.connect(self.autoTemp)
        self.tempACButton.clicked.connect(self.tempAC)

        # Fan
        self.fanDial.sliderReleased.connect(self.changeFan)
        self.fanDial.valueChanged.connect(self.changeFanColor)
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
        if packet[13] == '00':
            self._temp = ''
            self._fan = ''
            self._air = ''
            self.onoffButton.setText('On')
        else:
            self._temp = temp(packet)
            self._fan = fan(packet)
            self._air = air(packet)
            self.onoffButton.setText('Off')
        self.tempValueLabel.setText(self._temp)
        self.fanValueLabel.setText(self._fan)
        self.airValueLabel.setText(self._air)
        self._tempDial = temp2tempDial(self._temp)
        self.tempDial.setValue(self._tempDial)
        self.tempDial.changeColor(self._tempDial)
        print(self._fan)
        if self._fan != 'Auto':
            try:
                self._fanDial = int(self._fan)
                self.fanDial.setValue(self._fanDial)
            except:
                self.fanDial.setValue(6)
            self.fanDial.changeColor(self._fanDial)
        """
        else:
            print('ok')
            self.fanDial.setValue(6)
            self.fanDial.changeColor(6)
        """

    def write(self, x):
        self.serialWriterThread.write(x)

    def onoff(self):
        self.write(b'\x01')

    # Temperature
    def plusTemp(self, fromChange = False):
        self.write(b'\x03')
    def minusTemp(self, fromChange = False):
        self.write(b'\x02')

    def changeTemp(self):
        self.serialWriterThread.clearQueues()
        _temp = self.tempDial.value()
        diff = int(_temp) - int(self._tempDial)
        print(diff)
        for i in range(abs(diff)):
            if diff < 0:
                self.minusTemp(True)
            elif diff > 0:
                self.plusTemp(True)
            else:
                break

    def changeTempColor(self):
        self.tempDial.changeColor(self.tempDial.value())
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
        self.serialWriterThread.clearQueues()
        _fan = self.fanDial.value()
        diff = int(_fan) - int(self._fanDial)
        for i in range(abs(diff)):
            if diff < 0:
                self.minusFan()
            elif diff > 0:
                self.plusFan()
            else:
                break
    def changeFanColor(self):
        self.fanDial.changeColor(self.fanDial.value())
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