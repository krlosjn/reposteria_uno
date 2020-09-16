$(function(){
   $('#id_fechapedido').datepicker({
       format: 'YYYY-MM-DD',
       date: moment().format('YYYY-MM-DD'),
       locale: 'es'
   });
});

function PruebaInicial()
{
    alert("Probando...");
}
function Calcular()
{
    var cant, prec, desc, stotal, iva, total;
    cant = $("#id_cantidad").val();
    cant = cant===""? 0 :+cant;
    cant = cant<0 ? 0: cant;

    prec = $("#id_precio").val();
    prec = prec===""? 0 :+prec;
    prec = prec<0 ? 0: prec;

    iva = $("#id_iva").val();
    iva = iva===""? 0 :+iva;
    iva = iva<0 ? 0: iva;

    desc = $("#id_descuento").val();
    desc = desc===""? 0 :+desc;
    desc = desc<0 ? 0: desc;

    desc= desc>(cant*prec) ? 0:desc;
    
    stotal = cant * prec;
    iva = (stotal - desc)*(iva/100);
    total = (stotal - desc)+iva;

    $('#id_cantidad').val(cant);
    $('#id_precio').val(prec);
    $('#id_iva').val(iva);
    $('#id_descuento').val(desc);
    $('#id_subtotal').val(stotal);
    $('#id_total').val(total);
    

    
}