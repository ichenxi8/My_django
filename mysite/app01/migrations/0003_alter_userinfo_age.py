# Generated by Django 4.1.7 on 2023-04-02 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=2),
        ),
    ]
