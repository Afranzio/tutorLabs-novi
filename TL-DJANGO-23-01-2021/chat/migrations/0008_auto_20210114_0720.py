# Generated by Django 3.1.4 on 2021-01-14 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_classes'),
    ]

    operations = [
        migrations.CreateModel(
            name='myclasses',
            fields=[
                ('student_id', models.CharField(blank=True, max_length=40)),
                ('teacher_id', models.FloatField(blank=True, max_length=45)),
                ('class_id', models.CharField(blank=True, max_length=40, primary_key=True, serialize=False)),
                ('class_name', models.CharField(blank=True, max_length=45)),
                ('class_rate', models.CharField(blank=True, max_length=60)),
                ('Class_description', models.CharField(blank=True, max_length=60)),
            ],
            options={
                'db_table': 'myclasses',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='classes',
        ),
    ]
