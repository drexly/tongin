# -*- coding: utf-8 -*-
import datetime#여기서임포트
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200,default='통인시장 도시락집 이름')#식당 이름 필드200
    location=models.CharField(max_length=200,default='도시락집 위치')#질문필드200
    telephone=models.CharField(max_length=200,default='도시락집 연락처')#질문필드200
    pub_date=models.DateTimeField('Published Date', default=timezone.now())#등록날짜
    def was_published_recently(self):#최근에 등록됬냐
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)#출판날짜가 더 크면 트루리턴
    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean=True
    was_published_recently.short_description='최근에 등록된 집인가요?'
    taste = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    service = models.IntegerField(default=0)
    air = models.IntegerField(default=0)
    cleanness = models.IntegerField(default=0)
    count_taste = models.IntegerField(default=0)
    count_price = models.IntegerField(default=0)
    count_service = models.IntegerField(default=0)
    count_air = models.IntegerField(default=0)
    count_cleanness = models.IntegerField(default=0)
    review=models.CharField(max_length=200,default='100자 평')#질문지200
    def __str__(self):
        return self.question_text