from django.contrib import admin

# Register your models here.
from apps.matriculas.models import CursoSeccion, PeriodoAcademico


@admin.register(CursoSeccion)
class CursoSeccionAdmin(admin.ModelAdmin):
    pass

@admin.register(PeriodoAcademico)
class PeriodoAcademicoAdmin(admin.ModelAdmin):
    pass