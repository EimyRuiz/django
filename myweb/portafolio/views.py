from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto, Habilidad
from .forms import ProyectoForm, HabilidadForm


def listarProyectos(request):
    proyectos =Proyecto.objects.all()
    return render (request, 'portafolio/listarProyectos.html', {'proyectos':proyectos})

def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listerProyecto')
        else:
            form = ProyectoForm()
        return render(request,'portafolio/formulario.html', {'form':form})
    

def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    form = ProyectoForm(request.POST or None, instance=proyecto)
    if form.is_valid():
        form.save()
        return redirect('listarProyecto')
    return render(request, 'portafolio/formulario.html',{'form':form})

def eliminar_proyecto(request,pk):
    proyecto = get_object_or_404(Proyecto,pk=pk)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('listarProyectos')
    return render(request, 'portafolio/confirmar_eliminar.html', {'proyecto':proyecto}) 



#Habilidad

def lista_habilidades(request):
    habilidades = Habilidad.objects.all()
    return render(request, 'protafolio/lista_habilidades.html', {'habilidades': habilidades})


def crear_habilidad(request):
    if request.method == 'POST':
        form = HabilidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_habilidades')
        else:
            form = ProyectoForm()
        return render(request, 'portafolio/formulario.html', {form: form})
    
def editar_habilidad(request, pk):
    proyecto = get_object_or_404(Habilidad, pk=pk)
    form = HabilidadForm(request.POST or None, instance=proyecto)
    if form.is_valid():
        form.save()
        return redirect('listar_habilidades')
    return render(request, 'portafolio/formulario.html',{'form':form})

def eliminar_habilidad(request,pk):
    habilidad = get_object_or_404(Habilidad,pk=pk)
    if request.method == 'POST':
        habilidad.delete()
        return redirect('listar_habilidades')
    return render(request, 'portafolio/confirmar_eliminar.html', {'habilidad': habilidad}) 

# Create your views here.


