from django.db import models
from django.core.urlresolvers import reverse

from portfolio.fields import ThumbnailImageField
# Create your models here.

class Portfolio(models.Model):
    name = models.CharField('제목', max_length=50)
    location = models.CharField('장소', max_length=50)
    work_period = models.CharField('공사기간', max_length=50)
    description = models.TextField('서두', blank=True)
    create_date = models.DateTimeField('게시일', auto_now_add=True)
    modify_date = models.DateTimeField('수정일', auto_now=True)

    class Meta:
        ordering = ('-create_date',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:', args=(self.id,))

class PortfolioImg(models.Model):
    portfolio = models.ForeignKey(Portfolio)
    description = models.TextField('사진설명', blank=True)
    image = ThumbnailImageField(upload_to='photo')
    create_date = models.DateTimeField('게시일', auto_now_add=True)
    modify_date = models.DateTimeField('수정일', auto_now=True)

    class Meta:
        ordering = ('create_date',)

    def __str__(self):
        return self.description
