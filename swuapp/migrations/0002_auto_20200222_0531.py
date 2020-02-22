# Generated by Django 2.1 on 2020-02-21 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swuapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('boardid', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=100)),
                ('qualityscore', models.IntegerField()),
                ('difficultyscore', models.IntegerField()),
                ('recommendation', models.IntegerField()),
                ('declaration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('semester', models.CharField(max_length=30)),
                ('lectureid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('lecturename', models.CharField(max_length=50)),
                ('professor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserLecture',
            fields=[
                ('l_userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='l_userid', serialize=False, to='swuapp.User', unique=True)),
                ('l_lectureid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='l_lectureid', to='swuapp.Lecture')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='b_lectureid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b_lectureid', to='swuapp.Lecture'),
        ),
        migrations.AddField(
            model_name='board',
            name='b_userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b_userid', to='swuapp.User'),
        ),
    ]
