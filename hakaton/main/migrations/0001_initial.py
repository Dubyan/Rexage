# Generated by Django 3.1.3 on 2020-11-14 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Выбранный тур')),
                ('task', models.TextField(verbose_name='Отзыв')),
            ],
        ),
    ]
