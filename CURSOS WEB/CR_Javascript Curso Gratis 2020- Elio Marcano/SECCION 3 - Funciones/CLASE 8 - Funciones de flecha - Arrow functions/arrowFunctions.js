var acceso = true

/*var accesoU = function(a){
    return a
} */

//var accesoU = a => a // retorna un valor
//var accesoU = () => false //no pasamos parametros a nuestra funcion y retornamos un valor

var accesoU = (a,n) => console.log(`Usuario ${n} Acceso ${a}`) //no pasamos parametros a nuestra funcion y retornamos un valor
accesoU(acceso,"Ciapfa")

//----------------

var accesoU = (a,n) => {
    console.log(`Usuario ${n} en ejecucion`)
    return a
}


accesoU(acceso,"Ciapfa") == true ? 
console.log("Usuario permitido") : 
console.log("Usuario denegado")