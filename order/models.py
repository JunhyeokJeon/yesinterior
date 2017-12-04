from django.db import models
from portfolio.fields import ThumbnailImageField
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
    title = models.CharField('제목', max_length=50)
    location = models.CharField('장소', max_length=50)
    date = models.CharField('예상 공사시작 날짜', max_length=20)
    image = ThumbnailImageField('도면 사진', upload_to='photo')
    description = models.TextField('상세설명')
    name = models.CharField('이름', max_length=10)
    phone = models.CharField('휴대폰 번호', max_length=100, blank=True)
    email = models.EmailField('Email')

    create_date = models.DateTimeField('게시일', auto_now_add=True)
    owner = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ('-create_date',)

    def __str__(self):
        return self.title
