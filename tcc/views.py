from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from . import forms
from .models import TCC, Autor, Curso, Orientador


def autenticar_model(model):
    if model.lower() not in ['tcc', 'autor', 'orientador', 'curso']:
        raise Http404('Model not exist')

def home(request):
    tccs = TCC.objects.all()
    return render(request, 'index.html', context={'consultas': tccs})

@login_required
def tcc(request,id):
    tcc_detail = get_object_or_404(TCC, id=id)
    return render(request, 'tcc_individual.html', context={'tcc': tcc_detail})

@login_required
def criar(request, model):
    autenticar_model(model)
    form_model = eval(f'forms.{model.capitalize()}Form')
    if request.method == "POST": 
        form = form_model(request.POST, request.FILES)  
        if form.is_valid():    
            form.save() 
            model = form.instance
            return redirect('tcc:home')  

    else:  
        form = form_model()  
    return render(request,'criar.html',{'form':form, 'model': model.capitalize()})  

@login_required
def listar(request, model):
    autenticar_model(model)
    if model.lower() == 'tcc':
        class_model = eval('TCC')
    else:
        class_model = eval(f'{model.capitalize()}')

    consultas = class_model.objects.all()
    return render(request, f'listar/{model.lower()}.html', {'consultas':consultas})

@login_required
def atualizar(request, model, id):
    autenticar_model(model)
    if model.lower() == 'tcc':
        class_model = eval('TCC')
    else:
        class_model = eval(f'{model.capitalize()}')
    class_form = eval(f'forms.{model.capitalize()}Form')

    consultas = class_model.objects.get(id=id)
    a = consultas.__doc__.split('(')
    a = ''.join(a[1])
    a = a.replace(' ','')
    a = a[:-1].split(',')
    tupla1 = tuple(a)
    lista = []
    [lista.append(getattr(consultas,key)) for key in a]
    dic = dict(zip(tupla1, lista))

    form = class_form(initial=dic)
    if request.method == "POST":  
        form = class_form(request.POST, instance=consultas)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('tcc:home')  
            except Exception as e: 
                pass    
    return render(request,'atualizar.html',{'form':form})

@login_required
def deletar(request, model, id):
    autenticar_model(model)
    if model.lower() == 'tcc':
        class_model = eval('TCC')
    else:
        class_model = eval(f'{model.capitalize()}')

    book = class_model.objects.get(id=id)
    try:
        book.delete()
    except:
        pass
    return redirect('tcc:home')
