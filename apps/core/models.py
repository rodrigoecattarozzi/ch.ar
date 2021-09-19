from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.

class TimeModels(models.Model):
    creado = DateTimeField(auto_now_add=True,
                            verbose_name=u'Creado',
                            help_text=u'Fecha de creación')
    modificado = models.DateTimeField(auto_now_add=True,
                            verbose_name=u'Modificado',
                            help_text=u'Fecha de modificación')

    class Meta():
        abstract = True