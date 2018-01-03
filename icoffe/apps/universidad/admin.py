from django.contrib import admin

# Register your models here.
from apps.universidad.models import Alumno, Curso, Docente, Facultad, Especialidad, PlanEstudios, Local, Aula


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    pass

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    pass

@admin.register(Facultad)
class FacultadAdmin(admin.ModelAdmin):
    pass

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    pass

@admin.register(PlanEstudios)
class PlanEstudiosAdmin(admin.ModelAdmin):
    pass

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    pass

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    pass

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    pass

