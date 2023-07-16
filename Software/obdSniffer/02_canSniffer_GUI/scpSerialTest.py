import time
import serial


obdReader = serial.Serial("/dev/ttyUSB0",  38400)
try:
    buf = bytearray()
    time.sleep(0.5)
    obdReader.write(b'ATZ\r')
    time.sleep(0.5)
    obdReader.write(b'ATL1\r')
    time.sleep(0.5)
    obdReader.write(b'ATH1\r')
    time.sleep(0.5)
    obdReader.write(b'ATS1\r')
    time.sleep(0.5)
    obdReader.write(b'ATAL\r')
    time.sleep(0.5)
    obdReader.write(b'ATSP6\r')
    time.sleep(0.5)
    obdReader.write(b'ATMA\r')
    while True:
        # Because of the high transmission speed, we shouldn't assume that the internal serial buffer
        # will only contain one package at a time, so I split that buffer by end line characters.
        i = buf.find(b"\n")
        if i >= 0:
            r = buf[:i + 1]
            buf = buf[i + 1:]
            # print(r.decode("utf-8"))
            try:
                decodedData = r.decode("utf-8")
                print(f'decoded data : {decodedData}')
            except UnicodeDecodeError as e:
                print(f'decoding error : {e}')
        try:
            incomingBytesNum = max(1, min(2048, obdReader.in_waiting))
            data = obdReader.read(incomingBytesNum)
        except serial.SerialException as e:
            print(e)
            pass
        else:
            if len(data):
                buf.extend(data)
        time.sleep(0.1)
finally:
    obdReader.close()