# Generated by Django 2.1 on 2020-02-21 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swuapp', '0003_auto_20200222_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
