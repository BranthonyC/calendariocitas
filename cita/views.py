from django.shortcuts import render
from .models import Cita
from django.contrib import messages
from django.shortcuts import redirect
from users.models import Paciente

def appointment_update(request, pk):
    query = request.POST
    if Cita.objects.filter(id=pk).exists():
        try:
            cita = Cita.objects.get(id=pk)
            cita.fecha_cita=query['fecha_cita']
            cita.hora_cita=query['hora_cita']
            cita.comentario=query['comentario']

            cita.save()
        except:
            messages.add_message(request, messages.ERROR, 
            'ERROR: Ha ocurrido un error al actualizar la cita, intenta de nuevo.')
        else:
            messages.add_message(request, messages.INFO, 
            '¡Hemos guardado tus cambios!')
            
    return redirect('cita_detail', pk=pk)

def appointment_create(request, pk):
    query = request.POST
    try:
        cita = Cita(
            fecha_cita=query['fecha_cita'],
            hora_cita=query['hora_cita'],
            comentario=query['comentario'],
            paciente=Paciente.objects.get(id=pk),
        )
        cita.save()
    except:
        messages.add_message(request, messages.ERROR, 
        'ERROR: Ha ocurrido un error al crear la cita, intenta de nuevo.')
    else:
        messages.add_message(request, messages.INFO, 
        '¡Hemos guardado tus cambios!')
            
    return redirect('crear_cita', pk=pk, name=Paciente.objects.get(id=pk).nombre)