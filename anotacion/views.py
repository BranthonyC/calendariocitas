from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Anotacion
from cita.models import Cita
from .forms import CardAnotacion_form
# Create your views here.

def listado_anotaciones(request):
    anotaciones=Anotacion.objects.all()
    data={
        'lista_anotaciones':anotaciones
    }
    return render(request, 'anotacion/listado_anotaciones.html',data)

def modificar_anotacion(request,id):
    anotacion=Anotacion.objects.get(no_anotacion=id) 
    data = {
        'form': CardAnotacion_form(instance=anotacion)
    }
    if request.method=="POST":
        formulario=CardAnotacion_form(data=request.POST, instance=anotacion)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Anotacion modificada correctamente"
            data['form'] = formulario
    return render(request, 'anotacion/modificar_anotacion.html',data)
from django.views.generic import CreateView
from anotacion.models import Anotacion
from anotacion.forms import AnotacionForm
from django.urls import reverse_lazy
from datetime import datetime 

# Create your views here.
def eliminar_anotacion(request,id):
    anotacion = Anotacion.objects.get(no_anotacion=id)
    anotacion.delete()
    return redirect(to="listado_anotaciones")

def crear_anotacion(request):
    return render(request,'anotacion/index.html')


#class annotationCreate(CreateView):
#    model = Anotacion
#    form_class = AnotacionForm
#    template_name = 'anotacion/anotacion_form.html'

#    def post(self, request, *args, **kwargs):
#        form = self.form_class(request.POST)
#        if form.is_valid():
#            return HttpResponseRedirect('/success/')
#        return render(request, self.template_name, {'form': form})

def annotationCreate(request, id):
    #print(id)
    #return HttpResponseRedirect(reverse('citas'))
    #return render(request,'citas/cita_detail.html')
    
    form = AnotacionForm(request.POST)
    
    if form.is_valid():
        anotacion = form.save(commit=False)
        fecha = datetime.now()
        anotacion.fecha_hora = fecha
        cita = Cita.objects.get(id=id)
        anotacion.id_cita = cita
        anotacion.save()

    return HttpResponseRedirect('/citas/'+id)
