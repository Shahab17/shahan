# Generated by Django 4.1 on 2022-08-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500, verbose_name='آدرس')),
                ('area', models.FloatField(verbose_name='متراژ')),
                ('year', models.IntegerField(verbose_name='سال ساخت')),
                ('document', models.IntegerField(choices=[(1, 'آماده'), (2, 'در رهن'), (3, 'آماده نیست')], default=1, verbose_name='سند')),
                ('sale_price', models.IntegerField(blank=True, null=True, verbose_name='قیمت')),
                ('rent_price1', models.IntegerField(blank=True, null=True, verbose_name='رهن')),
                ('rent_price2', models.IntegerField(blank=True, null=True, verbose_name='اجاره')),
                ('person', models.CharField(max_length=200, verbose_name='مسئول')),
                ('kind', models.IntegerField(choices=[(1, 'اجاره'), (2, 'فروش'), (3, 'معاوضه')], default=1, verbose_name='مورد جهت')),
                ('status', models.IntegerField(choices=[(0, 'خیر'), (1, 'بله')], default=0, verbose_name='معامله شده')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='نوشته شده')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='اصلاح شده')),
            ],
        ),
    ]
