from django.urls import path
from .views import home,form_producto

urlpatterns =[  #esto el indica a la maquina los path que vamos a usar
    path('',home,name="home"),
    path('form_producto',form_producto,name='form_producto'),   
]