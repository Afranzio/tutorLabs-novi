# Generated by Django 3.1.4 on 2021-01-13 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20201226_1844'),
    ]

    operations = [
        migrations.CreateModel(
            name='connect',
            fields=[
                ('student_id', models.CharField(blank=True, max_length=40, primary_key=True, serialize=False)),
                ('teacher_id', models.FloatField(blank=True, max_length=45)),
                ('connect_id', models.CharField(blank=True, max_length=45)),
                ('class_id', models.CharField(blank=True, max_length=60)),
                ('connect_status', models.CharField(blank=True, max_length=60)),
                ('connect_seek_rating', models.CharField(blank=True, max_length=60)),
                ('connect_teach_rating', models.CharField(blank=True, max_length=60)),
                ('connect_rate', models.CharField(blank=True, default='0', max_length=45)),
            ],
            options={
                'db_table': 'connect',
            },
        ),
    ]
