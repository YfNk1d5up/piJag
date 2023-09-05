import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

import piJagClimv1_ui

import serial
import serial.tools.list_ports
import time


class piJagClimateGUI(QMainWindow, piJagClimv1_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comPorts = serial.tools.list_ports.comports()
        self.nameList = list(port.device for port in self.comPorts)
        self.arduino = serial.Serial(port=self.nameList[0], baudrate=115200, timeout=.1)
        
        self.tempPlusButton.clicked.connect(self.plusTemp)
        self.tempMinusButton.clicked.connect(self.minusTemp)



    def plusTemp(self):
        self.tempValueLabel.setText(self.temp(self.write_read("+")))
    def minusTemp(self):
        self.tempValueLabel.setText(self.temp(self.write_read("-")))

    def write_read(self, x):
        data = []
        if str(x) == "on":
            self.arduino.write(b'\x01')
        elif str(x) == "-":
            self.arduino.write(b'\x02')
        elif str(x) == "+":
            self.arduino.write(b'\x03')
        elif str(x) == "auto":
            self.arduino.write(b'\x04')
        elif str(x) == "front":
            self.arduino.write(b'\x05')
        elif str(x) == "face":
            self.arduino.write(b'\x06')
        elif str(x) == "facefeet":
            self.arduino.write(b'\x07')
        elif str(x) == "feet":
            self.arduino.write(b'\x08')
        elif str(x) == "frontfeet":
            self.arduino.write(b'\x09')
        elif str(x) == "ac":
            self.arduino.write(b'\x0a')
        elif str(x) == "rear":
            self.arduino.write(b'\x0b')
        elif str(x) == "recycle":
            self.arduino.write(b'\x0c')
        elif str(x) == "upfan":
            self.arduino.write(b'\x0d')
        elif str(x) == "downfan":
            self.arduino.write(b'\x0e')

        time.sleep(0.35)
        numBytes = self.arduino.inWaiting()
        # print(numBytes)
        if numBytes > 0:
            for i in range(numBytes):
                data.append(self.arduino.read().hex())
        return data

    def temp(self, value):
        temps = {"setpoints": {"00-00": "", "b0-1b": ".0", "e0-1d": ".5"},
                 "units": {"b0-13": "0", "30-00": "1", "d0-16": "2", "f0-14": "3", "70-05": "4", "e0-15": "5",
                           "e0-17": "6", "30-11": "7", "f0-17": "8", "70-15": "9"},
                 "tens": {"30": "1", "d0": "2", "f0": "3", "70": "H", "80": "L"}
                 }
        setpoint = value[11] + "-" + value[12]
        unit = value[13] + "-" + value[14]
        ten = value[15]
        try:
            if temps["tens"][ten] == "H":
                return "HI"
            elif temps["tens"][ten] == "L":
                return "LO"
            else:
                temperature = temps["tens"][ten] + temps["units"][unit] + temps["setpoints"][setpoint]
        except:
            temperature = "Can't read"
        return temperature

    def fan(self, value):
        fans = {"00-a0": "1", "00-e0": "2", "00-f0": "3", "01-f0": "4", "05-f0": "5", "07-f0": "6",
                "0f-f0": "7", "8f-f0": "8", "af-f0": "9", "ef-f0": "10", "ff-f0": "11"}
        val = value[17] + "-" + value[18]
        try:
            fan_val = fans[val]
        except Exception as e:
            fan_val = "Can't read"
            print(str(e))
        return fan_val

    def bit_detect_2(self, _hex, n, bits_on_lst=[]):
        if len(bits_on_lst) != 0:
            for bit in bits_on_lst:
                _hex = str((hex(int(_hex, 16) - 2 ** bit)))[2:]
                if len(_hex) == 1:
                    _hex = '0' + _hex
        if n == 2:
            return _hex[1] == '4'
        elif n == 3:
            return _hex[1] == '8'
        elif n == 7:
            return _hex[0] == '8'
        else:
            return False
def main():
    app = QApplication(sys.argv)
    gui = piJagClimateGUI()

    gui.show()
    app.exec_()

if __name__ == '__main__':
    main()