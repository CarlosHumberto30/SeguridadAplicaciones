from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import LoginForm, SeleccionarProyectoForm, ChangePasswordForm, AxesCaptchaForm
from administracion.models import Proyecto,colaborador_proyectos
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from  django.contrib.auth.models import User,Group,Permission
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from axes.decorators import axes_dispatch
from django.contrib.auth.signals import user_logged_in,\
    user_logged_out,\
    user_login_failed
from django.views import View
from axes.utils import *
from ipware import get_client_ip

@login_required
def home(request):
    return render(
        request,
        'main/home.html',
        {}
    )

@method_decorator(axes_dispatch, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class Login(View):

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('main:home')
        else:
            message = None
            form = LoginForm()
            return render(request, 'main/login.html', {'message': message, 'form': form})

    def post(self, request, *args, **kwargs):
        message = None
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    prueba = user.id
                    request.session['usuario'] = prueba
                    request.session['nombreusuario'] = username
                    user_logged_in.send(
                        sender=User,
                        request=request,
                        user=user,
                    )
                    return render(
                        request,
                        'main/home.html',
                        {}
                    )
                else:
                    messages.info(request, 'Autenticasion no exitosa vuelva intentarlo!')
                    user_login_failed.send(
                        sender=User,
                        request=request,
                        credentials={
                            'username': form.cleaned_data.get('username')
                        },
                    )
            else:

                user_login_failed.send(
                    sender=User,
                    request=request,
                    credentials={
                        'username': form.cleaned_data.get('username')
                    }
                )
                messages.warning(request, 'Usuario o Contraseña no validos!')
        else:
            user_login_failed.send(
                sender=User,
                request=request,
                credentials={
                    'username': form.cleaned_data.get('username')
                }
            )
        return render(request, 'main/login.html', {'message': message, 'form': form})


def locked_out(request):
    if request.POST:
        form = AxesCaptchaForm(request.POST)
        if form.is_valid():

            ip = get_client_ip(request)
            reset(ip=request.META['REMOTE_ADDR'])
            return redirect('main:login')
    else:
        form = AxesCaptchaForm()


    return render(request, 'main/locked_out.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('main:login')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Su contraseña a sido cambiada exitosa mente !!')
            return redirect('main:home')
        else:
            messages.error(request, 'Por favor, corrija el error a continuación.')
    else:
       form = PasswordChangeForm(request.user)
       #form = ChangePasswordForm()
    return render(request, 'main/changepassword.html', {
        'form': form
    })



@login_required
def seleccionar_proy(request,next):
    listaproyectos=[]
    if request.method =='POST':
            proyecto = request.POST['proyecto']
            nombreproyecto=Proyecto.objects.get(id=proyecto)
            request.session['proyecto']=proyecto
            request.session['nombreproyecto'] =nombreproyecto.nombre
           # Actualizar_Cuestionarios(proyecto)
            redirect_to = request.POST.get('next', '')
            messages.success(request, 'Proyecto seleccionado y actualizado con EXITO!')
            if redirect_to == 'ReporteFEl:cuestionariogap' or redirect_to == 'ReporteFEl:graficas' or redirect_to == 'ReporteFEl:cuestionarioseguimiento'\
                    or redirect_to == 'ReporteFEl:graficasseguimiento' or redirect_to == 'ReporteFEl:cuestionarioauditoria':
                return redirect(redirect_to,'1')
            else:
               return redirect(redirect_to)
    else:
        usuario = request.session['usuario']
        proyectos = Proyecto.objects.filter(usuario=usuario,estado='A')
        for proy in proyectos:
            listaproyectos.append(proy)
        proyectoscolaboracion = colaborador_proyectos.objects.filter(usuario=usuario)
        for proycolabora in  proyectoscolaboracion:
            if proycolabora.proyecto.estado == 'A':
                 listaproyectos.append(proycolabora.proyecto)
        return render(request, 'main/selecionar_proyecto.html', {'proyectos':listaproyectos,'next':next})


