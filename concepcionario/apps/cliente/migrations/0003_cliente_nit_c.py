# Generated by Django 3.2.7 on 2021-09-30 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_cliente_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='nit_c',
            field=models.CharField(max_length=20, null=True),
        ),
    ]