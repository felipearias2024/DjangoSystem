# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from app.models import *

# Create your views here.

#Function that render the first Template
def index(request):
    materias = Materia.objects.all()
    return render(request,'index.html', {'todos_los_cursos':materias})

def teachersData(request):
    teachers = Profesor.objects.all()
    return render(request,'preceptor.html', {'todos_los_profesores':teachers})

def studentsData(request):
    students = Alumno.objects.all()
    return render(request, 'alumno.html', {'todos_los_alumnos':students})

def addNota(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        student_nota = request.POST['student_nota']
        alumno = Alumno.objects.get(dni=student_id)
        nota = Nota(alumno = alumno, nota=student_nota)
        nota.save()
        return HttpResponse('{}'.format(alumno.apellido_a), '{}'.format(alumno.nombre_a))
    return HttpResponse("Solo podes acceder por POST !!")
