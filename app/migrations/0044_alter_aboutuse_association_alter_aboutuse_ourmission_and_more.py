# Generated by Django 5.0.4 on 2024-11-04 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_alter_projectx_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuse',
            name='Association',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutuse',
            name='ourmission',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutuse',
            name='slideh1',
            field=models.TextField(blank=True, null=True),
        ),
    ]