# Generated by Django 3.2.12 on 2022-04-17 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supports', '0002_answer_inquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='email_rcv_yn',
            field=models.BooleanField(verbose_name='이메일수신여부'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='phone_rcv_yn',
            field=models.BooleanField(verbose_name='문자수신여부'),
        ),
    ]
