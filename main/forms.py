from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField( widget=forms.TextInput(attrs={"placeholder":"Escriba nombre de usuario","class":"form-control input-sm"}))
    password = forms.CharField( widget=forms.PasswordInput(attrs={"placeholder":"Escriba su contraseña","class":"form-control input-sm"}))

class SeleccionarProyectoForm(forms.Form):
    proyecto = forms.FileField( widget=forms.Select(attrs={"class":"form-control input-sm"}))

class ChangePasswordForm(forms.Form):
    oldpassword  = forms.CharField(widget=forms.PasswordInput( attrs={"placeholder": "Ingrese su contrseña actual ", "class": "form-control input-sm", "name":"oldpassword"}),  max_length=30)
    newpassword = forms.CharField(widget=forms.PasswordInput( attrs={"placeholder": "Ingrese nueva contraseña ", "class": "form-control input-sm", "name":"newpassword"}),  max_length=30)
    confirmpassword = forms.CharField(widget=forms.PasswordInput( attrs={"placeholder": "Repita su nueva contraseña ", "class": "form-control input-sm","name":"confirmpassword"}),  max_length=30)
class AxesCaptchaForm(forms.Form):
    captcha = CaptchaField()