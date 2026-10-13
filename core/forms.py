
# forms: herramientas para crear formularios de Django
from django import forms

# ValidationError: permite mostrar errores de validación
from django.core.exceptions import ValidationError

# Importamos el modelo Servicio
from .models import Servicio


# Formulario generado a partir del modelo Servicio
class ServicioForm(forms.ModelForm):

    class Meta:
        # Modelo del que se generan los campos
        model = Servicio

        # Campos que aparecerán en el formulario
        fields = ['titulo', 'descripcion', 'precio', 'categoria']

    # Validación personalizada del precio
    def clean_precio(self):
        # Obtenemos el precio introducido
        precio = self.cleaned_data['precio']

        # El precio debe ser mayor que cero
        if precio <= 0:
            raise ValidationError('El precio debe ser mayor a 0.')

        # Devolvemos el precio validado
        return precio
