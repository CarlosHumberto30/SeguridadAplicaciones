from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from django.forms.models import inlineformset_factory
from administracion.forms import ClienteForm,  RolForm, UsuarioForm,\
                                ProyectoForm, TemaForm, editUsuarioForm,colaborador_proyectoform, version_estandarForm
from administracion.models import Clientes, Proyecto, Tema,  colaborador_proyectos,version_estandar

from  django.contrib.auth.models import User,Group,Permission
from  django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.http import JsonResponse
import json
from django.template.loader import render_to_string
from django.http import HttpResponse
@login_required
def listarcliente(request):
    clientes = Clientes.objects.filter(Q(status='A')|Q(status='I'))
    lista = []
    for cliente in clientes:
        if cliente.status == 'A':
            cliente.status = 'Activo'
        else:
            cliente.status='Inactivo'
        lista.append(cliente)
    return render(request, 'administracion/Cliente/listarcliente.html', {'clientes': clientes})

@login_required
@permission_required('administracion.add_clientes')
def crearcliente(request):
    cliente = Clientes()
    if request.method == 'POST':
        form1 = ClienteForm(request.POST, instance=cliente, prefix='form1')
        if form1.is_valid():
            if form1.save():
                messages.success(request, 'Cliente creado con éxito!')
                return redirect('administracion:listarcliente')
        else:
            messages.warning(request, 'Verifique los campos ingresados')
    else:
        form1 = ClienteForm(prefix='form1')
    return render(request, 'administracion/Cliente/agregarcliente.html', {'form1': form1})

@login_required
@permission_required('administracion.change_clientes')
def actualizarcliente(request, pk):
    cliente = Clientes.objects.get(pk=pk)
    if request.method == 'POST':
        form1 = ClienteForm(request.POST, instance=cliente, prefix='form1')

        if form1.is_valid():
            if form1.save():
                messages.success(request, 'Cliente actualizado con éxito!')
                return redirect('administracion:listarcliente')
            else:
                messages.warning(request, 'datos no guardados!')

    else:
        form1 = ClienteForm(instance=cliente, prefix='form1')
    return render(request, 'administracion/Cliente/editarcliente.html', {'form1': form1})


class eliminarcliente(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = Clientes
    template_name = 'administracion/Cliente/eliminarcliente.html'
    success_url = reverse_lazy('administracion:listarcliente')
    permission_required = ('administracion.delete_clientes')

    def get(self, request, *args, **kwargs):
        if Clientes.objects.filter(pk=kwargs['pk']).exists():
            cliente = Clientes.objects.get(pk=kwargs['pk'])
            return render(request, self.template_name, {'object': cliente})
        else:
            return redirect('administracion:listarcliente')
    def post(self, request, *args, **kwargs):
        if Clientes.objects.filter(pk=kwargs['pk']).exists():
            cliente = Clientes.objects.get(pk=kwargs['pk'])
            cliente.status = 'E'
            cliente.save()
            proyectos = Proyecto.objects.filter(cliente=cliente)
            for proyecto in proyectos:
                proyecto.estado='E'
                proyecto.save()
        return redirect(self.success_url)



def crearrol(request):
    if request.method =='POST':
        forms = RolForm(request.POST)
        if forms.is_valid:
            nombre = request.POST['name']
            if Group.objects.create(name=nombre):
                messages.success(request, 'Rol creado con éxito!')
                return redirect('administracion:listarrol')
        else:
            messages.warning(request, 'Verifique los campos ingresados!')
    else:
        forms = RolForm()
    return render(request, 'administracion/RolUsuario/agregar_rol.html', {'form': forms}, )

class listarrol(LoginRequiredMixin,ListView):
    model = Group
    template_name = 'administracion/RolUsuario/listar_rol.html'

class actualizarrol(LoginRequiredMixin,UpdateView):
    model = Group
    form_class = RolForm
    template_name = 'administracion/RolUsuario/editar_rol.html'
    success_url = reverse_lazy('administracion:listarrol')

class eliminarrol(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'administracion/RolUsuario/eliminar_rol.html'
    success_url = reverse_lazy('administracion:listarrol')

@login_required
@permission_required('auth.add_user')
def crearusuario(request):
    #verifica si ya existe un rol si no crea el rol Administrador, QSA y le agrega los permisos
    rol = Group.objects.filter(name='Auditor')
    if not rol:
      permisos = Permission.objects.all()
      grupoadministracion =  Group.objects.get(name='Administrador')
      grupoauditor =  Group.objects.create(name='Auditor')
      grupocliente = Group.objects.create(name='Cliente')
      for permiso in permisos:
          grupoadministracion.permissions.add(permiso)
          if permiso.codename == 'add_proyecto':
              grupoauditor.permissions.add(permiso)
          if permiso.codename == 'change_proyecto':
              grupoauditor.permissions.add(permiso)
          if permiso.codename == 'delete_proyecto':
              grupoauditor.permissions.add(permiso)

    if request.method == 'POST':
            forms = UsuarioForm(request.POST)
            if forms.is_valid:
                username = request.POST['username']
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                email = request.POST['email']
                password = request.POST['password']
                rol = request.POST['rol']

                user = User.objects.create_user(username=username, email=email, password=password)
                user.first_name = first_name
                user.last_name = last_name
                user.is_active = True
                user.groups.add(rol)
                user.save()
                messages.success(request, 'Usuario creado con éxito!')
                return redirect('administracion:listarusuario')
            else:
                messages.warning(request, 'Verifique los campos ingresados')
    else:
        forms = UsuarioForm()
        rol = Group.objects.all()
    return render(request, 'administracion/Usuario/crear_usuario.html', {'forms': forms,'groups':rol})

class listarusuario(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    model = User
    template_name = 'administracion/Usuario/listar_usuario.html'
    permission_required = ('auth.delete_user')
    def get(self, request, *args, **kwargs):
        object=User.objects.filter(is_active=True)
        return render(request, self.template_name, {'object_list': object})

@login_required
@permission_required('auth.change_user')
def actualizarusuario(request, pk):
    usuario = User.objects.get(pk=pk)
    if usuario.is_active == False:
        return redirect('administracion:listarusuario')
    user = User.get_username(usuario)
    if request.method == 'POST':
            forms = editUsuarioForm(request.POST)
            if forms.is_valid:
                id = request.POST['id']
                username = request.POST['username']
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                email = request.POST['email']
                rol = request.POST['rol']
                password = request.POST['password']
                usuario = User.objects.get(pk=id)
                usuario.groups.clear()
                usuario.first_name=first_name
                usuario.last_name=last_name
                usuario.email=email
                usuario.groups.add(rol)
                if len(password) > 0:
                    usuario.set_password(password)
                usuario.save()
                messages.success(request, 'Usuario actualizado con éxito!')
                return redirect('administracion:listarusuario')
            else:
                return redirect('administracion:editarusuario')
    else:

        forms = editUsuarioForm()
        forms.initial={'id':usuario.id,'username':usuario.username,'first_name':usuario.first_name, 'last_name':usuario.last_name,'email':usuario.email}
        rol= usuario.groups.all()[0]

        groups = Group.objects.all()
    return render(request, 'administracion/Usuario/editar_usuario.html', {'forms': forms,'groups':groups,'rol':rol})

class eliminarusuario(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = User
    template_name = 'administracion/Usuario/eliminar_usuario.html'
    success_url = reverse_lazy('administracion:listarusuario')
    permission_required = ('auth.delete_user')

    def get(self, request, *args, **kwargs):
        if User.objects.filter(pk=kwargs['pk']).exists():
            usuario = User.objects.get(pk=kwargs['pk'])
            return render(request, self.template_name, {'object': usuario})
        else:
            return redirect('administracion:listarusuario')

    def post(self, request, *args, **kwargs):
        if User.objects.filter(pk=kwargs['pk']).exists():
            user = User.objects.get(pk=kwargs['pk'])
            user.is_active = False
            user.save()
            return redirect(self.success_url)
@login_required
@permission_required('administracion.add_proyecto')
def crearproyecto(request):
    rol=''
    if request.method =='POST':
        forms = ProyectoForm(request.POST,instance=Proyecto())
        if forms.is_valid():
            # carga informacion para los cuestionaro ReporteFEl,SEGUIMIENTO Y AUDITORIA mandando la instancia el proyecto que se está creando.
            forms.save()
            messages.success(request, 'Proyecto creado con éxito!')
            return redirect('administracion:listarproyecto')
        else:
            messages.warning(request, 'Verifique los campos ingresados')
    else:
        forms = ProyectoForm(instance=Proyecto())
        for g in request.user.groups.all():
            rol = g.name

    return render(request, 'administracion/Proyecto/crearproyecto.html', {'form': forms,'Rol': rol})

@login_required
@permission_required('administracion.change_proyecto')
def listarproyecto(request):
    usuario = request.session['usuario']
    proyectos=[]
    for group in request.user.groups.all():
        if group.name =='Auditor':
           proyectos = Proyecto.objects.filter(usuario=usuario,estado='A')
           proyectosinactivos = Proyecto.objects.filter(usuario=usuario, estado='I')
           proyectosterminados = Proyecto.objects.filter(usuario=usuario, estado='T')
        else:
            proyectos = Proyecto.objects.filter(estado='A')
            proyectosinactivos = Proyecto.objects.filter(estado='I')
            proyectosterminados = Proyecto.objects.filter(estado='T')
    return render(request, 'administracion/Proyecto/listar_proyecto.html', {'proyectos': proyectos,'proyectosinactivos': proyectosinactivos,'proyectosterminados': proyectosterminados})


class actualizarproyecto(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'administracion/Proyecto/editarproyecto.html'
    success_url = reverse_lazy('administracion:listarproyecto')
    permission_required = ('administracion.change_proyecto')
    def get(self, request, *args, **kwargs):
        proyecto= Proyecto.objects.get(pk=kwargs['pk'])
        if proyecto.usuario.pk == request.user.pk or request.user.groups.filter(name='Administrador').exists():
            if proyecto.estado == 'E':
                return redirect('administracion:listarproyecto')
            forms = ProyectoForm(instance=proyecto)
            for g in request.user.groups.all():
                rol = g.name
            congelados= ""
            return render(request, self.template_name, {'form': forms,'Rol': rol,'cuestionarioscongelados':congelados})
        else:
            return redirect('administracion:listarproyecto')
class eliminarproyecto(LoginRequiredMixin,PermissionRequiredMixin,View):
    model = Proyecto
    template_name = 'administracion/Proyecto/eliminarproyecto.html'
    success_url = reverse_lazy('administracion:listarproyecto')
    permission_required = ('administracion.delete_proyecto')
    def get(self, request, *args, **kwargs):
        if Proyecto.objects.filter(pk=kwargs['pk']).exists():
            proyecto = Proyecto.objects.get(pk=kwargs['pk'])
            if proyecto.usuario.pk == request.user.pk or request.user.groups.filter(name='Administrador').exists():
                return render(request, self.template_name, {'object': proyecto})
            else:
                return redirect('administracion:listarproyecto')
        else:
            return redirect('administracion:listarproyecto')

    def post(self, request, *args, **kwargs):

        if Proyecto.objects.filter(pk=kwargs['pk']).exists():
            proyecto = Proyecto.objects.get(pk=kwargs['pk'])
            proyecto.estado='E'
            proyecto.save()
            return redirect(self.success_url)



class creartema(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model = Tema
    form_class = TemaForm
    template_nameajax = 'administracion/Tema/modal_agregar_tema.html'
    template_name = 'administracion/Tema/agregar_tema.html'
    success_url = reverse_lazy('administracion:listartema')
    permission_required = ('administracion.add_tema')

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return render(request, self.template_nameajax, {'form': self.form_class})
        else:
            return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = TemaForm(request.POST)
        if form.is_valid():
            tema = form.save()
        if request.is_ajax():

            data = {
                'tema_id': tema.pk,
                'tema_descripcion': tema.descripcion_tema
            }
            return JsonResponse(data)
        else:
            return redirect(self.success_url)



class listartema(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model = Tema
    template_name = 'administracion/Tema/listar_tema.html'
    permission_required = ('administracion.change_tema')


class actualizartema(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = Tema
    form_class = TemaForm
    template_name = 'administracion/Tema/editar_tema.html'
    success_url = reverse_lazy('administracion:listartema')
    permission_required = ('administracion.change_tema')


class eliminartema(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = Tema
    template_name = 'administracion/Tema/eliminartema.html'
    success_url = reverse_lazy('administracion:listartema')
    permission_required = ('administracion.delete_tema')
    def get(self, request, *args, **kwargs):
        if Tema.objects.filter(pk=kwargs['pk']).exists():
            tema = Tema.objects.get(pk=kwargs['pk'])
            return render(request, self.template_name, {'object': tema})
        else:
            return redirect('administracion:listartema')


# mantenimiento version
class crearversion(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model = version_estandar
    form_class = version_estandarForm
    template_nameajax = 'administracion/version/modal_agregar_version.html'
    template_name = 'administracion/version/agregar_version.html'
    permission_required = ('administracion.add_version_estandar')
    success_url = reverse_lazy('administracion:listarversion')

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return render(request, self.template_nameajax, {'form': self.form_class})
        else:
            return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = version_estandarForm(request.POST)
        if form.is_valid():
            version = form.save()
        if request.is_ajax():

            data = {
                'version_id': version.pk,
                'version_nombre': version.nombre
            }
            return JsonResponse(data)
        else:
            return redirect(self.success_url)



class listarversion(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model = version_estandar
    template_name = 'administracion/version/listar_version.html'
    permission_required = ('administracion.change_version_estandar')



class actualizarversion(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = version_estandar
    form_class = version_estandarForm
    template_name = 'administracion/version/editar_version.html'
    permission_required = ('administracion.change_version_estandar')
    success_url = reverse_lazy('administracion:listarversion')



class eliminarversion(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = version_estandar
    template_name = 'administracion/version/eliminarversion.html'
    permission_required = ('administracion.delete_version_estandar')
    success_url = reverse_lazy('administracion:listarversion')


    def get(self, request, *args, **kwargs):
        if version_estandar.objects.filter(pk=kwargs['pk']).exists():
            version = version_estandar.objects.get(pk=kwargs['pk'])
            return render(request, self.template_name, {'object': version})
        else:
            return redirect('administracion:listarversion')







class colaboradorproyecto(LoginRequiredMixin,PermissionRequiredMixin,View):
    model = colaborador_proyectos
    form_class = colaborador_proyectoform
    template_name = 'administracion/Proyecto/asignarcolaborador.html'
    permission_required = ('administracion.add_colaborador_proyectos')
    success_url = reverse_lazy('administracion:listarproyecto')

    def get(self, request, *args, **kwargs):
        colaboradorproyecto = []
        listidusuario = []
        userlogueado=request.user
        proyecto = Proyecto.objects.get(id=kwargs['pk'])
        if proyecto.usuario.pk == request.user.pk or request.user.groups.filter(name='Administrador').exists():
            if colaborador_proyectos.objects.filter(proyecto=kwargs['pk']).exists():
                colaboradorproyecto = colaborador_proyectos.objects.filter(proyecto=kwargs['pk'])
                for usuario in colaboradorproyecto:
                    listidusuario.append(usuario.usuario.id)
            listidusuario.append(proyecto.usuario.id)
            usuarios = User.objects.filter(is_active=True).exclude(id__in=listidusuario)

            return render(request, self.template_name, {'asignados': colaboradorproyecto,'usuarios':usuarios,'proyecto':proyecto})
        else:
            return redirect('administracion:listarproyecto')

def asignarcolaborador(request):

        idproyecto = request.GET.get('idproyecto', None)

        idusuarios = request.GET.getlist('idusuarios[]')
        if idproyecto:
          proyecto = Proyecto.objects.get(id=idproyecto)
          if colaborador_proyectos.objects.filter(proyecto=idproyecto).exists():
              objetos = colaborador_proyectos.objects.filter(proyecto=idproyecto)
              for obj in objetos:
                  obj.delete()
        if idusuarios:
          for usuario in idusuarios:
              instanciausuario=User.objects.get(pk=usuario)
              colaborador_proyectos.objects.create(proyecto=proyecto, usuario=instanciausuario)

        data = {
            'is_taken': idproyecto
        }
        return JsonResponse(data)


# valida que el nombre de usuario no sea repetido
def validarnombreusuario(request):
    nombre = request.GET.get('nombre',None)
    existe=0
    if User.objects.filter(username=nombre).exists():
        existe = 1
    else:

        existe = 0

    data = {
        'existe': existe
    }
    return JsonResponse(data)

