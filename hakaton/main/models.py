from django.db import models


class Tour(models.Model):
    Туроператор = models.TextField(
        max_length=123123,
        default='',
    )
    Где_остановиться = models.TextField(
        max_length=123123,
        default=''
    )
    Где_поесть = models.TextField(
        max_length=123123,
        default=''
    )


    Комментарий = models.TextField(
        max_length=123123,
        default=''
    )








    def __str__(self):
        return self.Туроператор
