# Generated by Django 3.0.3 on 2020-02-23 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('primo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='guides', to='primo.Game'),
            preserve_default=False,
        ),
    ]
