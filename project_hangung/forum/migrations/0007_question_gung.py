# Generated by Django 3.2.5 on 2021-08-11 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20210809_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='gung',
            field=models.CharField(default='gyeongbokgung', max_length=20),
        ),
    ]
