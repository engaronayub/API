# Generated by Django 5.1.4 on 2025-01-12 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('language', models.CharField(max_length=250)),
                ('price', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('instructor', models.CharField(max_length=100)),
            ],
        ),
    ]
