# Generated by Django 3.1.3 on 2020-11-15 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201115_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='тур',
            field=models.CharField(choices=[('Туроператор - Небо56', 'Небо56'), ('Туроператор - А-Трэвл', 'А-Трэвл'), ('Туроператор - Болльшие гонки', 'Большие гонки')], default=[('Туроператор - Небо56', 'Небо56'), ('Туроператор - А-Трэвл', 'А-Трэвл'), ('Туроператор - Болльшие гонки', 'Большие гонки')], max_length=555),
        ),
    ]
