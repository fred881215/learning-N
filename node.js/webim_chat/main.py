from flask import Flask, request, render_template, redirect, url_for, abort, jsonify
from flask_socketio import SocketIO, emit
from werkzeug.utils import secure_filename
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO()
socketio.init_app(app)

name_space = '/chat'
back_wait = False
# 依Server端設置
File_path = '/home/nick/git_project/learning-N/node.js/webim_fb/db/file_share/'

# 發送訊息
@app.route('/sendmsg', methods=['POST'])
def sendmsg():
    # 前端 talkroom.html 送出按鈕的指向，用 socketio 回傳訊息的同時對 chat_guid 的會員發送訊息，並把對話紀錄存到 msg.json 。
    if not request.json:
        return abort(400)
    else:
        try:
            time = request.json['time']
            message = request.json['message']
            guid = request.json['guid']
            chat_guid = request.json['chat_guid']
            topic = 'pub' + str(guid)
            # 1.己方右側回傳
            socketio.emit(topic, message, broadcast=True, namespace=name_space)
            # 2.對方左側傳送
            socketio.emit(chat_guid, message, broadcast=True, namespace=name_space)
        except:
            return abort(400)
        else:
            # 過濾訪客 test ，會員聊天訊息存到 msg.json (歷史紀錄)。
            if guid != 0:
                with open('/home/nick/git_project/learning-N/node.js/webim_fb/db/msg.json', 'a') as f:
                    json.dump(request.json, f)
                    f.write("\n")
                    f.close
        return jsonify({'status': 'ok'})

# 上傳檔案
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    f = request.files['file']
    f.save(File_path + "SHARE:" + f.filename)
    return jsonify({'status': 'ok'})

# 後端 socket 連線提示
@socketio.on('connect', namespace=name_space)
def connected_msg():
    print('client connected!')
@socketio.on('disconnect', namespace=name_space)
def disconnect_msg():
    print('client disconnected!')

# 登入頁面
@app.route('/')
def index():
    return render_template('login.html')

# 連資料庫的函式
def Contact_person():
    # 抓所有聯絡人。
    persons = []
    f = open('/home/nick/git_project/learning-N/node.js/webim_fb/db/guid.json', 'r')
    for line in f.readlines():
        data = json.loads(line)
        person = {"phone":data["Phone"], "guid":data["Guid"]}
        persons.append(person)
    f.close
    return persons

# 跳轉 Home.html
@app.route('/string/CustMsgService/main')
def mainpage():
    global back_wait
    # 登入時用 Contact_person() 拉全部聯絡人。
    persons = Contact_person()
    if back_wait:
        # 前端 talkroom.html 上一頁按鈕的 <window.location.href> ,back API執行完之後覆蓋全域變數，重新渲染 Home.html 。
        f = open('/home/nick/git_project/learning-N/node.js/webim_fb/db/guid.json', 'r')
        for line in f.readlines():
            inf = json.loads(line)
            if guid_jump == inf["Guid"]:
                phone = inf["Phone"]
        f.close
        back_wait = False
        return render_template('Home.html', phone=phone, guid=guid_jump, persons=persons)
    return render_template('Home.html', phone=phone_jump, guid=guid_jump, persons=persons)

# 跳轉 talkroom.html ，分 POST 和 GET 兩部份。
@app.route('/string/CustMsgService/GetMsg', methods=['POST'])
def GetMsg_POST():
    # 前端傳送POST請求，拉雙方資料存到全域變數，和下方GET函式結合。
    global chat_jump_phone
    global chat_jump_guid
    data = request.json
    f = open('/home/nick/git_project/learning-N/node.js/webim_fb/db/guid.json', 'r')
    for line in f.readlines():
        inf = json.loads(line)
        # 找對方資料
        if str(data["person"]) == inf["Guid"]:
            chat_jump_phone = inf["Phone"]
            chat_jump_guid = inf["Guid"]
        # 找自己資料
        if str(data["guid"]) == inf["Guid"]:
            phone_jump = inf["Phone"]
            guid_jump = inf["Guid"]
    f.close
    return jsonify({'status': 'ok'})

@app.route('/string/CustMsgService/GetMsg')
def GetMsg_GET():
    # 前端 Home.html <window.location.href> 的跳轉，跳到聊天室。
    send_guid = []
    msg = []
    time = []
    if guid_jump != 0:
        # 拉歷史紀錄
        f = open('/home/nick/git_project/learning-N/node.js/webim_fb/db/msg.json', 'r')
        for line in f.readlines():
            inf = json.loads(line)
            if (guid_jump == str(inf["guid"]) and chat_jump_guid == str(inf["chat_guid"])) | (guid_jump == str(inf["chat_guid"]) and chat_jump_guid == str(inf["guid"])):
                send_guid.append(inf["guid"])
                msg.append(inf["message"])
                time.append(inf["time"])
        f.close
    return render_template('talkroom.html', msg=msg, time=time, send_guid=send_guid, chat_name=chat_jump_phone, chat_guid=chat_jump_guid, phone=phone_jump, guid=guid_jump)

# 登入 API
@app.route('/string/CustMsgService/ValidByAdapter', methods=['POST'])
def login():
    global phone_jump
    global passwd_jump
    global guid_jump
    global chat_jump_phone
    global chat_jump_guid
    data = request.json
    Phone = data["Phone"]
    Password = data["Password"]
    account_type = data["account_type"]
    accept = False
    if account_type == 'member':
        # 登入會員
        f = open('/home/nick/git_project/learning-N/node.js/webim_fb/db/guid.json', 'r')
        for line in f.readlines():
            inf = json.loads(line)
            # 1.比對帳號密碼，如果比對成功 accept 為 True ，抓會員的 guid 存到全域變數。
            if Phone == inf["Phone"] and Password == inf["Password"]:
                accept = True
                guid_jump = inf["Guid"]
        # 2.比對失敗則回傳錯誤碼
        if accept == False:
            return abort(400)
        f.close
        phone_jump = Phone
        passwd_jump = Password
    else:
        # 訪客進 test 環境。
        guid_jump = 0
        chat_jump_phone = 'test'
        chat_jump_guid = 1
        phone_jump = Phone
        passwd_jump = Password
    return jsonify({'status': 'ok'})

# 登出 API
@app.route('/string/CustMsgService/Logout', methods=['POST'])
def logout():
    return jsonify({'status': 'ok'})

# 上一頁 API
@app.route('/string/CustMsgService/Back', methods=['POST'])
def back():
    # 接前端上一頁按鈕
    data = request.json
    # 跳回條件(全域)
    back_wait = True
    # 抓回前端guid
    guid_jump = data["guid"]
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    socketio.run(app)
    # app.debug = True
    # app.run()