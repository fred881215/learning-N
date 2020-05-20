import paho.mqtt.client as mqtt
import json
def on_connect(client, userdata, flags, rc):
    client.subscribe("Sensor/DHT22")
def on_message(client, userdata, msg):
    data = json.loads(str(msg.payload.decode('ascii')))
    print(data)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.157", 1883)
client.loop_forever()