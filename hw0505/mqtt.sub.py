import paho.mqtt.client as mqtt
import pymysql 
import time

connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='bydu',
                             password='000000',
                             db='my_db',
                             charset='utf8')

cursor = connection.cursor()

# 連線設定
# 初始化地端程式
client = mqtt.Client()

# 設定連線資訊(IP, Port, 連線時間)
client.connect("127.0.0.1", 1883, 60)

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sqlc = """CREATE TABLE `EMPLOYEE`(
        `NAME` CHAR(20) NOT NULL,
        `AGE` INT(10),
        )ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

sqli = """INSERT INTO EMPLOYEE('NAME','AGE') VALUES (%s, %d);"""

# 當地端程式連線伺服器得到回應時，要做的動作
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    cursor.execute(sqlc)
    client.subscribe("imac/iot")

# 當接收到從伺服器發送的訊息時要進行的動作
def on_message(client, userdata, msg):
    try:
        print(msg.topic+" "+ msg.payload.decode('utf-8'))
        data = cursor.fetchone()
        cursor.execute(sqli,msg)
        time.sleep(1)
    except:
        connection.rollback()

# 設定連線的動作
client.on_connect = on_connect
# 設定接收訊息的動作
client.on_message = on_message

connection.commit()

# 開始連線，執行設定的動作和處理重新連線問題
# 也可以手動使用其他loop函式來進行連接
client.loop_forever()

connection.close()