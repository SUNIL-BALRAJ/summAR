# Generated by Django 3.2.16 on 2023-04-23 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20230414_1802'),
    ]

    operations = [
        migrations.DeleteModel(
            name='city',
        ),
        migrations.DeleteModel(
            name='forum',
        ),
        migrations.DeleteModel(
            name='uploadedVid',
        ),
    ]