# Generated by Django 5.0.4 on 2024-11-02 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_alter_projectx_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectx',
            name='Status',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]