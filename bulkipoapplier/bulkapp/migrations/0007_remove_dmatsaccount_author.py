# Generated by Django 4.1.5 on 2023-01-24 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bulkapp', '0006_dmatsaccount_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dmatsaccount',
            name='author',
        ),
    ]
