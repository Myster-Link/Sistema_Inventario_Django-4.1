from django import forms
from .models import CategoriasProducto, Proveedor


class editar_producto(forms.Form):

    

    choices_categoria = (
        ('1', 'camaras')
    )

    choices_proveedor = (
        ('1', 'DAHUA')
    )

    nombre = forms.CharField(label='Nombre:', max_length=30)
    codigo = forms.CharField(label='Codigo:', max_length=20)
    categoria = forms.ChoiceField(widget=forms.Select, choices=choices_categoria)
    proveedor = forms.ChoiceField(widget=forms.Select, choices=choices_proveedor)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'name':'descripcion', 'rows':'5', 'cols':'30'}))
    stock = forms.FloatField(label='Stock:')
    precio = forms.FloatField(label='Precio:')
    