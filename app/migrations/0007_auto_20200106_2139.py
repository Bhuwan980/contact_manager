# Generated by Django 3.0.1 on 2020-01-06 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200106_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='info',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
