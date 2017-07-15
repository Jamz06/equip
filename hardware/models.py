from django.db import models
from django.core.files.storage import FileSystemStorage

storage_configs = FileSystemStorage(location='/storage/configs')


class Types(models.Model):
    '''
    Тип устройства
    '''

    hard_type = models.CharField(max_length=30)

class Manufacturer(models.Model):
    '''
    Производитель, марка
    '''
    name = models.CharField(max_length=32)


class Hard_Model(models.Model):
    '''
    Модель устройства
    '''
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    hard_type = models.ForeignKey(Types)


class Region(models.Model):
    '''
    Регион точки доаступа
    '''
    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"
    
    
    name = models.CharField("Регион", max_length=60)
    def __str__(self):
        return self.name

class Toch_dost(models.Model):
    '''
    Точка доступа
    '''
    class Meta:
        verbose_name = "Точка доступа"
        verbose_name_plural = "Точки доступа"
    
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        verbose_name = "Регион"
        )

    name = models.CharField("Узел связи", max_length=32)
    def __str__(self):
        # return self.region + ", " + self.name
        return self.name

class Hardware(models.Model):
    '''
    Содержит информацию о железке
    '''
    toch_dost = models.ForeignKey(Toch_dost)
    model = models.ForeignKey(Hard_Model)
    hard_type = models.ForeignKey(Types)
    ip = models.CharField(max_length=16)
    mask = models.CharField(max_length=16)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=200)
    config = models.FileField(storage=storage_configs)
    
    