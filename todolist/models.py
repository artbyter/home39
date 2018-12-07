from django.db import models


# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name='Задача')
    status = models.CharField(max_length=50, default='new', verbose_name='Статус')
    description = models.TextField(max_length=2000, null=True, blank=True,  default='', verbose_name='Описание')

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return f'{self.pk}.{self.name} ({self.status})'
