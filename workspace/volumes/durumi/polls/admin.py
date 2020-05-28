from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2 

class QuestionAdmin(admin.ModelAdmin):
    list_filter =['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        ('question_text'    ,{'fields' : ['question_text'],'classes':['collapse']}),
        ('Date Information' ,{'fields' : ['pub_date'],'classes':['collapse']}),
        ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')

# Register your models here.

admin.site.register(Question,QuestionAdmin)

