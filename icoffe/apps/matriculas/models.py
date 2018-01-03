from django.db import models

from apps.universidad.models import Alumno, Curso, Aula, Docente

class PeriodoAcademico(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=6)

    def __str__(self):
        return self.codigo

class CursoSeccion(models.Model):
    id = models.AutoField(primary_key=True)
    curso = models.ForeignKey(Curso)
    seccion = models.CharField(max_length=1)
    aula = models.ForeignKey(Aula)
    docente = models.ForeignKey(Docente)
    periodo = models.ForeignKey(PeriodoAcademico)

    def __str__(self):
        return self.curso.__str__()+" - "+self.seccion+" - "+self.periodo.__str__()

# Create your models here.
class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    alumno = models.ForeignKey(Alumno)
    curso = models.ForeignKey(CursoSeccion)
    periodo = models.ForeignKey(PeriodoAcademico)
    promedio_final = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, default=None)