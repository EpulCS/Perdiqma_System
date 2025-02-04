# Generated by Django 4.2.6 on 2024-06-20 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perdiqma_homepage', '0003_activity'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery_pictures/')),
                ('caption', models.CharField(max_length=200)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
