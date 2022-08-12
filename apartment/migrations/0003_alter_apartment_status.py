# Generated by Django 4.1 on 2022-08-12 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0002_remove_apartment_is_forexchange_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='status',
            field=models.IntegerField(choices=[(0, 'خیر'), (1, 'بله')], default=0, verbose_name='معامله شده'),
        ),
    ]