# Generated by Django 4.2.2 on 2023-09-08 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_blogusers_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='blogusers',
            table='blog_users',
        ),
    ]