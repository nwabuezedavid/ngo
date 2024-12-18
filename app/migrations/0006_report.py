# Generated by Django 5.0.4 on 2024-10-31 07:40

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_aboutuse_idx_contactus_idx_donate_idx_homepage_idx_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='report',
            fields=[
                ('uuids', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('body', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.TextField(blank=True, max_length=500, null=True)),
                ('date', models.DateField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
