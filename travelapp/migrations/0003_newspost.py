# Generated by Django 3.2.5 on 2021-07-15 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_place_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='newspost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=50)),
                ('day', models.IntegerField()),
                ('headline', models.TextField()),
                ('descr', models.TextField()),
                ('image', models.ImageField(upload_to='pic')),
            ],
        ),
    ]
