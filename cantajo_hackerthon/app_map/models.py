from django.db import models
from django import forms
from django.utils import timezone


# Create your models here.


class Catlist(models.Model):
    name = models.CharField(max_length=10)
    genderchoice = (('0','모름'), ('1','남'), ('2','여'))
    gender = models.CharField(max_length = 1, choices = genderchoice)
    age = models.CharField(max_length=1, choices = (('a', '아기묘'), ('b', '성묘'), ('c', '노묘'), ('d', '모름')), default = '?')
    furious = models.BooleanField( '경계심이 많음', default=False)
    family = models.BooleanField('가족이 있음', default=False)
    food = models.BooleanField('주기적으로 급식을 먹고 있음', default=False)
    touch = models.BooleanField('만지면 안됨', default=False)
    health = models.BooleanField('정기적으로 병원을 다니고 있음', default=False)
    catimage = models.ImageField(upload_to= 'images/')
    mapimage = models.ImageField(upload_to= 'images/')
    info = models.TextField(default='a')
    marks = models.TextField(default='a')           
    pos_y = models.TextField(default='a')
    pos_x = models.TextField(default='a')
    
    
    def __str__(self):
        
        return self.name


class Catphoto(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to = 'images/')
    catnum = models.IntegerField(default = -5)
    pub_date=models.DateTimeField('date published',null=True)
    def __str__(self):

        return self.title