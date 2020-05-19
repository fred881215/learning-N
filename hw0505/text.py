import paho.mqtt.client as mqtt
import random
import json
import time  

# 連線設定
# 初始化地端程式
client = mqtt.Client()

# 設定連線資訊(IP, Port, 連線時間)
client.connect("192.168.1.149", 1883, 60)

while True:
    rdage = random.randint(0,30)
    payload = {'name' : 'nick' , 'age' : rdage}
    print (json.dumps(payload))
    #要發布的主題和內容
    client.publish("imac/iot", json.dumps(payload))
    time.sleep(5)