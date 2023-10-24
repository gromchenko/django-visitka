from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название услуги')

    def __str__(self):
        return self.title

class Main(models.Model):
    txt = models.TextField(verbose_name='Текст на главной страницеи')


