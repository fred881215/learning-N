import paho.mqtt.client as mqtt
import json
import pymongo

client_mongo = pymongo.MongoClient(host='localhost', port=27017)

db = client_mongo.dht11

collection = db.dht

def on_connect(client, userdata, flags, rc):
    client.subscribe("Sensor/DHT22")
def on_message(client, userdata, msg):
    data = json.loads(str(msg.payload.decode('ascii')))
    result = collection.insert_one(data)
    print(data)
    result()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("127.0.0.1", 1883)
client.loop_forever()