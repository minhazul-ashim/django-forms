# Generated by Django 5.0.3 on 2024-03-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='notes',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
