import serial
import time

lora = serial.Serial("/dev/ttyUSB0", 57600, timeout = 1)

lora.write(b'radio cw off\r\n')
lora.readline()
lora.write(b'radio set bw 500\r\n')
lora.readline()
lora.write(b'radio set sf sf11\r\n')
lora.readline()
lora.write(b'radio set freq 868100000\r\n')
lora.readline()
lora.write(b'mac pause\r\n')
lora.readline()

while True:
    lora.write(b'radio rx 0\r\n')

    if lora.readline().strip() == "ok" or "radio_tx_ok" :
        print( str(lora.readline().strip()) )