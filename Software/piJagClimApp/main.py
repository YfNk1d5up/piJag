# Importing Libraries
import serial
import serial.tools.list_ports
import time
comPorts = serial.tools.list_ports.comports()
nameList = list(port.device for port in comPorts)
print(nameList)
arduino = serial.Serial(port=nameList[0], baudrate=115200, timeout=.1)
def write_read(x):
    data = []
    if int(x) == 1:
        arduino.write(b'\x01')
    if int(x) == 2:
        arduino.write(b'\x02')
    if int(x) == 3:
        arduino.write(b'\x03')
    time.sleep(0.05)
    numBytes = arduino.inWaiting()
    print(numBytes)
    if numBytes > 0:
        for i in range(numBytes):
            data.append(arduino.read())
    return data
while True:
    num = input("Enter 1 to start: ") # Taking input from user
    value = write_read(num)
    print(value) # printing the value
