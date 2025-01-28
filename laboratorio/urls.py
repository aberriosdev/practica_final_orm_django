from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'), 
    path('list/', views.LaboratorioListView.as_view(), name='laboratorio_list'),
    path('crear/', views.LaboratorioCreateView.as_view(), name='laboratorio_create'),  
    path('<int:pk>/editar/', views.LaboratorioUpdateView.as_view(), name='laboratorio_edit'),  
    path('<int:pk>/eliminar/', views.LaboratorioDeleteView.as_view(), name='laboratorio_delete'), 
]
