import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

import piJagClimv1_ui
from utils import arduinoSimul, temp, fan, air, bit_detect_2
import serial
import serial.tools.list_ports
import time


class piJagClimateGUI(QMainWindow, piJagClimv1_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.simul = False
        self.comPorts = serial.tools.list_ports.comports()
        self.nameList = list(port.device for port in self.comPorts)
        if len(self.nameList) > 0:
            self.arduino = serial.Serial(port=self.nameList[0], baudrate=115200, timeout=.1)
            self.simul = False
        else:
            self.arduino = arduinoSimul()
            self.simul = True



        # Temperature

        self.tempDial.setValue(21)
        self.tempDial.changeColor(255,255,0,127)
        self.tempValueLabel.setText("26.5")
        self.temp = self.tempDial.value()

        self.tempDial.valueChanged.connect(self.changeTemp)
        self.tempPlusButton.clicked.connect(self.plusTemp)
        self.tempMinusButton.clicked.connect(self.minusTemp)
        self.tempAutoButton.clicked.connect(self.autoTemp)
        self.tempACButton.clicked.connect(self.tempAC)

        # Fan

        self.fanDial.setValue(9)
        self.fanValueLabel.setText("9")
        self.fan = self.fanDial.value()

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


    # Temperature
    def plusTemp(self, fromChange = False):
        _temp = temp(self.write_read(b'\x03'))
        self.tempValueLabel.setText(_temp)
        if not fromChange:
            if len(_temp)<3:
                if _temp[0]=='H':
                    self.temp = 31
                else:
                    self.temp = 1
            else:
                self.temp = int((float(_temp) - 16) * 2) + 1
            self.tempDial.setValue(self.temp)
    def minusTemp(self, fromChange = False):
        _temp = temp(self.write_read(b'\x02'))
        self.tempValueLabel.setText(_temp)
        if not fromChange:
            if len(_temp) < 3:
                if _temp[0] == 'H':
                    self.temp = 31
                else:
                    self.temp = 1
            else:
                self.temp = int((float(_temp) - 16) * 2) + 1
            self.tempDial.setValue(self.temp)
    def changeTemp(self):
        _temp = self.tempDial.value()
        diff = int(_temp) - int(self.temp)
        for i in range(abs(diff)):
            if diff < 0:
                self.minusTemp(True)
            else:
                self.plusTemp(True)
        self.temp = _temp
    def autoTemp(self):
        self.tempValueLabel.setText(temp(self.write_read("?")))
    def tempAC(self):
        self.airValueLabel.setText(air(self.write_read(b'\x0a')))

    # Fan
    def plusFan(self, fromChange = False):
        _fan = fan(self.write_read(b'\x0d'))
        self.fanValueLabel.setText(_fan)
        self.fan = int(_fan)
        if not fromChange:
            self.fanDial.setValue(int(_fan))
    def minusFan(self, fromChange = False):
        _fan = fan(self.write_read(b'\x0e'))
        self.fanValueLabel.setText(_fan)
        self.fan = int(_fan)
        if not fromChange:
            self.fanDial.setValue(int(_fan))
    def changeFan(self):
        _fan = self.fanDial.value()
        diff = int(_fan) - int(self.fan)
        for i in range(abs(diff)):
            if diff < 0:
                self.minusFan()
            else:
                self.plusFan()
        self.fan = _fan
    def autoFan(self):
        self.fanValueLabel.setText(fan(self.write_read(b'\x04')))

    def airFace(self):
        values = self.write_read(b'\x06')
        self.airValueLabel.setText(air(values))
        self.fanValueLabel.setText(fan(values))
    def airFeet(self):
        values = self.write_read(b'\x08')
        self.airValueLabel.setText(air(values))
        self.fanValueLabel.setText(fan(values))
    def airFeetFace(self):
        values = self.write_read(b'\x07')
        self.airValueLabel.setText(air(values))
        self.fanValueLabel.setText(fan(values))
    def airFront(self):
        values = self.write_read(b'\x05')
        self.airValueLabel.setText(air(values))
        self.fanValueLabel.setText(fan(values))
    def airRear(self):
        values = self.write_read(b'\x0b')
        self.airValueLabel.setText(air(values))
        self.fanValueLabel.setText(fan(values))
    def airRecycle(self):
        values = self.write_read(b'\x0c')
        self.airValueLabel.setText(air(values))
        self.fanValueLabel.setText(fan(values))


    def write_read(self, x):

        data = []
        self.arduino.write(x)
        if not self.simul:
            time.sleep(0.35)
        numBytes = self.arduino.inWaiting()
        # print(numBytes)
        if numBytes > 0:
            for i in range(numBytes):
                data.append(self.arduino.read().hex())
        return data


def main():
    app = QApplication(sys.argv)
    gui = piJagClimateGUI()

    gui.show()
    app.setStyle('Fusion')
    app.exec_()

if __name__ == '__main__':
    main()