# Generated by Django 4.1 on 2022-08-08 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='bookImage',
            new_name='image',
        ),
    ]
