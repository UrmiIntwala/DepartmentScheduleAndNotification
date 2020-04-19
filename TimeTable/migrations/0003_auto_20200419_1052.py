# Generated by Django 2.1.7 on 2020-04-19 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0002_timetable_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='classroom',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='timetable',
            name='time',
            field=models.CharField(default='00:00', max_length=5),
        ),
        migrations.AddField(
            model_name='timetable',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='timetable',
            unique_together={('branch', 'division', 'day', 'time', 'year')},
        ),
    ]