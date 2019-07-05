# Generated by Django 2.1.7 on 2019-06-30 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_deadline_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='post',
            name='message_html',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
