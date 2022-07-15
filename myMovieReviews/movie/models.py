from django.db import models
from re import T

# Create your models here.

class genrebox(models.Model):
    genrele = (('sf','sf'),('comic','comic'),('horror','horror'))

class Movie(models.Model):
    title = models.CharField(max_length=50, verbose_name="제목") #챠필드 최대길이,제목안쓰면 제목이라고 미리들어감?
    openyear = models.IntegerField(verbose_name="개봉년도")
    genre = models.CharField(max_length=50, choices=genrebox.genrele, default='sf')
    # genre = models.CharField(max_length=50, verbose_name="장르")
    score = models.IntegerField(verbose_name="별점")
    runningtime = models.IntegerField(verbose_name="러닝타임")
    content = models.TextField(verbose_name="리뷰")
    director = models.CharField(max_length=50, verbose_name="감독")
    actor = models.CharField(max_length=50, verbose_name="배우")