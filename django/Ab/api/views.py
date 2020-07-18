from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from .models import *
from django.core.mail import send_mail

# Create your views here.
def index(request): # 首頁
    return render(request, 'index.html')

def register(request): # 註冊
    errors = []
    account = None
    password = None
    phone = None
    email = None
    if request.method == 'POST':
        if not request.POST.get('account'):
            errors.append('帳號不能空白')
        else:
            account = request.POST.get('account')
        if not request.POST.get('phone'):
            errors.append('手機不能空白')
        else:
            phone = request.POST.get('phone')
        if not request.POST.get('email'):
            errors.append('信箱不能空白')
        else:
            email = request.POST.get('email')
        if not request.POST.get('password'):
            errors.append('密碼不能空白')
        else:
            password = request.POST.get('password')
        if account and password and phone and email :
            UserProfile.objects.create_user(username=account,phone=phone,email=email,password=password, is_active=False)
            status = {"status": "0"}
            return HttpResponseRedirect('/api/auth')
        status = {"status": "1"}
    return render(request, 'register.html', {'errors': errors})

def login(request): # 登入
    errors =[]
    account = None
    password = None
    fb_check = False
    if request.method == "POST":
        if not request.POST.get('account'):
            errors.append('帳號不能空白')
        else:
            account = request.POST.get('account')
        if not request.POST.get('password'):
            errors.append('密碼不能空白')
        else:
            password = request.POST.get('password')
        if request.POST.get('fb_check') != 'yes':
            errors.append('FB聲明未勾選')
            status = {"status": "3"}
        else:
            fb_check = True
        if account is not None and password is not None and fb_check is True:
            user = auth.authenticate(username=account, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/api/')
                status = {"status": "0"}
            else:
                errors.append('帳號或密碼有誤')
        status = {"status": "1"}
    return render(request,'login.html', {'errors': errors})

def logout(request): # 登出
    auth.logout(request)
    return HttpResponseRedirect('/api/')

def send(request): # 信箱認證--發送
    errors = []
    email = None
    phone = None
    if request.method == 'POST':
        if not request.POST.get('email'):
            errors.append('信箱不能空白')
        else:
            email = request.POST.get('email')
        if not request.POST.get('phone'):
            errors.append('手機不能空白')
        else:
            phone = request.POST.get('phone')
        if phone and email:
            title = "Django驗證信"
            msg = "click here"
            email_from = "fred881215@gmail.com"
            send_mail(title, msg, email_from, [email], fail_silently=False)
            status = {"status": "0"}
            return HttpResponseRedirect('/api/verification/check')
        status = {"status": "1"}
    return render(request, 'send.html', {'errors': errors})

# def check(request): # 信箱認證--檢查

# def check_user(request):
#     if request.method =='POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         # 检测用户是否存在
#         user = User.objects.filter(username=username,password=password).first()
#         if user:
#             return HttpResponse("用户已经存在")
#         # 保存用户信息
#         # 刚注册的用户是未激活
#         user = User.objects.create(username=username,password=password,is_active=0)

#         # 发送邮件，确认激活
#         token = token_confirm.generate_validate_token(user.uid)
#         print(token)
#         # 构造验证url
#         url = "http://"+request.get_host()+reverse("App:activeuser",kwargs={'token':token})
#         # 加载模板
#         html = loader.get_template('active.html').render({'url':url})
#         print(url)
#         send_mail("账号激活",'',EMAIL_FROM,['Zz_lzk@163.com'],html_message=html)
#         return HttpResponse("激活邮件已经发送，请登录邮箱确认激活")
#     return render(request,'register.html')


# def active_user(request,token):
#     # 激活用户
#     try:
#         uid = token_confirm.confirm_validate_token(token)
#     except Exception as e:
#         print(e)
#         try:
#             uid = token_confirm.remove_validate_token(token)
#             user = User.objects.get(pk=uid)
#             user.delete()
#         except:
#             pass
#         return HttpResponse("激活失败，请重新注册")
#     try:
#         user = User.objects.get(pk=uid)
#     except User.DoesNotExist:
#         return HttpResponse("你激活的用户不存在，请重新注册")
#     user.is_active = 1  # 激活用户
#     user.save()

#     return HttpResponse("用户已激活，请登录系统")