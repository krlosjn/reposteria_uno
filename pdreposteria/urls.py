"""pdreposteria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.usuario.views import RegistroUsuario
from django.conf.urls import include, url
from apps.pedidos.views import PedidosListar, PedidosCrear, PedidosEliminar

from apps.postres.views import PostresListado, PostreDetalle, PostreCrear, PostreActualizar, PostreEliminar
from django.contrib.auth.views import LoginView, logout_then_login, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    #Creamos la ruta para listar todos los postres de la base de datos
    path('postres/', PostresListado.as_view(template_name = "postres/index.html"), name='leer'),
    path('postres/detalle/<int:pk>', PostreDetalle.as_view(template_name = "postres/detalles.html"), name='detalles'),
    path('postres/crear', PostreCrear.as_view(template_name = "postres/crear.html"), name='crear'),
    path('postres/editar/<int:pk>', PostreActualizar.as_view(template_name = "postres/actualizar.html"), name='actualizar'),
    path('postres/eliminar/<int:pk>', PostreEliminar.as_view(), name='eliminar'),

    path('pedidos/', PedidosListar.as_view(template_name = "pedidos/pedidos_list.html"), name='pedidos'),
    path('pedidos/nuevo', PedidosCrear.as_view(template_name = "pedidos/pedidos_crear.html"), name='pedidos_crear'),
    path('pedidos/eliminar/<int:pk>', PedidosEliminar.as_view(), name='pedidos_eliminar'),


    path('accounts/login/', LoginView.as_view(template_name = "usuario/index.html"), name='login'),
    path('logout/', logout_then_login, name='logout'),
    path('usuario/nuevo/', RegistroUsuario.as_view(), name='Registrar'),

    path('reset/password_reset/', PasswordResetView.as_view(template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html'), 
        name='password_reset'),
    path('reset/password_resetDone/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done'),
        
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),

    path('reset/password_resetComplete', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),

]

