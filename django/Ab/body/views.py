from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib import auth
from .models import *
from datetime import date,datetime
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def object_to_json(obj): # 轉換函式
    print(obj.__dict__)
    print(type(obj))
    data = json.dumps(obj.__dict__, default=json_util.default)

    # data = json.dumps(obj, default=lambda o:o.__dict__, sort_keys=True, indent=4)
    print(data)
    data = json.loads(data)
    # data.pop('_state')
    # data.pop('id')
    # data.pop('uid')
    return data

@csrf_exempt
def blood_pressure(request): # 上傳血壓測量結果!
    uid = request.user.uid
    if request.method == 'POST':
        # uid = '1'
        nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        systolic = request.POST.get('systolic')
        diastolic = request.POST.get('diastolic')
        pulse = request.POST.get('pulse')
        # data = request.body
        # data = str(data, encoding="utf-8")
        # data = json.loads(data)
        # systolic = data['systolic']
        # diastolic = data['diastolic']
        # pulse = data['pulse']
        try:
            Blood_pressure.objects.create(uid=uid, systolic=systolic, diastolic=diastolic, pulse=pulse, recorded_at=nowtime)
        except:
            output = {"status":"1"}
        else:
            output = {"status":"0"}        
    return JsonResponse(output,safe=False)

@csrf_exempt
def body_weight(request): # 上傳體重測量結果!
    uid = request.user.uid
    # uid = '1'
    nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    weight = request.POST.get('weight')
    body_fat = request.POST.get('body_fat')
    bmi = request.POST.get('bmi')
    # data = request.body
    # data = str(data, encoding="utf-8")
    # data = json.loads(data)
    # weight = data['weight']
    # body_fat = data['body_fat']
    # bmi = data['bmi']
    try:
        Weight.objects.create(uid=uid, weight=weight, body_fat=body_fat, bmi=bmi, recorded_at=nowtime)
    except:
        output = {"status":"1"}
    else:
        output = {"status":"0"}        
    return JsonResponse(output,safe=False) 

@csrf_exempt
def blood_sugar(request): # 上傳血糖測量結果!
    uid = request.user.uid
    # uid = '1'
    nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sugar = request.POST.get('sugar')
    # data = request.body
    # data = str(data, encoding="utf-8")
    # data = json.loads(data)
    # sugar = data['sugar']
    timeperiod_list = ['晨起', '早餐前', '早餐後', '午餐前', '午餐後', '晚餐前', '晚餐後', '睡前']
    # timeperiod = timeperiod_list[(int(data['timeperiod'])-1)%8]
    timeperiod = timeperiod_list[(int(request.POST.get('timeperiod'))-1)%8]
    try:
        Blood_sugar.objects.create(uid=uid, sugar=sugar, timeperiod=timeperiod, recorded_at=nowtime)
    except:
        output = {"status":"1"}
    else:
        output = {"status":"0"}        
    return JsonResponse(output,safe=False)
            
@csrf_exempt
def last_upload(request): # 最後上傳時間!
    uid = request.user.uid
    # uid = '1'
    try:
        pre = Blood_pressure.objects.filter(uid=uid).latest('recorded_at')
        wei = Weight.objects.filter(uid=uid).latest('recorded_at')
        sug = Blood_sugar.objects.filter(uid=uid).latest('recorded_at')
    except:
        output = {"status":"1"}
    else:
        output = {
            "status":"0", 
            "last_upload":[
                {"blood_pressure":pre.recorded_at, "weight":wei.recorded_at, "blood_sugar":sug.recorded_at}
            ]
        }        
    return JsonResponse(output,safe=False)

@csrf_exempt
def records(request): # 上一筆紀錄資訊!
    # uid = request.user.uid
    uid = '1'
    try:
        pre = Blood_pressure.objects.filter(uid=uid).latest('recorded_at')
        wei = Weight.objects.filter(uid=uid).latest('recorded_at')
        # sug = Blood_sugar.objects.filter(uid=uid).latest('recorded_at')
        pre = object_to_json(pre)
        wei = object_to_json(wei)
        # sug = object_to_json(sug)
        # print(sug)
    except:
        output = {"status":"1"}
    else:
        output = {"status":"0", "blood_pressure":pre, "weight":wei}
    return JsonResponse(output,safe=False)
# , "blood_sugar":sug
@csrf_exempt
def diary_list(request,date): # 日記列表資料
    uid = request.user.uid
    try:
        if date != NULL :
            blood_pressure = Blood_pressure.objects.get(uid=uid)
            weight = Weight.objects.get(uid=uid)
            blood_sugar = Blood_sugar.objects.get(uid=uid)
            diary_diet = Diary_diet.objects.get(uid=uid)
            reply = UserCare.objects.get(uid=uid)
            data = json.loads(data)
    except:
        output = {"status":"1"}
    else:
        output = {"status":"0", "diary":[{"blood_pressure":blood_pressure, "weight":weight, "blood_sugar":blood_sugar, "diary_diet":diary_diet, "reply":reply.message}]}     
    return JsonResponse(output,safe=False)

@csrf_exempt
def diary_diet(request,date): # 飲食日記
    uid = request.user.uid
    description = request.POST.get('description')
    meal_list = ['早餐', '午餐', '晚餐']
    meal = meal_list[(int(request.POST.get('meal'))-1)%3]
    tag = []
    tag.append(request.POST.get('tag'))
    image = request.POST.get('image')
    image_count = len(image)
    lat = request.POST.get('lat')
    lng = request.POST.get('lng')
    nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        Diary_diet.objects.create(uid=uid, description=description, meal=meal, tag=tag, image=image, image_count=image_count, lat=lat, lng=lng, recorded_at=nowtime)
    except:
        output = {"status":"1"}
    else:
        output = {"status":"0", "image_url":image}
        return render(request, 'user/diary_diet.html', output)      
    return JsonResponse(output,safe=False)

@csrf_exempt
def diary_records_delete(request,date): # 刪除日記記錄
    uid = request.user.uid
    blood_sugars = []
    blood_pressures = []
    weights = []
    diets = []
    blood_sugars.append(request.POST.get('blood_sugars'))
    blood_pressures.append(request.POST.get('blood_pressures'))
    weights.append(request.POST.get('weights'))
    diets.append(request.POST.get('diets'))
    try:
        for id in blood_sugars :
            Blood_pressure.objects.get(uid=uid, pk=id).delete()
        for id in blood_pressures :
            Weight.objects.get(uid=uid, pk=id).delete()
        for id in weights :
            Blood_sugar.objects.get(uid=uid, pk=id).delete()
        for id in diets :
            Diary_diet.objects.get(uid=uid, pk=id).delete()
    except:
        output = {"status":"1"}
    else:
        output = {"status":"0"}     
    return JsonResponse(output,safe=False)

@csrf_exempt
def care(request): # 關懷諮詢
    uid = request.user.uid
    nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        if request.method == 'GET':
            UserCare = UserCare.objects.filter(member_id=0).latest('updated_at')
        if request.method == 'POST':
            message = request.POST.get('message')
            UserCare.objects.create(uid=uid, member_id=0, reply_id=NULL, message=message, updated_at=nowtime)
    except:
        output = {"status":"1"}
        return JsonResponse(output,safe=False)
    else:
        output = {"status":"0", "UserCare":UserCare}
    return render(request, 'friend/friend_list.html', output)
