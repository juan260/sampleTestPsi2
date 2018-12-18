# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#import os
#os.environ.setdefault('DJANGO_SETTINGS_MODULE',
#      'proyecto.settings')
# Create your models here.

class estanteria(models.Model):
    ubicacion=models.CharField(max_length=255)

    def __str__(self):
        return self.ubicacion
    def __unicode__(self):
        return self.ubicacion

class objeto(models.Model):
    nombreO=models.CharField(max_length=255)

    def __str__(self):
        return self.nombreO
    def __unicode__(self):
        return self.nombreO

class stock(models.Model):
    estanteria_id=models.ForeignKey(estanteria, on_delete=models.CASCADE, null=True, blank=True)
    objeto_id=models.ForeignKey(objeto, on_delete=models.CASCADE, null=True, blank=True)
    numerounidades=models.IntegerField(null=True)

    def __str__(self):
        return str(self.estanteria_id) + " " + str(self.objeto_id)
    def __unicode__(self):
        return str(self.estanteria_id) + " " + str(self.objeto_id)