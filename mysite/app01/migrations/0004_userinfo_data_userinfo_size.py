# Generated by Django 4.1.7 on 2023-04-02 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_alter_userinfo_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='data',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='size',
            field=models.CharField(default=8, max_length=16),
            preserve_default=False,
        ),
    ]
