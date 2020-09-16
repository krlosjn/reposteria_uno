function retornarFecha()
{
    var fecha
    fecha=new Date ();
    var cadena=fecha.getDate()+'/'+(fecha.getMonth()+1)+'/'+fecha.getFullYear();
    return cadena;
}

function retornarHora()
{
    var fecha
    fecha=new Date ();
    var cadena=fecha.getHours()+':'+(fecha.getMinutes()+1)+':'+fecha.getSeconds();
    return cadena;
}
