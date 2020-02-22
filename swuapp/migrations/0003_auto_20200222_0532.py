# Generated by Django 2.1 on 2020-02-21 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swuapp', '0002_auto_20200222_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='b_lectureid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b_lectureid', to='swuapp.Lecture', unique=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='b_userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b_userid', to='swuapp.User', unique=True),
        ),
        migrations.AlterField(
            model_name='userlecture',
            name='l_lectureid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='l_lectureid', to='swuapp.Lecture', unique=True),
        ),
    ]
