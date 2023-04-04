# Generated by Django 4.1.7 on 2023-04-04 07:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0009_remove_shoes_category_shoes_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savedshoes',
            name='shoes',
        ),
        migrations.AddField(
            model_name='savedshoes',
            name='shoes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shoes.shoes'),
            preserve_default=False,
        ),
    ]