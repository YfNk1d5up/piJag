from PyQt5.QtCore import QThread, pyqtSignal
import serial
import time


class SerialReaderThread(QThread):
    receivedPacketSignal = pyqtSignal(str, float)
    buf = bytearray()

    def __init__(self, serial=None, protocol='CAN'):
        super(SerialReaderThread, self).__init__()
        self.serial = serial
        self.protocol = protocol
        self.isRunning = False

    def stop(self):
        self.isRunning = False

    def changeProtocol(self, protocol):
        self.protocol = protocol

    def run(self):
        self.isRunning = True
        """
        Already in main : startSniffing
        if self.protocol == 'SCP':
            # reset OBD II UART
            self.serial.write(b'ATZ\r')
            time.sleep(0.5)
            # set Line Feed Mode
            self.serial.write(b'ATL1\r')
            time.sleep(0.5)
            # set message headers ON
            self.serial.write(b'ATH1\r')
            time.sleep(0.5)
            # set spaces between bytes to ON
            self.serial.write(b'ATS1\r')
            time.sleep(0.5)
            # allow messages that are longer than 7 bytes
            self.serial.write(b'ATAL\r')
            time.sleep(0.5)
            # set protocol to SAE J1850 PWM (41.6 kbaud)
            self.serial.write(b'ATSP1\r')
            time.sleep(0.5)
            # read All message
            self.serial.write(b'ATMA\r')
        """
        while self.isRunning:
            # Because of the high transmission speed, we shouldn't assume that the internal serial buffer
            # will only contain one package at a time, so I split that buffer by end line characters.
            i = self.buf.find(b"\n")
            if i >= 0:
                r = self.buf[:i + 1]
                self.buf = self.buf[i + 1:]
                # print(r.decode("utf-8"))
                try:
                    decodedData = r.decode("utf-8")
                    if self.protocol == 'SCP':
                        #print(decodedData)
                        # Reorder to unify results on Gui
                        # SCP consists in :
                        # PP RR TT DD DD DD DD DD DD DD CC - where PP = priority, RR = receiver ID, TT = transmitter ID, DD = data, CC = checksum.
                        decodedData = decodedData[3:5] + ',' + decodedData[6:8] + ',' + decodedData[0:2] + ',' + \
                                      decodedData[9:-2].replace(' ', '') + 'e'  # add end char to unify decoding in main
                    self.receivedPacketSignal.emit(decodedData, time.time())
                except UnicodeDecodeError as e:
                    print(e)
            try:
                incomingBytesNum = max(1, min(2048, self.serial.in_waiting))
                data = self.serial.read(incomingBytesNum)
            except serial.SerialException as e:
                print(e)
                pass
                # There is no new data from serial port
            except TypeError as e:
                # Disconnect of USB->UART occured
                print("Serial disconnected")
                print(e)
                self.serial.close()
            except OSError as e:
                # Disconnect of USB->UART occured
                print("Serial disconnected")
                print(e)
                self.serial.close()
            else:
                if len(data):
                    self.buf.extend(data)
        self.msleep(100)
