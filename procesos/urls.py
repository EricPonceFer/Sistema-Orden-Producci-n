from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('orden/', views.production_order_product, name='order_product'),
    path('reporte/', views.production_report, name='production_report')
]