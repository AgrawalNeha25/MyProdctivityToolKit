# Generated by Django 2.1.7 on 2019-06-30 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20190630_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='deadline_html',
        ),
    ]
