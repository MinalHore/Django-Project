# Generated by Django 5.0.6 on 2024-07-01 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taskapp', '0006_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]
