# Generated by Django 4.1.7 on 2023-03-14 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
