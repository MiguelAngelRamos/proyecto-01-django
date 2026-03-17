from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_bodega'),
    path('logout/', views.logout_view, name='logout_bodega'),
    path('', views.panel_bodega, name='panel_bodega'),  ## 127.0.0.1:8000/bodega/
]

# http://127.0.0.1:8000/bodega/login/