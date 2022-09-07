from telnetlib import STATUS
from django.db import models
from django.urls import reverse


DOCUMENT = (
    (1, 'آماده'),
    (2, 'در رهن'),
    (3, 'آماده نیست')
)

KIND = (
    (1,'اجاره'),
    (2,'فروش'),
    (3,'معاوضه')
)

STATUS = (
    (0,'خیر'),
    (1,'بله')
)

class Field(models.Model):
    
    address = models.CharField(max_length=500, verbose_name='آدرس')
    area = models.FloatField(verbose_name='متراژ')
    document = models.IntegerField(choices=DOCUMENT, verbose_name='سند', default=1)
    sale_price = models.IntegerField(verbose_name='قیمت', null=True, blank=True)
    rent_price1 = models.IntegerField(verbose_name='رهن', null=True, blank=True)
    rent_price2 = models.IntegerField(verbose_name='اجاره', null=True, blank=True)
    person = models.CharField(max_length=200, verbose_name='مسئول')
    kind = models.IntegerField(verbose_name='مورد جهت', choices = KIND, default=1)
    number = models.IntegerField(verbose_name='قطعه شماره', default=1)
    status = models.IntegerField(verbose_name='معامله شده', choices = STATUS, default=0)
    
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='نوشته شده')
    updated_on = models.DateTimeField(auto_now= True, verbose_name='اصلاح شده')

    def get_absolute_url(self):
        return reverse('field_detail', args=[self.id])