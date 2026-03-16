from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_bodega'),
    path('logout/', views.logout_view, name='logout_bodega'),
    path('', views.panel_view, name='panel_bodega'),
]