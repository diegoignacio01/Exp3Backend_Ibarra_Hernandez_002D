from django import forms    
from django.forms import ModelForm
from .models import Producto

class ProductoForm(ModelForm):
    class Meta:
        model= Producto
        fields = ['idProducto','marca','modelo','nombre']
        labels={
            'id del producto':'Ingrese el id del producto',
            'marca':'Ingresar marca del producto',
            'modelo':'Ingrese modelo del producto',
        }
        widgets={
            'id del producto':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'id del producto',
                    'id':'id producto',

                }
            ),
            'marca':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'marca del producto',
                    'id':'marca',
                }
            ),
            'nombre':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'nombre del producto',
                    'id':'nombre',
                }
            ),
            'modelo':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'modelo del producto',
                    'id':'modelo',
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )
        }