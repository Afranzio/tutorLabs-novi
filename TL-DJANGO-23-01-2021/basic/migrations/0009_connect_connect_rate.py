# Generated by Django 3.1.4 on 2021-01-13 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0008_connect'),
    ]

    operations = [
        migrations.AddField(
            model_name='connect',
            name='connect_rate',
            field=models.CharField(blank=True, max_length=45),
        ),
    ]