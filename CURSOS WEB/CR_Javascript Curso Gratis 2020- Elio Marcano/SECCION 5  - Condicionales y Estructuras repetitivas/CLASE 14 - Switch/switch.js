//Recibe una expresion y de acuardo a ella, ejecuta un caso

var opcion = 2

switch (opcion){
    case 1:
        console.log("Menu Usuario")
        break;
    case 2 : 
        console.log("Menu administrativo")
        break;
    case 3 : 
        console.log("Configuracion")
        break;
    case "Nuevo Menu":
        var miNUevoMenu = "Salida"
        console.log(miNUevoMenu)
        break;
    default:
        console.log("Break")
        break;
}
