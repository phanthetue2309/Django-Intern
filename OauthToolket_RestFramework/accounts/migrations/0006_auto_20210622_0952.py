# Generated by Django 3.1.12 on 2021-06-22 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210622_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]
