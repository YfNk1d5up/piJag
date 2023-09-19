



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

def temp2tempDial(_temp):
    try:
        if len(_temp) < 3:
            if _temp[0] == 'H':
                dial = 30
            else:
                dial = 0
        else:
            dial = int((float(_temp) - 16) * 2)
        return dial
    except ValueError:
        return 15
    except IndexError:
        return 15

def tempDial2temp(_tempDial):
    try:
        if _tempDial == 0:
            return 'LO'
        elif _tempDial == 30:
            return 'HI'
        else:
            return str(23.5 + (_tempDial - 15) / 2)
    except ValueError:
        return '25.5'
    except IndexError:
        return '25.5'

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