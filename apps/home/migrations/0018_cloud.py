# Generated by Django 3.2.6 on 2023-07-28 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_ipfs_f_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='cloud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.IntegerField(default=True)),
            ],
        ),
    ]
