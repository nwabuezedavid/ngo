# Generated by Django 5.0.4 on 2024-10-31 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_teams'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]