# Generated by Django 4.2.6 on 2023-10-16 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobApp', '0003_applicantdetails_email_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantdetails',
            name='email_id',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='applicantdetails',
            name='phone_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
