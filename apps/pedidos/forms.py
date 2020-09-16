from django import forms
from apps.pedidos.models import Pedidos, DetallePedido
# from _datetime import datetime
from functools import partial
import datetime
DateInput = partial(forms.DateInput, {'class':'datapicker'})

class PedidosForm(forms.ModelForm):
    class Meta:
        model=Pedidos
        fields = [
            'clientes',
            'fechapedido',
            'fechaentrega',
            'fechaenvio',
            'formaenvio',
            'destinatario',
            'direcciondestinatario',
            'ciudaddestinatario',
        ]
        labels = {
            'clientes': 'clientes',
            'fechapedido': 'fechapedido',
            'fechaentrega':'fechaentrega',
            'fechaenvio': 'fechaenvio',
            'formaenvio': 'formaenvio',
            'destinatario': 'destinatario',
            'direcciondestinatario':'direcciondestinatario',
            'ciudaddestinatario':'ciudaddestinatario',
        }
        widgets = {
            'clientes': forms.Select(attrs={'class':'form-control'}),
            # 'fechapedido': forms.widgets.DateInput(format='%Y-%m-%d', attrs={'value':datetime.now().strftime('%Y-%m-%d'), 'type':'date'}),
            # 'fechaentrega': forms.widgets.DateInput(format='%Y-%m-%d', attrs={'value':datetime.now().strftime('%Y-%m-%d'),'type':'date'}),
            # 'fechaenvio': forms.widgets.DateInput(format='%Y-%m-%d', attrs={'value':datetime.now().strftime('%Y-%m-%d'),'type':'date'}),
            'fechapedido': forms.widgets.DateInput(attrs={'type':'date', 'class':'form-control' }),
            'fechaentrega': forms.widgets.DateInput(attrs={'type':'date', 'class':'form-control' }),
            'fechaenvio': forms.widgets.DateInput(attrs={'type':'date', 'class':'form-control' }),
            'formaenvio': forms.TextInput(attrs={'class':'form-control'}),
            'destinatario': forms.TextInput(attrs={'class':'form-control'}),
            'direcciondestinatario':forms.Textarea(attrs={'class':'form-control'}),
            'ciudaddestinatario': forms.TextInput(attrs={'class':'form-control'}),
        }
class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model=DetallePedido
        fields = [
            'postre',
            'iva',
            'cantidad',
            'descuento',
            'subtotal',
            'total',
        ]
        labels = {
            'postre': 'postre',
            'iva': 'iva',
            'cantidad':'cantidad',
            'descuento': 'descuento',
            'subtotal': 'subtotal',
            'total': 'total',
        }
        widgets = {
            'postre': forms.Select(attrs={'class':'form-control'}),
            'iva': forms.Select(attrs={'class':'form-control'}),
            'cantidad':forms.TextInput(attrs={'class':'form-control'}),
            'descuento': forms.TextInput(attrs={'class':'form-control'}),
            'subtotal': forms.TextInput(attrs={'class':'form-control', 'readonly':True}),
            'total': forms.TextInput(attrs={'class':'form-control', 'readonly':True}),
        }