from flask import Flask, request
from pymongo import MongoClient
from subprocess import Popen, PIPE
import configparser
import datetime
import time
import json
import sys
import ossaudiodev

config = configparser.ConfigParser()
config.read('config.ini')

myMongoClient = MongoClient(config['MONGODB']['URL'])
myMongoDb = myMongoClient["smart-data-center"]

# 攝影功能
dbCameraControl = myMongoDb['cameraControl']
dbCameraCreate = myMongoDb['cameraCreate']

def main():
    # 新增攝像機功能
    def func_CameraCreate():
        create_page = dbCameraCreate.find_one()
        if create_page["status"] == "1":
            Ping_result = Popen(["nc -v " + create_page["ip"] + " " + create_page["port"]], stdin=PIPE, stdout=PIPE, shell=True).communicate(input=b'\n')
            print(Ping_result)
            if str(Ping_result) == "(b'', None)":
                respText = "該位址無法連通～"
                # 回傳給用戶端

            else:
                respText = "該位址可以連通～"
                count_list = len([i for i in dbCameraControl.find()])
                # dbCameraControl.update_one({"device_number":str(count_list+1)}, {"$set":{"status":"0", "device_name":create_page["name"], "device_location":create_page["location"], "device_ip":create_page["ip"], "device_port":create_page["port"], "video_second":"", "chat_id":"", "connection":"0"}}, upsert=True)
            print(respText)
            # dbCameraCreate.update_one({"feature":"datapost"}, {"$set":{"status":"0", "name":"", "location":"", "ip":"", "port":"", "chat_id":""}}, upsert=True)
    # 攝像機請求檢測
    def func_CameraControl():
        all_camera = dbCameraControl.find()
        for camera in all_camera:
            if camera["status"] == "1" or camera["status"] == "2":
                respText = ""
                bot.send_message(chat_id=camera["chat_id"], text=respText, parse_mode="Markdown")
    func_CameraCreate()
main()
