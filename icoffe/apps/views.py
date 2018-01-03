from django.shortcuts import render

# Create your views here.
def inicioView(request):
    template = 'index.html'
    return render(request, template, )