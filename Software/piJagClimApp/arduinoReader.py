from PyQt5.QtCore import QThread, pyqtSignal
import serial

class SerialReaderThread(QThread):
    receivedPacketSignal = pyqtSignal(list)
    buf = []

    def __init__(self, serial):
        super(SerialReaderThread, self).__init__()
        self.serial = serial
        self.isRunning = False

    def stop(self):
        self.isRunning = False

    def run(self):
        self.isRunning = True
        while self.isRunning:
            try:
                data = []
                numBytes = self.serial.inWaiting()
                if numBytes > 0:
                    for i in range(numBytes):
                        data.append(self.serial.read().hex())
                    if data != self.buf:
                        self.receivedPacketSignal.emit(data)
                        self.buf = data
            except serial.SerialException as e:
                print(e)
                pass
                # There is no new data from serial port
            except TypeError as e:
                # Disconnect of USB->UART occured
                #print("Serial disconnected")
                #print(e)
                #self.serial.close()
                pass
            except OSError as e:
                # Disconnect of USB->UART occured
                print("Serial disconnected")
                print(e)
                self.serial.close()
            else:
                pass
                #if len(data):
                #self.buf.extend(data)
        self.msleep(100)
