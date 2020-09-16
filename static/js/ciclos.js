//Ciclo For
// var m1="Recorriendo el ciclo for";
// //Crear el ciclo For
// for (var i=0; i<5; i++)
// {
//     alert(m1);
// }

//Ciclo While
// var passwd="";
// while (passwd != "password")
// {
//     passwd=prompt("Contrasena", "");
// }
// alert("Muy bien has ingresado correctamente");

// //Ciclo do while
var input;
do{
    input=prompt("Introduzca algo aqui","");
}
while (input==null||input=="");
alert("Has ingresado " + input);
