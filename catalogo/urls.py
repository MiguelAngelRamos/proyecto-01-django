from django.urls import path
from . import views
urlpatterns = [ 
    path('', views.lista_productos, name='lista_productos'),
]


## 127.0.0.1:8000/lista/