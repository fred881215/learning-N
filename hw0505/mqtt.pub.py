import paho.mqtt.client as mqtt
import json
import time  
import serial
 
COM_PORT = '/dev/ttyUSB0'    # 指定通訊埠名稱
BAUD_RATES = 9600    # 設定傳輸速率
ser = serial.Serial(COM_PORT, BAUD_RATES)   # 初始化序列通訊埠

# 連線設定
# 初始化地端程式
client = mqtt.Client()

# # 設定連線資訊(IP, Port, 連線時間)
client.connect("127.0.0.1", 1883, 60)

try:
    while True:
        while ser.in_waiting:          # 若收到序列資料…
            data_raw = ser.readline()  # 讀取一行
            data = data_raw.decode()   # 用預設的UTF-8解碼
            print('接收到的原始資料：', data_raw)
            print('接收到的資料：', data)
            client.publish("imac/iot", data)
            time.sleep(5)
            
except KeyboardInterrupt:
    ser.close()    # 清除序列通訊物件