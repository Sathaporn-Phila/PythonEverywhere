# Generated by Django 3.1.6 on 2021-02-15 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='listTime',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
