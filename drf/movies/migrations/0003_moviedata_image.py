# Generated by Django 5.0.4 on 2024-04-21 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='image',
            field=models.ImageField(default='Images/None/No-img.jpg', upload_to='Images/'),
        ),
    ]