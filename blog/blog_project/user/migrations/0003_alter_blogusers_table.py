# Generated by Django 4.2.2 on 2023-09-08 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_token'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='blogusers',
            table='blog_user',
        ),
    ]
