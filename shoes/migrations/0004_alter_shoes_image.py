# Generated by Django 4.1.4 on 2023-03-28 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0003_remove_savedshoes_shoes_savedshoes_shoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='image',
            field=models.ImageField(upload_to='images/shoe'),
        ),
    ]
