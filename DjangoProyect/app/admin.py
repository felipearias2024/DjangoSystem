# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Alumno)
admin.site.register(Materia)
admin.site.register(Profesor)
admin.site.register(Notas)
admin.site.register(Matricula)