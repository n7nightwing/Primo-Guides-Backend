# Generated by Django 3.0.3 on 2020-02-24 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primo', '0002_guide_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='photo_url',
            field=models.TextField(default=''),
        ),
    ]
