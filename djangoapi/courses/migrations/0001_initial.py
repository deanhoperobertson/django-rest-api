# Generated by Django 4.0.2 on 2022-02-16 22:27

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
                ('name', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
