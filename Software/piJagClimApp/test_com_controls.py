# Importing Libraries
import serial
import serial.tools.list_ports
import time
comPorts = serial.tools.list_ports.comports()
nameList = list(port.device for port in comPorts)
print(nameList)
arduino = serial.Serial(port=nameList[0], baudrate=115200, timeout=.1)

def get_diff(hex_list, last_hex_list):
    if len(last_hex_list) == 0:
        return None
    res = []
    for i in range(len(hex_list)):
        if hex_list[i] != last_hex_list[i]:
            res.append([i, hex_list[i], last_hex_list[i]])
    return res
def bit_detect_2(_hex,n, bits_on_lst=[]):
    if len(bits_on_lst) != 0:
        for bit in bits_on_lst:
            _hex = str((hex(int(_hex, 16) - 2**bit)))[2:]
            if len(_hex) == 1:
                _hex = '0'+_hex
    if n==2:
        return _hex[1] == '4'
    elif n==3:
        return _hex[1] == '8'
    elif n==7:
        return _hex[0] == '8'
    else:
        return False
def bit_detect(_hex,n):
    return format(int(_hex, 16), '0>42b')[n] == '1'

def fan(value):
    fans = {"00-a0":"1", "00-e0":"2", "00-f0":"3", "01-f0": "4", "05-f0": "5", "07-f0": "6",
            "0f-f0":"7", "8f-f0":"8", "af-f0": "9","ef-f0":"10", "ff-f0":"11"}
    val = value[17] + "-" + value[18]
    try:
        fan_val = fans[val]
    except Exception as e:
        fan_val = "Can't read"
        print(str(e))
    return fan_val
def temp(value):
    temps = {"setpoints":{"00-00":"","b0-1b": ".0", "e0-1d":".5"},
             "units":{"b0-13":"0", "30-00":"1", "d0-16":"2", "f0-14": "3", "70-05": "4", "e0-15": "5", "e0-17":"6", "30-11":"7", "f0-17": "8","70-15":"9"},
             "tens":{"30": "1", "d0": "2", "f0": "3", "70": "H", "80": "L"}
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
    elif str(x) == "facefeet":
        arduino.write(b'\x07')
    elif str(x) == "feet":
        arduino.write(b'\x08')
    elif str(x) == "frontfeet":
        arduino.write(b'\x09')
    elif str(x) == "ac":
        arduino.write(b'\x0a')
    elif str(x) == "rear":
        arduino.write(b'\x0b')
    elif str(x) == "recycle":
        arduino.write(b'\x0c')
    elif str(x) == "upfan":
        arduino.write(b'\x0d')
    elif str(x) == "downfan":
        arduino.write(b'\x0e')

    time.sleep(0.35)
    numBytes = arduino.inWaiting()
    #print(numBytes)
    if numBytes > 0:
        for i in range(numBytes):
            data.append(arduino.read().hex())
    return data
last_value = []
while True:
    num = input("Enter command: ") # Taking input from user
    now = time.time()
    value = write_read(num)
    """
    diffs = get_diff(value[5:], last_value[5:])
    if diffs is not None:
        for diff in diffs:
            print(diff)
    last_value = value
    """
    if len(value)>18:
        #print(value)
        print("Temperature : ", temp(value))
        print("Auto : ", bit_detect_2(value[10], 2))
        print("LittleMan : ", bit_detect_2(value[9], 7))
        print("Face Arrow : ", bit_detect_2(value[7], 3))
        print("Feet Arrow : ", bit_detect_2(value[9], 3))
        print("Feet defrost : ", bit_detect_2(value[7], 7))
        if not bit_detect_2(value[16], 2, [1]):
            print("Fan : ", fan(value))
        else:
            print("Fan : False")
    print(time.time() - now)