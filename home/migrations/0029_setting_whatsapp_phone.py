# Generated by Django 3.1.5 on 2021-02-11 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20210105_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='whatsapp_phone',
            field=models.CharField(default='', max_length=20),
        ),
    ]