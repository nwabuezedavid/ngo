# Generated by Django 5.0.4 on 2024-11-01 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_alter_job_closedate_alter_job_date_alter_news_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='body',
            field=models.TextField(),
        ),
    ]
