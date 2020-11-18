from django.contrib import admin
from .Models.UserModel import Notice, Question, AchieveInfo

admin.site.register(Notice)
admin.site.register(Question)
admin.site.register(AchieveInfo)
# Register your models here.
