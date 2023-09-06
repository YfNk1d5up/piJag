

class readObject():
    def __init__(self, x):
        self.x = x

    def hex(self):
        return self.x

class arduinoSimul():
    def __init__(self):
        self.values = ['01','c8','00','00','00','00','00','00','88','00','00','e0','1d','e0','17','d0','00', 'af','f0','00']
        self.dict_temps = {"setpoints": {"": "00-00", ".0": "b0-1b", ".5": "e0-1d"},
                  "units": {"0": "b0-13","1": "30-00", "2": "d0-16", "3": "f0-14", "4": "70-05", "5": "e0-15",
                            "6": "e0-17", "7": "30-11", "8": "f0-17", "9": "70-15"},
                  "tens": {"1": "30", "2": "d0", "3": "f0", "H": "70", "L": "80"}
                  }
        self.dict_fans = {'1': "00-a0", '2': "00-e0", '3': "00-f0", '4': "01-f0", '5': "05-f0", '6': "07-f0",
            '7': "0f-f0", '8': "8f-f0", '9': "af-f0", '10': "ef-f0", '11': "ff-f0"}
        self.i = 0
    def write(self, x):
        match x:
            case b'\x01': # ONOFF
                pass
                
            case b'\x02': # minus
                _temp = temp(self.values)
                if len(_temp) < 3:
                    if _temp[0] == 'H':
                        _temp = '31.0'
                    else:
                        _temp = '16.0'
                try:
                    new_temp = float(_temp)-0.5
                    if new_temp > 16:
                        _temp = "{:.1f}".format(new_temp)
                        _tens = self.dict_temps['tens'][_temp[0]]
                        _units = self.dict_temps['units'][_temp[1]]
                        _setpoints = self.dict_temps['setpoints'][_temp[2:]]
                        self.values[15] = _tens
                        self.values[13] = _units.split('-')[0]
                        self.values[14] = _units.split('-')[1]
                        self.values[11] = _setpoints.split('-')[0]
                        self.values[12] = _setpoints.split('-')[1]
                    else:
                        self.values[15] = self.dict_temps['tens']['L']
                except Exception as e:
                    print(str(e))
                

            case b'\x03': # plus
                _temp = temp(self.values)
                if len(_temp) < 3:
                    if _temp[0] == 'H':
                        _temp = '31.0'
                    else:
                        _temp = '16.0'
                try:
                    new_temp = float(_temp) + 0.5
                    if new_temp < 31:
                        _temp = "{:.1f}".format(new_temp)
                        _tens = self.dict_temps['tens'][_temp[0]]
                        _units = self.dict_temps['units'][_temp[1]]
                        _setpoints = self.dict_temps['setpoints'][_temp[2:]]
                        self.values[15] = _tens
                        self.values[13] = _units.split('-')[0]
                        self.values[14] = _units.split('-')[1]
                        self.values[11] = _setpoints.split('-')[0]
                        self.values[12] = _setpoints.split('-')[1]
                    else:
                        self.values[15] = self.dict_temps['tens']['H']
                except Exception as e:
                    print(str(e))
                
            case b'\x04': # auto
                self.values[10] = '84'
                
            case b'\x05': # front defrost
                self.values[10] = '80'
                self.values[9] = '00'
                self.values[7] = '80'
                
            case b'\x06': # face
                self.values[10] = '80'
                self.values[9] = '80'
                self.values[7] = '08'
                
            case b'\x07': # face & feet
                self.values[10] = '80'
                self.values[9] = '88'
                self.values[7] = '08'
                
            case b'\x08': # feet
                self.values[10] = '80'
                self.values[9] = '88'
                self.values[7] = '00'
                
            case b'\x09': # front defrost & feet
                self.values[10] = '80'
                self.values[9] = '80'
                self.values[7] = '88'
                
            case b'\x0a': # A / C
                pass
                
            case b'\x0b': # rear defrost
                pass
                
            case b'\x0c': # Recycle
                pass
                
            case b'\x0d': # up Fan
                self.values[10] = '80'
                _fan = int(fan(self.values))
                try:
                    if _fan == 11:
                        _fan = 10
                    new_fan = _fan + 1
                    _fans = self.dict_fans[str(new_fan)]
                    self.values[17] = _fans.split('-')[0]
                    self.values[18] = _fans.split('-')[1]
                except Exception as e:
                    print(str(e))
                
            case b'\x0e': # down Fan
                self.values[10] = '80'
                _fan = int(fan(self.values))
                try:
                    if _fan == 1:
                        _fan = 2
                    new_fan = _fan - 1
                    _fans = self.dict_fans[str(new_fan)]
                    self.values[17] = _fans.split('-')[0]
                    self.values[18] = _fans.split('-')[1]
                except Exception as e:
                    print(str(e))
                
        return x

    def inWaiting(self):
        return 20

    def read(self):
        _readObj = readObject(self.values[self.i])
        self.i += 1
        if self.i > 19:
            self.i = 0
        return _readObj



temps = {"setpoints": {"00-00": "", "b0-1b": ".0", "e0-1d": ".5"},
             "units": {"b0-13": "0", "30-00": "1", "d0-16": "2", "f0-14": "3", "70-05": "4", "e0-15": "5",
                       "e0-17": "6", "30-11": "7", "f0-17": "8", "70-15": "9"},
             "tens": {"30": "1", "d0": "2", "f0": "3", "70": "H", "80": "L"}
             }

fans = {"00-a0": "1", "00-e0": "2", "00-f0": "3", "01-f0": "4", "05-f0": "5", "07-f0": "6",
            "0f-f0": "7", "8f-f0": "8", "af-f0": "9", "ef-f0": "10", "ff-f0": "11"}


def temp(value):
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

def fan(value):
    val = value[17] + "-" + value[18]
    auto = bit_detect_2(value[10], 2)
    try:
        if auto:
            fan_val = "Auto"
        else:
            fan_val = fans[val]
    except Exception as e:
        fan_val = "Can't read"
        print(str(e))
    return fan_val

def air(value):
    dict_air = {"LittleMan": bit_detect_2(value[9], 7),
    "Face": bit_detect_2(value[7], 3),
    "Feet": bit_detect_2(value[9], 3),
    "Front": bit_detect_2(value[7], 7)
     }
    if dict_air["LittleMan"] and dict_air["Face"] and dict_air["Feet"]:
        return "Face&Feet"
    elif dict_air["LittleMan"] and dict_air["Feet"] and dict_air["Front"]:
        return "Feet&Front"
    elif dict_air["LittleMan"] and dict_air["Face"]:
        return "Face"
    elif dict_air["LittleMan"] and dict_air["Feet"]:
        return "Feet"
    elif dict_air["Front"]:
        return "Front"
    return "Can't Read"

def bit_detect_2(_hex, n, bits_on_lst=[]):
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