# Generated by Django 3.2.16 on 2023-04-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0004_auto_20230423_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(default=True, max_length=20)),
                ('memid', models.IntegerField(default=True)),
                ('location', models.CharField(default=True, max_length=20)),
            ],
        ),
    ]
