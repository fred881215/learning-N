import serial
import time

lora = serial.Serial("/dev/ttyUSB0", 57600)

lora.write(b'radio set bw 500\r\n')
lora.readline()
lora.write(b'radio set sf sf11\r\n')
lora.readline()
lora.write(b'radio set freq 868100000\r\n')
lora.readline()

while True:
    lora.write(b'mac pause\r\n')
    lora.readline()

    t = int(time.time())
    byte_cmd = bytes('radio tx ' + str(t) + '\r\n')
    lora.write(byte_cmd)
    lora.readline()
    lora.readline()