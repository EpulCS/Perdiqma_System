# Generated by Django 4.2.6 on 2024-06-09 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perdiqma_homepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perdiqma',
            name='join_date',
        ),
    ]
