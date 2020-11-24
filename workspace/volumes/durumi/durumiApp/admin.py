from django.contrib import admin
from .Models.UserModel import Notice, Question, AchieveInfo, AchieveClear, User

admin.site.register(Notice)
admin.site.register(Question)
admin.site.register(AchieveInfo)
admin.site.register(AchieveClear)
admin.site.register(User)
# Register your models here.
