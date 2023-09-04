# Importing Libraries
import serial
import serial.tools.list_ports
import time
comPorts = serial.tools.list_ports.comports()
nameList = list(port.device for port in comPorts)
print(nameList)
arduino = serial.Serial(port=nameList[0], baudrate=115200, timeout=.1)


def temp(value):
    temps = {"setpoints":{"00-00":"","b0-1b": ".0", "e0-1d":".5"},
             "units":{"b0-13":"0", "30-00":"1", "d0-16":"2", "f0-14": "3", "70-05": "4", "e0-15": "5", "e0-17":"6", "30-11":"7", "f0-17": "8","70-15":"9"},
             "tens":{"30": "1", "d0": "2", "f0": "3", "70": "H", "80": "L"}
             }
    setpoint = str(value[11].hex()) + "-" + str(value[12].hex())
    unit = str(value[13].hex()) + "-" + str(value[14].hex())
    ten = str(value[15].hex())
    try:
        if temps["tens"][ten] == "H":
            return "HI"
        elif temps["tens"][ten] == "L":
            return "LO"
        else:
            temperature = temps["tens"][ten]+temps["units"][unit]+temps["setpoints"][setpoint]
    except:
        temperature = "Can't read"
    return temperature
def write_read(x):
    data = []
    if str(x) == "on":
        arduino.write(b'\x01')
    elif str(x) == "-":
        arduino.write(b'\x02')
    elif str(x) == "+":
        arduino.write(b'\x03')
    elif str(x) == "auto":
        arduino.write(b'\x04')
    elif str(x) == "front":
        arduino.write(b'\x05')
    elif str(x) == "face":
        arduino.write(b'\x06')
    time.sleep(0.3)
    numBytes = arduino.inWaiting()
    #print(numBytes)
    if numBytes > 0:
        for i in range(numBytes):
            data.append(arduino.read())
    return data
while True:
    num = input("Enter 1 to start: ") # Taking input from user
    value = write_read(num)
    if len(value)>18:
        #print(value)
        #print("Auto" , bin(int(str(value[7].hex())))) # printing the value
        print("Temperature : ", temp(value))