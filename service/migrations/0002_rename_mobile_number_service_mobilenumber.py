# Generated by Django 5.0.1 on 2024-03-20 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='mobile_number',
            new_name='mobilenumber',
        ),
    ]
