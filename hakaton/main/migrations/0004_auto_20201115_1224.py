# Generated by Django 3.1.3 on 2020-11-15 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_tour_year_in_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='task',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='title',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='year_in_school',
        ),
        migrations.AddField(
            model_name='tour',
            name='Где_остановиться',
            field=models.CharField(choices=[('1', 'Место1'), ('2', 'Место2'), ('3', 'Место3'), ('4', 'Место4'), ('5', 'Место5')], default='1', max_length=2),
        ),
        migrations.AddField(
            model_name='tour',
            name='тур',
            field=models.CharField(choices=[('1', 'Небо56'), ('2', 'А-Трэвл'), ('3', 'Большие гонки')], default=[('1', 'Небо56'), ('2', 'А-Трэвл'), ('3', 'Большие гонки')], max_length=2),
        ),
    ]
