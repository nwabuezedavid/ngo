# Generated by Django 5.0.4 on 2024-10-26 19:39

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutuse',
            fields=[
                ('h1', models.CharField(blank=True, max_length=50, null=True)),
                ('slideh1', models.TextField(blank=True, max_length=50, null=True)),
                ('h2', models.CharField(blank=True, max_length=50, null=True)),
                ('slideh2', models.TextField(blank=True, max_length=50, null=True)),
                ('h3', models.CharField(blank=True, max_length=50, null=True)),
                ('slideh3', models.TextField(blank=True, max_length=50, null=True)),
                ('h4', models.CharField(blank=True, max_length=50, null=True)),
                ('slideh4', models.TextField(blank=True, max_length=50, null=True)),
                ('h5', models.CharField(blank=True, max_length=50, null=True)),
                ('slideH5', models.TextField(blank=True, max_length=50, null=True)),
                ('uuids', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ourmission', models.TextField(blank=True, max_length=50, null=True)),
                ('ourvision', models.TextField(blank=True, max_length=50, null=True)),
                ('body', models.TextField(blank=True, max_length=50, null=True)),
                ('Association', models.TextField(blank=True, max_length=50, null=True)),
                ('Associationimage', models.TextField(blank=True, max_length=50, null=True)),
                ('building', models.TextField(blank=True, max_length=50, null=True)),
                ('buildingimage', models.TextField(blank=True, max_length=50, null=True)),
                ('body2', models.TextField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('uuids', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('body', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='stayupdated',
            fields=[
                ('uuids', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='header',
            new_name='h1',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='imagex',
            new_name='h1image',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='title',
            new_name='h2',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='imagex1',
            new_name='slide1',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='imagex2',
            new_name='slide2',
        ),
        migrations.RenameField(
            model_name='siteedit',
            old_name='Address',
            new_name='facebooklink',
        ),
        migrations.RenameField(
            model_name='siteedit',
            old_name='country',
            new_name='headOffice',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='date',
        ),
        migrations.AddField(
            model_name='homepage',
            name='h3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='h4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='h5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slide3',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slide4',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slide5',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='siteedit',
            name='headoffice2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='siteedit',
            name='instergram',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='siteedit',
            name='twiiterlink',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='siteedit',
            name='youtubelink',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
