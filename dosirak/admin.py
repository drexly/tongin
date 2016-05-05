# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.contrib import admin
from dosirak.models import Question
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
   fieldsets =[('도시락점 이름',{'fields':['question_text']}),('Location',{'fields':['location']}),('Contacts',{'fields':['telephone']}),('Date information',{'fields':['pub_date'],'classes':['collapse']}),('맛',{'fields':['taste']}),('가격',{'fields':['price']}),('서비스',{'fields':['service']}),('분위기',{'fields':['air']}),('청결도',{'fields':['cleanness']}),('100자평',{'fields':['review']})]
   #fieldsets=[('Questionaire',{'fields':['question_text']}),('Date Info',{'fields':['pub_date']}),]
   # fields = ['pub_date','question_text']
   list_display = ('question_text','location','telephone','pub_date','was_published_recently','taste','price','service','cleanness','air','review')
   list_filter = ['pub_date','question_text']
   #search_fields = ['question_text']
   #search_fields = ['foreign_key__related_fieldname']
   search_fields = ['question_text','location','telephone']
admin.site.register(Question,QuestionAdmin)#폼 만들어줘서 등
