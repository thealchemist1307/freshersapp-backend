# Generated by Django 2.2.13 on 2020-06-16 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(default='', max_length=70)),
                ('timings', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
