# Generated by Django 4.1.7 on 2023-04-02 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_userinfo_data_userinfo_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='data',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='size',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(),
        ),
    ]
