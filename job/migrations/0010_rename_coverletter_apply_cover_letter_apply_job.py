# Generated by Django 4.1.7 on 2023-03-22 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_apply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='coverletter',
            new_name='cover_letter',
        ),
        migrations.AddField(
            model_name='apply',
            name='job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='apply', to='job.job'),
            preserve_default=False,
        ),
    ]
