# Generated by Django 4.1.7 on 2023-04-04 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0010_remove_savedshoes_shoes_savedshoes_shoes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SavedShoes',
        ),
    ]
