from django.db import models

# Create your models here.
class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=11)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    def __str__(self):
        return self.nombres +" "+ self.apellidos

class Docente(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    def __str__(self):
        return self.nombres +" "+ self.apellidos

class Facultad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Especialidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    facultad = models.ForeignKey(Facultad)

    def __str__(self):
        return self.nombre

#CURSOS
class PlanEstudios(models.Model):
    id = models.AutoField(primary_key=True)
    anho = models.IntegerField()
    especialidad = models.ForeignKey(Especialidad)

    def __str__(self):
        return str(self.anho)

class Curso(models.Model):
    codigo = models.CharField(max_length=50,primary_key=True)
    nombre = models.CharField(max_length=50)
    plan = models.ForeignKey(PlanEstudios)

    def __str__(self):
        return self.nombre

#AULAS
class Local(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Aula(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    local = models.ForeignKey(Local)
    facultad = models.ForeignKey(Facultad)

    def __str__(self):
        return self.codigo