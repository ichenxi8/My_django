# Generated by Django 4.1.7 on 2023-04-05 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateField(verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='dapart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.department', verbose_name='部门'),
        ),
    ]
