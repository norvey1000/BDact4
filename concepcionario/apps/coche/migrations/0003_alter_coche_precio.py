# Generated by Django 3.2.7 on 2021-09-29 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coche', '0002_alter_coche_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coche',
            name='precio',
            field=models.BigIntegerField(),
        ),
    ]
