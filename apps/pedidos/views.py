from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from apps.pedidos.models import Pedidos, DetallePedido
from apps.pedidos.forms import PedidosForm, DetallePedidoForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.
class PedidosListar(ListView):
    model=DetallePedido
    template_name='pedidos/pedidos_list.html'

class PedidosCrear(CreateView):
    model=DetallePedido
    template_name='pedidos/pedidos_crear.html'
    form_class = DetallePedidoForm
    second_form_class = PedidosForm
    success_url = reverse_lazy('pedidos')
    success_message = 'Pedido creado de manera exitosa'
    
    def get_context_data(self, **kwargs):
        context = super(PedidosCrear, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            DetallePedido = form.save(commit=False)
            DetallePedido.pedidos = form2.save()
            DetallePedido.save()
            return HttpResponseRedirect(self.get_success_url())

class PedidosEliminar(DeleteView):
    model=DetallePedido
    form_class = DetallePedidoForm
    second_form_class = PedidosForm
    success_url = reverse_lazy('pedidos')