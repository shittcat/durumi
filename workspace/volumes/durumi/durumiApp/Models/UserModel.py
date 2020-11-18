import datetime
from django.utils import timezone
from django.db import models
# Create your models here.

"유저 정보"


class User(models.Model):
    userId = models.CharField(max_length=15, unique=True)
    userPw = models.CharField(max_length=500)
    userSalt = models.CharField(max_length=100)
    userMail = models.EmailField(max_length=120)
    userLv = models.IntegerField(default="1", null=False)
    userExp = models.IntegerField(default="0", null=False)
    introduce = models.CharField(max_length=150, default="자기소개")
    profileImg = models.CharField(max_length=20, default="usericon1", null=False)
    linkId = models.CharField(max_length=20, blank=True, unique=True)

    def __str__(self):
        return self.userId


"관광타입 ID"


class ContentType(models.Model):
    typeId = models.IntegerField(primary_key=True)
    describ = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.describ


"두루미 자체 분류"


class DurumiCat(models.Model):
    durumiDesc = models.CharField(primary_key=True, max_length=25)
    iconAddr = models.CharField(max_length=100)

    def __str__(self):
        return self.durumiDesc


"대분류"


class Cat1(models.Model):
    type1Id = models.IntegerField(primary_key=True)
    describ = models.CharField(max_length=30, unique=True)
    durumiDesc = models.ForeignKey(DurumiCat, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.describ


"중분류"


class Cat2(models.Model):
    typeId = models.IntegerField(primary_key=True)
    describ = models.CharField(max_length=30, unique=True)
    durumiDesc = models.ForeignKey(DurumiCat, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.describ


"소분류"


class Cat3(models.Model):
    typeId = models.IntegerField(primary_key=True)
    describ = models.CharField(max_length=30, unique=True)
    durumiDesc = models.ForeignKey(DurumiCat, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.describ


"사진 정보"


class Photo(models.Model):
    imgAddr = models.CharField(null=False, unique=True, max_length=100)
    pubDate = models.DateTimeField('photo published')
    locName = models.CharField(null=False, max_length=30)
    views = models.IntegerField
    likey = models.IntegerField
    userId = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.imgAddr


"트립노트 정보"


class Tripnote(models.Model):
    name = models.CharField(default="나만의 경로", max_length=30)
    dest = models.CharField(null=True, max_length=10000)
    cat = models.CharField(null=True, max_length=100)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


"배지 달성 내용"


class BadgeClear(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    badge1 = models.BooleanField
    badge2 = models.BooleanField
    badge3 = models.BooleanField
    badge4 = models.BooleanField
    badge5 = models.BooleanField

    def __str__(self):
        return self.userId


"배지 정보"


class BadgeInfo(models.Model):
    name = models.CharField(primary_key=True, max_length=10)
    content = models.CharField(max_length=30)
    imgAddr = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.name


"업적 달성 내용"


class AchieveClear(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    Achieve1 = models.BooleanField
    Achieve2 = models.BooleanField
    Achieve3 = models.BooleanField
    Achieve4 = models.BooleanField
    Achieve5 = models.BooleanField

    def __str__(self):
        return self.userId


"업적 정보"


class AchieveInfo(models.Model):
    name = models.CharField(primary_key=True, max_length=10)
    content = models.CharField(max_length=30)
    imgAddr = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.name


"공지사항"


class Notice(models.Model):
    title = models.CharField(max_length=200, null=False)
    content = models.TextField()
    pubDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


"문의사항"

class Question(models.Model):
    title = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=120, null=False)
    content = models.TextField()
    pubDate = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return self.title