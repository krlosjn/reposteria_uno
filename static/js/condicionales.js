
    var edad;
    edad = prompt ("Introduzca edad (en numero): ");
    edad = parseInt(edad);
    if (edad < 18)//Realizar comprobacion si es menor de edad
    {
        alert("Eres menor de edad");
    }
    else if (edad<65)
    {
        alert("Usted sigue siendo adulto");
    }
    else
    {
        alert("Ya debes jubilarte");
    }
    
