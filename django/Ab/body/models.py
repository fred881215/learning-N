from django.db import models

# Create your models here.
class Blood_pressure(models.Model):
    uid = models.CharField(max_length = 100,blank=True)
    systolic = models.FloatField(blank=True)
    diastolic = models.FloatField(blank=True)
    pulse = models.IntegerField(blank=True)
    recorded_at= models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=True, blank=True)
    def __str__(self):
        message = dict()
        message = {
            'uid':self.uid,
            'systolic':self.systolic,
            'diastolic':self.diastolic,
            'pulse':self.pulse,
            'recorded_at':self.recorded_at,
            'created_at':self.created_at,
            'date':self.date
        }
        return str(message)

class Weight(models.Model):
    uid = models.CharField(max_length = 100,blank=True)
    weight = models.FloatField(blank=True)
    body_fat = models.FloatField(blank=True)
    bmi = models.FloatField(blank=True)
    recorded_at= models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=True, blank=True)
    def __str__(self):
        message = dict()
        message = {
            'uid':self.uid,
            'weight':self.weight,
            'body_fat':self.body_fat,
            'bmi':self.bmi,
            'recorded_at':self.recorded_at,
            'created_at':self.created_at,
            'date':self.date
        }
        return str(message)

class Blood_sugar(models.Model):
    uid = models.CharField(max_length = 100,blank=True)
    sugar = models.IntegerField(blank=True)# 血糖
    timeperiod = models.CharField(max_length = 100,blank=True) # 時段
    recorded_at= models.DateTimeField(auto_now=False, auto_now_add=False, blank=True) # 上傳時間
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=True, blank=True)
    def __str__(self):
        message = dict()
        message = {
            'uid':self.uid,
            'sugar':self.sugar,
            'timeperiod':self.timeperiod,
            'recorded_at':self.recorded_at,
            'created_at':self.created_at,
            'date':self.date
        }
        return str(message)

class Diary_diet(models.Model):
    uid = models.CharField(max_length = 100,blank=True)
    description = models.CharField(max_length = 100,blank=True)
    meal = models.CharField(max_length = 100,blank=True)
    tag = models.CharField(max_length = 100,blank=True)
    image = models.ImageField(upload_to = 'diet/diet_%Y-%m-%d_%H:%M:%S')
    image_count = models.IntegerField(blank=True)
    lat = models.FloatField(max_length = 100,blank=True)
    lng = models.FloatField(max_length = 100,blank=True)
    recorded_at = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    def __str__(self):
        message = dict()
        message = {
            'uid':self.uid,
            'description':self.description,
            'meal':self.meal,
            'tag':self.tag,
            'image':self.image,
            'image_count':self.image_count,
            'lat':self.lat,
            'lng':self.lng,
            'recorded_at':self.recorded_at
        }
        return str(message)
