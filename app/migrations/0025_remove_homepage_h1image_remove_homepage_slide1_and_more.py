# Generated by Django 5.0.4 on 2024-11-01 08:41

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_rename_type_projectx_header'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='h1image',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='slide1',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='slide2',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='slide3',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='slide4',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='slide5',
        ),
        migrations.AlterField(
            model_name='homepage',
            name='uuids',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
