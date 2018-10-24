from django import forms
from administracion.models import Clientes, Proyecto, Tema, colaborador_proyectos,version_estandar
from django.contrib.auth.models import Group,User
from  django.db.models import Q
STATUS_CHOICES = (('A','Activo',),('I','Inactivo',),)
STATUSPROYECTO_CHOICES = (('A','Activo',),('I','Inactivo',),('T','Terminado',))
RESPUESTA_CHOICES = (('SI', 'SI'), ('NO', 'NO',),)
PREGUNTA_CHOICES = (('SI', 'SI'), ('NO', 'NO',), ('PENDIENTE', 'PENDIENTE',), ('NTSRA', 'NTSRA',), ('N/A', 'N/A',),)
INSTRUCCION_CHOICES = (('1', 'SI'), ('0', 'NO',))
DATE_INPUT_FORMATS = ['%d/%m/%Y',]


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = [
            'nombre',
            'nit',
            'numero',
            'status',
        ]
        labels = {
            'nombre': 'Nombre Completo:',
            'nit':'Numero de Nit:',
            'numero': 'Numero de Telefono:',
            'status': 'Estatus:',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={"placeholder":"Ingrese nombre del cliente","class":"form-control input-sm","oninput":"validartexto(this.id)"}),
            'nit': forms.TextInput(attrs={"placeholder":"Ingrese nit del cliente","class":"form-control input-sm","oninput":"validartexto(this.id)"}),
            'numero': forms.TextInput(attrs={"placeholder": "+(502) 98765432", "class": "form-control input-sm",
                       "oninput": "validarnumero(this.id)"}),
            'status': forms.Select(choices=STATUS_CHOICES, attrs={"class":"form-control input-sm"}),
        }


class RolForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'name',
        ]
        labels = {
            'name': 'Rol',
        }
        widgets = {
            'name': forms.TextInput(attrs={"placeholder":"Example admin","class":"form-control input-sm"}),
        }



class UsuarioForm(forms.Form):
    id = forms.CharField(widget=forms.TextInput( attrs={"placeholder":"Ejemplo: jlopez","class":"form-control input-sm "}), max_length=30)
    username = forms.CharField(widget=forms.TextInput( attrs={"placeholder":"Ejemplo: jlopez","class":"form-control input-sm","oninput":"validartexto(this.id)","onchange":"validarnombreusuario(this.value)"}), max_length=30)
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Ingrese Nombre", "class": "form-control input-sm","oninput":"validartexto(this.id)"}), max_length=30)
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Ingrese Apellido", "class": "form-control input-sm","oninput":"validartexto(this.id)"}),  max_length=30)
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "ejemplo@dominio.com", "class": "form-control input-sm", "oninput":"validartexto(this.id)"}),  max_length=30)
    password = forms.CharField(widget=forms.PasswordInput( attrs={"placeholder": "Ingrese su contraseña ", "class": "form-control input-sm"}),  max_length=30)
    rol = forms.FileField(widget=forms.Select(attrs={"class": "form-control input-sm"}))
class editUsuarioForm(forms.Form):
    id = forms.CharField(widget=forms.TextInput( attrs={"placeholder":"type username","class":"form-control input-sm"}), max_length=30)
    username = forms.CharField(widget=forms.TextInput( attrs={"placeholder":"Ejemplo: jlopez","class":"form-control input-sm","oninput":"validartexto(this.id)"}), max_length=30)
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Ingrese Nombre", "class": "form-control input-sm","oninput":"validartexto(this.id)"}), max_length=30)
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Ingrese Apellido", "class": "form-control input-sm","oninput":"validartexto(this.id)"}),  max_length=30)
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "ejemplo@dominio.com", "class": "form-control input-sm"}),  max_length=30)
    rol = forms.FileField(widget=forms.Select(attrs={"class": "form-control input-sm"}))

class ProyectoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProyectoForm, self).__init__(*args, **kwargs)
        # Filter queryset fields to groups
        self.fields['usuario'].queryset = User.objects.filter(is_active=True)
        self.fields['cliente'].queryset = Clientes.objects.filter(status='A')

    class Meta:
        model = Proyecto
        fields = [
            'nombre',
            'usuario',
            'cliente',
            'fecha_ini',
            'fecha_fin',
            'estado',
            'version',
        ]

        labels = {
            'nombre': 'Nombre:',
            'usuario' : 'Usuario:',
            'cliente': 'Cliente:',
            'fecha_ini': 'Fecha inicialización:',
            'fecha_fin': 'Fecha finalización:',
            'estado': 'Estado',
            'version': 'Version Estandar',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={"placeholder":"type name for proyect","class":"form-control input-sm","oninput":"validartexto(this.id)"}),
            'usuario': forms.Select(attrs={"class":"form-control input-sm"}),
            'cliente': forms.Select(attrs={"class":"form-control input-sm"}),
            'fecha_ini': forms.DateInput(attrs={"placeholder":"AAAA-MM-DD","class":"form-control input-sm"}),
            'fecha_fin': forms.DateInput(attrs={"placeholder":"AAAA-MM-DD","class":"form-control input-sm"}),
            'estado': forms.Select(choices=STATUSPROYECTO_CHOICES, attrs={"class": "form-control input-sm", "onchange": "cambioestado(this.id)"}),
            'version': forms.Select(attrs={"class": "form-control input-sm"}),
        }

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = [
            'descripcion_tema',
            'descripcion',
        ]
        labels = {
            'descripcion_tema': 'Tema:',
            'descripcion': 'Descripción:',
        }
        widgets = {
            'descripcion_tema': forms.TextInput(attrs={"placeholder":"Escriba el tema","class":"form-control input-sm","oninput":"validartexto(this.id)"}),
            'descripcion': forms.Textarea(attrs={"placeholder": "Escriba descripción", "class": "form-control input-sm"}),
        }




class colaborador_proyectoform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(colaborador_proyectos, self).__init__(*args, **kwargs)
        # Filter queryset fields to groups
        self.fields['usuario'].queryset = User.objects.filter(is_active=True)
    class Meta:
        model = colaborador_proyectos
        fields = [
            'proyecto',
            'usuario',

        ]

        labels = {
            'proyecto': 'Proyecto:',
            'usuario':'Usuario',

        }

        widgets = {
            'proyecto': forms.Select(attrs={"class":"form-control input-sm"}),
            'usuario': forms.CheckboxSelectMultiple(),
        }
class version_estandarForm(forms.ModelForm):
    class Meta:
        model = version_estandar
        fields = [
            'nombre',
            'descripcion',

        ]

        labels = {
            'nombre':'Nombre:',
            'descripcion':'Descipción:',

        }

        widgets = {
            'nombre': forms.TextInput(attrs={"placeholder": "Ingresar nombre de versión", "class": "form-control input-sm","oninput":"validartexto(this.id)"}),
            'descripcion': forms.Textarea(attrs={"placeholder":"Ingresar descripción de version","class":"form-control input-sm"}),
        }