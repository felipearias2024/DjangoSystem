# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from app.models import *

# Create your views here.

#Function that render the first Template
def index(request):
    materias = Materia.objects.all()
    for a in materias:
        matri = Matricula.objects.filter(materia=a)
        cantidad = matri.count()
        a.cant_alumnos = cantidad
    return render(request,'index.html', {'cursos':materias})

def addNota(request):
    print "adding"
    if request.method == 'POST':
        student_id = request.POST['student_id']
        nota = request.POST['student_nota']
        materia_id = request.POST['materia_id']
        materia = Materia.objects.get(materia_id=materia_id)
        alumno = Alumno.objects.get(dni=student_id)
        print materia
        print alumno
        print nota
        new_nota = Notas(valor=nota, alumno=alumno, materia=materia)
        new_nota.save()
        return redirect('index')

def materia(request, pk):
    materia = Materia.objects.get(pk=pk)
    matriculados = Matricula.objects.filter(materia=materia)
    return render(request,'materias.html', {'materia':materia,'alumnos':matriculados})

def teachersData(request):
    teachers = Profesor.objects.all()
    return render(request,'preceptor.html', {'profesores':teachers})

def studentsData(request):
    students = Alumno.objects.all()
    return render(request, 'alumno.html', {'alumnos':students})

def findStudent(request, id_for):
    student = Alumno.objects.get(dni=id_for)
    return render(request, 'addNota.html', {'alumno':student})