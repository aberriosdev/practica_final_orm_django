# Generated by Django 5.1.5 on 2025-01-24 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0002_actualizado_campos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='f_fabricacion',
            field=models.DateField(default='2015-01-01'),
        ),
    ]
