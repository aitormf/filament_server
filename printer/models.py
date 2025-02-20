from django.db import models

# Create your models here.
class Printer(models.Model):
    model = models.CharField(max_length=200, verbose_name='model')
    name = models.CharField(max_length=200, verbose_name='name')
    created = models.DateTimeField(auto_now_add=True, verbose_name='creation date') # se actualiza al crear el objeto
    updated = models.DateTimeField(auto_now=True, verbose_name='edit date') # se actualiza en cada cambio

    class Meta:
        verbose_name = 'Printer'
        verbose_name_plural = 'Printers'
        ordering = ['created']

    def __str__(self):
        return self.name