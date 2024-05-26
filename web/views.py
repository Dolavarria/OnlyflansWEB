from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Flan,ContactForm
from .forms import ContactFormModelForm


def indice(request):
    flanes = Flan.objects.all()
    flanes_privados = Flan.objects.filter(is_private=True)
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

def about(request):
    return render(request, 'about.html', {})


def default_map(request):
    return render(request, 'ubicacion.html', {})

@login_required
def welcome(request):
    flanes = Flan.objects.all()
    flanes_privados = Flan.objects.filter(is_private=True)
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'welcome.html', {'flanes':flanes_privados})

def contacto(request):
    if request.method=='POST':
        #Crear instancia del formulario con los datos del request
        form=ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form=ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/contacto/exito/')
    else:
        form=ContactFormModelForm()
    return render(request, 'contacto.html', {'form': form})

def contacto_exito(request):
    return render(request, 'contactoexito.html', {})
