# Generated by Django 2.1.7 on 2019-06-30 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='groupmember',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='groupmember',
            name='group',
        ),
        migrations.RemoveField(
            model_name='groupmember',
            name='user',
        ),
        migrations.RemoveField(
            model_name='group',
            name='description_html',
        ),
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
        migrations.RemoveField(
            model_name='group',
            name='slug',
        ),
        migrations.DeleteModel(
            name='GroupMember',
        ),
    ]