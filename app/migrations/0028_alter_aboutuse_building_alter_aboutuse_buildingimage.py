# Generated by Django 5.0.4 on 2024-11-01 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_alter_aboutuse_associationimage_alter_aboutuse_body2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuse',
            name='building',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutuse',
            name='buildingimage',
            field=models.TextField(blank=True, null=True),
        ),
    ]
