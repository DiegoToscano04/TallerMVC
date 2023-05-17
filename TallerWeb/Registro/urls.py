from django.urls import path
from. import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro', views.registro, name='registro'),
    path('Libros', views.Libros, name='Libros'),
    path('Libros/crear', views.crear, name='crear'),
    path('Libros/editar', views.editar, name='editar'),
    path('eliminar/<int:id>',views.eliminar, name='eliminar'),
    path('eliminar/editar/<int:id>',views.editar, name='editar'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)