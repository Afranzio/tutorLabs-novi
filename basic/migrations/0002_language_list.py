# Generated by Django 3.1.4 on 2020-12-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='language_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'language_list',
            },
        ),
    ]
