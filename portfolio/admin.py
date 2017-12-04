from django.contrib import admin

from portfolio.models import Portfolio, PortfolioImg
# Register your models here.

class PortfolioImgInline(admin.StackedInline):
    model = PortfolioImg
    extra = 3

class PortfolioAdmin(admin.ModelAdmin):
    inlines = [ PortfolioImgInline ]
    list_display = ('name', 'work_period', 'create_date')

class PortfolioImgAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'create_date')

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioImg, PortfolioImgAdmin)
