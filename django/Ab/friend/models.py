from django.db import models

# Create your models here.
class Friend(models.Model):
    uid = models.CharField(max_length = 100,blank=True)
    invite_code = models.CharField(max_length = 100,blank=True) # 邀請碼
    def __str__(self):
        message = dict()
        message = {
            'uid':self.uid,
            'invite_code':self.invite_code        
        }
        return str(message)

class Friend_data(models.Model):
    uid = models.CharField(max_length = 100,blank=True)
    relation_id = models.CharField(max_length = 100,blank=True)
    type = models.IntegerField(blank=True)
    status = models.IntegerField(blank=True)
    read = models.BooleanField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    def __str__(self):
        message = dict()
        message = {
            'uid':self.user_id,
            'relation_id':self.relation_id,
            'type':self.type,
            'status':self.status,
            'read':self.read,
            'created_at':self.created_at,
            'updated_at':self.updated_at
        }
        return str(message)

class UserCare(models.Model):
    uid = models.CharField(max_length = 100,blank=True)
    member_id = models.CharField(max_length = 100,blank=True)
    reply_id = models.CharField(max_length = 100,blank=True)
    message = models.CharField(max_length = 100,blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=True, blank=True)
    def __str__(self):
        message = dict()
        message = {
            'uid':self.uid,
            'member_id':self.member_id,
            'reply_id':self.reply_id,
            'message':self.message,
            'created_at':self.created_at,
            'updated_at':self.updated_at,
            'date':self.date
        }
        return str(message)

class Notification(models.Model):
    uid = models.CharField(max_length = 100,blank=True)
    member_id = models.CharField(max_length = 100,blank=True)
    reply_id = models.CharField(max_length = 100,blank=True)
    message = models.CharField(max_length = 100,blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    def __str__(self):
        message = dict()
        message = {
            'uid':self.uid,
            'member_id':self.member_id,
            'reply_id':self.reply_id,
            'message':self.message,
            'created_at':self.created_at,
            'updated_at':self.updated_at
        }
        return str(message)
