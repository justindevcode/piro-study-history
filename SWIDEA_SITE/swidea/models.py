from django.db import models
from re import T

# Create your models here.

class swtool(models.Model):
    toolname = models.CharField(max_length=50, verbose_name="툴이름")
    tooltype = models.CharField(max_length=50, verbose_name="툴타입")
    toolcontent = models.TextField(verbose_name="툴내용")

class swidea(models.Model):
    ideaname = models.CharField(max_length=50, verbose_name="아이디어이름")
    ideaphoto = models.ImageField(blank=True,verbose_name="아이디어사진", null=True)
    ideacontent = models.TextField(verbose_name="아이디어내용")
    ideainterest = models.IntegerField(verbose_name="아이디어관심도")
    ideatool = models.ForeignKey(swtool,on_delete=models.CASCADE,related_name="아이디어툴")
    ideachoice = models.BooleanField(default=False, verbose_name="아이디어찜")