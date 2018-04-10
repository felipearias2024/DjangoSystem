# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.models import *

# Create your views here.

#Function that render the first Template
def index(request):
    materias = Materia.objects.all()
    return render(request,'index.html', {'cursos':materias})

def addNota(request):
    print "adding"
    if request.method == 'POST':
        student_id = request.POST['student_id']
        nota = request.POST['student_nota']
        print nota
        alumno = Alumno.objects.get(dni=student_id)
        new_nota = Notas(alumno=alumno, valor=nota)
        new_nota.save()
    return redirect('index')

def materia(request, pk):
    materia = Materia.objects.get(pk=pk)
    matriculados = Matricula.objects.get(materia=materia)
    students = Alumno.objects.filter(dni=matriculados.alumno.dni)
    teachers = Profesor.objects.all().filter(materia_p=materia)
    return render(request,'materias.html', {'materia':materia,'alumnos':students, 'profesores':teachers})

def teachersData(request):
    teachers = Profesor.objects.all()
    return render(request,'preceptor.html', {'profesores':teachers})

def studentsData(request):
    students = Alumno.objects.all()
    return render(request, 'alumno.html', {'alumnos':students})

def findStudent(request, id_for):
    student = Alumno.objects.get(dni=id_for)
    return render(request, 'addNota.html', {'alumno':student})