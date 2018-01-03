
from django.shortcuts import render

# Create your views here.
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from apps.matriculas.forms import MatriculaForm
from apps.matriculas.models import Matricula


def MatriculaInicioView(request):
    template = 'matriculas/index.html'
    return render(request, template, )

class MatriculaLista(ListView):
    template_name = 'matriculas/lista.html'
    model = Matricula
    context_object_name = 'matriculas'

    #def get_context_data(self, **kwargs):
    #    context = super(MatriculaLista, self).get_context_data(**kwargs)
    #    return context

    #def get_queryset(self):
    #    return Matricula.objects.all()


class MatriculaView(FormView):
    template_name = 'matriculas/matricular.html'
    form_class = MatriculaForm
    success_url = reverse_lazy('matriculas:ok')

    def form_valid(self, form):
        form.save()
        return super(MatriculaView, self).form_valid(form)

class MatriculadoView(TemplateView):
    template_name = 'matriculas/ok.html'