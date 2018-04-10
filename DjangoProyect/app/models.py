# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.conf import settings

class Materia(models.Model):
    materia_id = models.IntegerField('Clave de materia', primary_key=True)
    nombre_m = models.CharField('Nombre de la materia', max_length=128)

    def __str__(self):
        return 'Materia: {}'.format(self.nombre_m)


class Profesor(models.Model):
    nombre_p = models.CharField('Nombre del Profesor', max_length = 128)
    apellido_p = models.CharField('Apellido del Profesor', max_length = 128)
    dni = models.IntegerField('Clave de profesor', primary_key=True)
    materia_p = models.ForeignKey(Materia)

    def __str__(self):
        return 'Profesor: {} {} | asignatura: {}'.format(self.nombre_p, self.apellido_p, self.materia_p)
    
class Alumno(models.Model):
    nombre_a = models.CharField('Nombre del Alumno', max_length = 128)
    apellido_a = models.CharField('Apellido del Alumno', max_length = 128)
    dni = models.IntegerField('Clave de Alumno', primary_key=True)
    
    def __str__(self):
        return 'Alumno: {} {}'.format(self.nombre_a, self.apellido_a)


class Notas(models.Model):
    valor = models.IntegerField('Valor de la nota')
    alumno = models.ForeignKey(Alumno)
    materia = models.ForeignKey(Materia)

    def __str__(self):
        return 'Nota de {}: {} en {}'.format(self.alumno.nombre_a, self.valor, self.materia.nombre_m)
    
class Matricula(models.Model):
    materia = models.ForeignKey(Materia)
    alumno = models.ForeignKey(Alumno)

    def __str__(self):
        return 'El alumno {} asiste a {} '.format(self.alumno.nombre_a, self.materia.nombre_m)
        