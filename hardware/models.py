from django.db import models
from django.core.files.storage import FileSystemStorage

storage_configs = FileSystemStorage(location='/storage/configs')


class Types(models.Model):
    '''
    Тип устройства
    '''
    class Meta:
        verbose_name = "Тип устройства"
        verbose_name_plural = "Типы устройств"
    
    hard_type = models.CharField(max_length=30)

    def __str__(self):
        return self.hard_type


class Manufacturer(models.Model):
    '''
    Производитель, марка
    '''
    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"

    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Hard_Model(models.Model):
    '''
    Модель устройства
    '''
    class Meta:
        verbose_name = "Модель устройства"
        verbose_name_plural = "Модели устройств"

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    hard_type = models.ForeignKey(Types)

    def __str__(self):
        return self.name

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
        return self.region.name + ", " + self.name

class Ustr(models.Model):
    '''
    Содержит информацию о железке
    '''
    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"

    toch_dost = models.ForeignKey(
        Toch_dost,
        verbose_name = "Узел свзяи"
        )
    model = models.ForeignKey(
        Hard_Model,
        verbose_name = "Модель"
        )
    hard_type = models.ForeignKey(
        Types,
        verbose_name = "Тип"
        )
        
    ip = models.GenericIPAddressField()
    mask = models.GenericIPAddressField("Маска", default="255.255.255.224")
    login = models.CharField("Логин", max_length=20, default="admin")
    password = models.CharField("Пароль", max_length=200)
    config = models.FileField("Конфиг", storage=storage_configs, blank=True)
    
    def __str__(self):
        return self.toch_dost.region.name + ", " + self.toch_dost.name + " " + self.hard_type.hard_type + " " + self.model.name