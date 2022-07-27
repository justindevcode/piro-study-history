from django.db import models

# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    like = models.BooleanField(default=False)
