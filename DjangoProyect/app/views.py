# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from app.models import *

# Create your views here.

#Function that render the first Template
def index(request):
    materias = Materia.objects.all()
    return render(request,'index.html', {'cursos':materias})

def addNota(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        student_nota = request.POST['student_nota']
        alumno = Alumno.objects.get(dni=student_id)
        nota = Nota(alumno = alumno, nota=student_nota)
        nota.save()
        return HttpResponse('{}'.format(alumno.apellido_a), '{}'.format(alumno.nombre_a))
    return HttpResponse("Solo podes acceder por POST !!")

def materias(request, pk):
    materia = Materia.objects.get(pk=pk)
    students = Alumno.objects.all().filter(materia_a=materia)
    teachers = Profesor.objects.all().filter(materia_p=materia)
    return render(request,'materias.html', {'materia':materia, 'profesores':teachers, 'alumnos':students})

def teachersData(request):
    teachers = Profesor.objects.all()
    return render(request,'preceptor.html', {'profesores':teachers})

def studentsData(request):
    students = Alumno.objects.all()
    return render(request, 'alumno.html', {'alumnos':students})

'''

function datos_formulario_guardia(url, alum) {
      //alert("soquetes");
      $.ajax({
        method: "POST",
        url: url,
        data: {
          csrfmiddlewaretoken: '{{ csrf_token }}'
        }
      })
        .done(function (data) {
        $("#datos").html(data);
        document.getElementById('id01').style.display='block';
      });
    };

'''