# Generated by Django 4.1.5 on 2023-01-24 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bulkapp', '0004_alter_dmatsaccount_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dmatsaccount',
            name='user',
        ),
    ]