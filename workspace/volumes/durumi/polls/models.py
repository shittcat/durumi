import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now 
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class User(models.Model):
    userId = models.CharField(max_length=15, unique=True)
    userPw = models.CharField(max_length=200)
    introduce = models.CharField(max_length=50, default="자기소개")
    linkId = models.CharField(max_length=20, null=True, unique=True)

    def __str__(self):
        return self.userid


class ContentType(models.Model):
    typeId = models.IntegerField(primary_key=True)
    describ = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.describ

class Cat1(models.Model):
    cat1Id = models.IntegerField(primary_key=True)
    describ = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.describ

class Cat2(models.Model):
    typeId = models.IntegerField(primary_key=True)
    describ = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.describ

class Cat3(models.Model):
    typeId = models.IntegerField(primary_key=True)
    describ = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.describ

"""
class DurumiCat(models.Model):
    durumiDesc = models.CharField(max_length)
"""