# Generated by Django 2.2.4 on 2022-09-26 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20220926_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.AddField(
            model_name='user',
            name='age1',
            field=models.IntegerField(default=5),
        ),
    ]
