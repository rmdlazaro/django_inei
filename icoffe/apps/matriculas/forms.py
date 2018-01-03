from django.forms.models import ModelForm

from apps.matriculas.models import Matricula


class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = ('alumno', 'curso', 'periodo')