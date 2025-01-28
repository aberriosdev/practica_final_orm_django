from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Laboratorio


def inicio(request):
    return render(request, 'inicio.html')

class LaboratorioListView(ListView):
    model = Laboratorio
    template_name = 'laboratorio/leer_laboratorio.html'
    context_object_name = 'laboratorios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        visitas = self.request.session.get('visitas', 0)
        self.request.session['visitas'] = visitas + 1
        context['request'] = self.request
        return context

    
class LaboratorioCreateView(CreateView):
    model = Laboratorio
    template_name = 'laboratorio/crear_laboratorio.html'
    fields = ['nombre', 'ciudad', 'pais']
    success_url = reverse_lazy('laboratorio_list') 


class LaboratorioUpdateView(UpdateView):
    model = Laboratorio
    fields = ['nombre', 'ciudad', 'pais']  
    template_name = 'laboratorio/editar_laboratorio.html'
    success_url = reverse_lazy('laboratorio_list') 


class LaboratorioDeleteView(DeleteView):
    model = Laboratorio
    template_name = 'laboratorio/eliminar_laboratorio.html'  
    success_url = reverse_lazy('laboratorio_list') 




