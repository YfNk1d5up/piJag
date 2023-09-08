import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

import piJagClimv1_ui
from utils.arduinoReader import SerialReaderThread
from utils.arduinoWriter import SerialWriterThread
from utils.ArduinoSimul import arduinoSimul
from utils.utils import temp, fan, air, temp2tempDial
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
        self._color = {'r': 0, 'g': 0, 'b': 0, 'a': 255}
        self._rear = False
        # Dial default values
        self._tempDial = 15
        self._fanDial = 5

        # "on" default value
        self._on = True

        # OnOff
        self.onoffButton.clicked.connect(self.onoff)

        # Temperature
        self.tempDial.sliderReleased.connect(self.changeTemp)
        self.tempDial.valueChanged.connect(self.changeTempColor)
        self.tempPlusButton.clicked.connect(self.plusTemp)
        self.tempMinusButton.clicked.connect(self.minusTemp)
        self.tempAutoButton.clicked.connect(self.autoTemp)
        self.tempACButton.clicked.connect(self.tempAC)
        self.tempDial.setEnabled(False)
        self.tempPlusButton.setEnabled(False)
        self.tempMinusButton.setEnabled(False)
        self.tempAutoButton.setEnabled(False)
        self.tempACButton.setEnabled(False)

        # Fan
        self.fanDial.sliderReleased.connect(self.changeFan)
        self.fanDial.valueChanged.connect(self.changeFanColor)
        self.fanMinusButton.clicked.connect(self.minusFan)
        self.fanPlusButton.clicked.connect(self.plusFan)
        self.fanAutoButton.clicked.connect(self.autoFan)
        self.fanDial.setEnabled(False)
        self.fanMinusButton.setEnabled(False)
        self.fanPlusButton.setEnabled(False)
        self.fanAutoButton.setEnabled(False)

        # Controls
        self.airFaceButton.clicked.connect(self.airFace)
        self.airFeetButton.clicked.connect(self.airFeet)
        self.airFeetFaceButton.clicked.connect(self.airFeetFace)
        self.airFrontDefrostButton.clicked.connect(self.airFront)
        self.airFeetFrontDefrostButton.clicked.connect(self.airFeetFront)
        self.airRearDefrostButton.clicked.connect(self.airRear)
        self.airRecyclingButton.clicked.connect(self.airRecycle)
        self.airFaceButton.setEnabled(False)
        self.airFeetButton.setEnabled(False)
        self.airFeetFaceButton.setEnabled(False)
        self.airFrontDefrostButton.setEnabled(False)
        self.airFeetFrontDefrostButton.setEnabled(False)
        self.airRearDefrostButton.setEnabled(False)
        self.airRecyclingButton.setEnabled(False)

        self.list_air_buttons = [self.airFeetFaceButton,
                                 self.airFaceButton,
                                 self.airFeetButton,
                                 self.airFrontDefrostButton,
                                 self.airFeetFrontDefrostButton
                                 ]

        time.sleep(1.5) # Wait for threads to initialize
        self.write(b'\x10') # Ask for values

    def serialPacketReceiverCallback(self, packet):
        if packet[13] == '00':
            self._temp = ''
            self._fan = ''
            self._air = ''
            self._color = {'r': 0, 'g': 0, 'b': 0, 'a': 255}
            #self.onoffButton.setText('On')
            self._on = False
        else:
            self._temp = temp(packet)
            self._fan = fan(packet)
            self._air = air(packet)
            self._color = self.tempDial.getColor()
            self.onoffButton.select(self._color)
            #self.onoffButton.setText('Off')
            self._on = True
        self.tempDial.setVal(self._temp)
        self.updateButtonsBackground()

        self._tempDial = temp2tempDial(self._temp)
        self.tempDial.setValue(self._tempDial)
        self.tempDial.changeColor(self._tempDial)

        self.fanDial.setVal(self._fan)
        if self._fan != 'Auto':
            try:
                self._fanDial = int(self._fan)
                self.fanDial.setValue(self._fanDial)
            except:
                self.fanDial.setValue(6)
            self.fanDial.changeColor(self._fanDial)
        else:
            self.fanDial.animateCursor()

    def write(self, x):
        self.serialWriterThread.write(x)

    def onoff(self):
        self.write(b'\x01')

        if self._on:
            # Temperature
            self.tempDial.setEnabled(False)
            self.tempPlusButton.setEnabled(False)
            self.tempMinusButton.setEnabled(False)
            self.tempAutoButton.setEnabled(False)
            self.tempACButton.setEnabled(False)

            # Fan
            self.fanDial.setEnabled(False)
            self.fanMinusButton.setEnabled(False)
            self.fanPlusButton.setEnabled(False)
            self.fanAutoButton.setEnabled(False)

            # Controls
            self.airFaceButton.setEnabled(False)
            self.airFeetButton.setEnabled(False)
            self.airFeetFaceButton.setEnabled(False)
            self.airFrontDefrostButton.setEnabled(False)
            self.airFeetFrontDefrostButton.setEnabled(False)
            self.airRearDefrostButton.setEnabled(False)
            self.airRecyclingButton.setEnabled(False)

            self.onoffButton.deselect()

        else:
            # Temperature
            self.tempDial.setEnabled(True)
            self.tempPlusButton.setEnabled(True)
            self.tempMinusButton.setEnabled(True)
            self.tempAutoButton.setEnabled(True)
            self.tempACButton.setEnabled(True)

            # Fan
            self.fanDial.setEnabled(True)
            self.fanMinusButton.setEnabled(True)
            self.fanPlusButton.setEnabled(True)
            self.fanAutoButton.setEnabled(True)

            # Controls
            self.airFaceButton.setEnabled(True)
            self.airFeetButton.setEnabled(True)
            self.airFeetFaceButton.setEnabled(True)
            self.airFrontDefrostButton.setEnabled(True)
            self.airFeetFrontDefrostButton.setEnabled(True)
            self.airRearDefrostButton.setEnabled(True)
            self.airRecyclingButton.setEnabled(True)

            self.onoffButton.select(self.tempDial.getColor())

    # Temperature
    def plusTemp(self, fromChange = False):
        self.write(b'\x03')
    def minusTemp(self, fromChange = False):
        self.write(b'\x02')

    def changeTemp(self):
        self.serialWriterThread.clearQueues()
        _temp = self.tempDial.value()
        diff = int(_temp) - int(self._tempDial)
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
        #self.tempDial.animateCursor()
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
    def airFeetFront(self):
        self.write(b'\x09')
    def airRear(self):
        self.write(b'\x0b')
        if self._air == 'Front':
            self._rear = not self._rear
            if self._rear:
                self.updateButtonsBackground(self.airRearDefrostButton)
            else:
                self.updateButtonsBackground()
    def airRecycle(self):
        self.write(b'\x0c')

    def updateButtonsBackground(self, forced = None):
        colors = {'grey' : "background-color:rgb(180,180,180); border-radius: 50%;",
                  'white': "background-color:rgb(255,255,255); border-radius: 50%;"
                  }
        if forced == None:
            for button in self.list_air_buttons:
                button.deselect()
            if self._fan != 'Front':
                self._rear = False
                self.airRearDefrostButton.deselect()
            if not self._rear:
                self.airRearDefrostButton.deselect()
            if self._air == 'Face':
                self.airFaceButton.select(self._color)
            elif self._air == 'Feet':
                self.airFeetButton.select(self._color)
            elif self._air == 'Face&Feet':
                self.airFeetFaceButton.select(self._color)
            elif self._air == 'Front':
                self.airFrontDefrostButton.select(self._color)
            elif self._air == 'Feet&Front':
                self.airFeetFrontDefrostButton.select(self._color)
        else:
            forced.select(self._color)



def main():
    app = QApplication(sys.argv)
    gui = piJagClimateGUI()

    gui.show()
    app.setStyle('Fusion')
    app.exec_()

if __name__ == '__main__':
    main()