# Generated by Django 3.1.3 on 2020-11-15 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_tour_где_поесть'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='Где_остановиться',
            field=models.CharField(choices=[('Старый Маяк', 'Старый Маяк'), ('Золотой Слон', 'Золотой Слон'), ('Виктория', 'Виктория'), ('Зорянка', 'Зорянка'), ('олотой Дракон', 'Золотой Дракон'), ('Hilton Garden inn Orenburg', 'Hilton Garden inn Orenburg'), ('Дубрава Плюс', 'Дубрава Плюс')], default='Старый Маяк', max_length=123123),
        ),
        migrations.AlterField(
            model_name='tour',
            name='Где_поесть',
            field=models.CharField(choices=[('Макдоналдс', 'Макдоналдс'), ('Имбирь', 'Имбирь'), ('Пасс', 'Роял Пасс'), ('Роза ветров', 'Роза ветров'), ('Шашлычная Тандыр', 'Шашлычная Тандыр'), ('Пахлава', 'Пахлава'), ('Coffee like', 'Coffee like')], default='Макдоналдс', max_length=123123),
        ),
    ]
