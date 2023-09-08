
from utils.utils import temp, fan

class arduinoSimul():
    def __init__(self):
        self.values = ['01' ,'c8' ,'00' ,'00' ,'00' ,'00' ,'00' ,'00' ,'88' ,'00' ,'00' ,'e0' ,'1d' ,'e0' ,'17' ,'d0'
                       ,'00', 'af' ,'f0' ,'00']
        self.dict_temps = {"setpoints": {"": "00-00", ".0": "b0-1b", ".5": "e0-1d"},
                           "units": {"0": "b0-13" ,"1": "30-00", "2": "d0-16", "3": "f0-14", "4": "70-05", "5": "e0-15",
                                     "6": "e0-17", "7": "30-11", "8": "f0-17", "9": "70-15"},
                           "tens": {"1": "30", "2": "d0", "3": "f0", "H": "70", "L": "80"}
                           }
        self.dict_fans = {'1': "00-a0", '2': "00-e0", '3': "00-f0", '4': "01-f0", '5': "05-f0", '6': "07-f0",
                          '7': "0f-f0", '8': "8f-f0", '9': "af-f0", '10': "ef-f0", '11': "ff-f0"}
        self.on = True
        self.i = 0
    def write(self, x):
        if x == b'\x01': # ONOFF
            if self.on == True:
                self.values[13] = '00'
            else:
                self.values[13] = 'e0'
            self.on = not self.on

        elif x == b'\x02': # minus
            _temp = temp(self.values)
            if len(_temp) < 3:
                if _temp[0] == 'H':
                    _temp = '31.0'
                else:
                    _temp = '16.0'
            try:
                new_temp = float(_temp ) -0.5
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


        elif x == b'\x03': # plus
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

        elif x == b'\x04': # auto
            self.values[10] = '84'

        elif x == b'\x05': # front defrost
            self.values[10] = '80'
            self.values[9] = '00'
            self.values[7] = '80'

        elif x == b'\x06': # face
            self.values[10] = '80'
            self.values[9] = '80'
            self.values[7] = '08'

        elif x == b'\x07': # face & feet
            self.values[10] = '80'
            self.values[9] = '88'
            self.values[7] = '08'

        elif x == b'\x08': # feet
            self.values[10] = '80'
            self.values[9] = '88'
            self.values[7] = '00'

        elif x == b'\x09': # front defrost & feet
            self.values[10] = '80'
            self.values[9] = '80'
            self.values[7] = '88'

        elif x == b'\x0a': # A / C
            pass

        elif x == b'\x0b': # rear defrost
            pass

        elif x == b'\x0c': # Recycle
            pass

        elif x == b'\x0d': # up Fan
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

        elif x == b'\x0e': # down Fan
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
        elif x == b'\x10': # down Fan
            pass

        return x

    def inWaiting(self):
        return 20

    def read(self):
        _readObj = readObject(self.values[self.i])
        self.i += 1
        if self.i > 19:
            self.i = 0
        return _readObj


class readObject():
    def __init__(self, x):
        self.x = x

    def hex(self):
        return self.x