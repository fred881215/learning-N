from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib import auth
from .models import *
from api.models import *
from datetime import date,datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def friend_code(request): # 獲取控糖團邀請碼
    uid = request.user.uid
    try:
        user_friend = Friend.objects.get(uid=uid)
        invite_code = user_friend.invite_code
    except:
        output = {"status":"1"}
    else:
        output = {"status":"0", "invite_code":invite_code}        
    return JsonResponse(output,safe=False)

@csrf_exempt
def friend_list(request): # 控糖團列表
    uid = request.user.uid
    try:
        requests_list = UserProfile.objects.all()
    except:
        output = {"status":"1"}
        return JsonResponse(output,safe=False)
    else:
        output = {"status":"0", "requests_list":requests_list}
    return render(request, 'friend/friend_list.html', output)

@csrf_exempt
def friend_requests(request): # 獲取控糖團邀請
    uid = request.user.uid
    try:
        requests_list = Friend_data.objects.get(relation_id=uid)
        friend_uid = requests_list.uid
        user = UserSet.objects.get(uid=friend_uid)
    except:
        output = {"status":"1"}
        return JsonResponse(output,safe=False)
    else:
        output = {"status":"0", "requests_list":requests_list, "user":user}
    return render(request, 'friend/friend_requests.html', output)

@csrf_exempt
def friend_send(request): # 送出控糖團邀請
    uid = request.user.uid
    friend_type = request.POST.get('type')
    invite_code = request.POST.get('invite_code')
    nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        user_friend = Friend.objects.get(invite_code=invite_code)
        friend_uid = user_friend.uid
        user_file1 = UserProfile.objects.get(uid=uid)
        user_file2 = UserProfile.objects.get(uid=friend_uid)
    except:
        output = {"status":"1"} # 1: 邀請碼無效
    else:
        if Friend_data.objects.get(uid=uid, relation_id=friend_uid, status=1):
            output = {"status":"1"} # 2: 已經成為好友
        else:
            Friend_data.objects.create(uid=uid, relation_id=friend_uid, type=friend_type, read=False, updated_at=nowtime)
            Friend_data.objects.create(uid=friend_uid, relation_id=uid, type=friend_type, read=False, updated_at=nowtime)
            output = {"status":"0"}
    return JsonResponse(output,safe=False)

@csrf_exempt
def friend_accept(request,friend_uid): # 接受控糖團邀請
    uid = request.user.uid
    nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        check1 = Friend_data.objects.get(uid=uid, relation_id=friend_uid)
        check1.read = True
        check1.status = 1
        check1.updated_at = nowtime
        check1.save()
        check2 = Friend_data.objects.get(uid=friend_uid, relation_id=uid)
        check2.read = True
        check2.status = 1
        check2.updated_at = nowtime
        check2.save()
    except:
        output = {"status":"1"}
    else:
        output = {"status":"0"}
    return JsonResponse(output,safe=False)

@csrf_exempt
def friend_refuse(request,friend_uid): # 拒絕控糖團邀請
    uid = request.user.uid
    nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        check1 = Friend_data.objects.get(uid=uid, relation_id=friend_uid)
        check1.read = True
        check1.status = 2
        check1.updated_at = nowtime
        check1.save()
        check2 = Friend_data.objects.get(uid=friend_uid, relation_id=uid)
        check2.read = True
        check2.status = 2
        check2.updated_at = nowtime
        check2.save()
    except:
        output = {"status":"1"}
    else:
        output = {"status":"0"}
    return JsonResponse(output,safe=False)

@csrf_exempt
def friend_delete(request,friend_uid): # 刪除控糖團邀請
    uid = request.user.uid
    try:
        Friend_data.objects.get(uid=uid, relation_id=friend_uid).delete()
        Friend_data.objects.get(uid=friend_uid, relation_id=uid).delete()
    except:
        output = {"status":"1"}
    else:
        output = {"status":"0"}
    return JsonResponse(output,safe=False)

@csrf_exempt
def friend_results(request): # 控糖團結果
    uid = request.user.uid
    try:
        requests_list = Friend_data.objects.get(uid=uid)
        friend_uid = requests_list.relation_id
        relation = UserSet.objects.get(uid=friend_uid)
    except:
        output = {"status":"1"}
        return JsonResponse(output,safe=False)
    else:
        output = {"status":"0", "requests_list":requests_list, "relation":relation}
    return render(request, 'friend/friend_list.html', output)

@csrf_exempt
def notification(request): # 親友團通知
    uid = request.user.uid
    message = request.POST.get('message')
    nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        user = Friend_data.objects.get(uid=uid, type=1, status=1)
        friend_uid_list = user.relation_id
        for friend_uid in friend_uid_list:
            Notification.objects.create(uid=uid, member_id=1, reply_id=friend_uid, message=message, updated_at=nowtime)
    except:
        output = {"status":"1"}
    else:
        output = {"status":"0"}
    return JsonResponse(output,safe=False)

@csrf_exempt
def friend_remove(request): # 刪除更多好友
    uid = request.user.uid
    ids = []
    ids.append(request.POST.get('ids'))
    try:
        for user_id in ids :
            Friend_data.objects.get(uid=uid, relation_id=user_id).delete()
            Friend_data.objects.get(uid=user_id, relation_id=uid).delete()
    except:
        output = {"status":"1"}
    else:
        output = {"status":"0"}
    return JsonResponse(output,safe=False)