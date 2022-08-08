# Generated by Django 4.1 on 2022-08-08 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=800)),
                ('bookImage', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=200)),
                ('favorite', models.BooleanField()),
                ('pages', models.IntegerField()),
                ('authors', models.CharField(max_length=500)),
            ],
        ),
    ]