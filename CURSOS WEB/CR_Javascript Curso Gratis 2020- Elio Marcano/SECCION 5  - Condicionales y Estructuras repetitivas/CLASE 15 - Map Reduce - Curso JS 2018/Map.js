var pelicula1 = {
    titulo:"La monja",
    anio:"2018",
    valoracion: 4
}
var pelicula2 = {
    titulo:"Annabelle",
    anio:"2014",
    valoracion: 3
}
var pelicula3 = {
    titulo:"Annabelle 2",
    anio:"2017",
    valoracion: 5
}
var pelicula4 = {
    titulo:"El Conjuro",
    anio:"2013",
    valoracion: 5
}
var pelicula5 = {
    titulo:"El Conjuro 2",
    anio:"2016",
    valoracion: 3
}

var peliculas = [pelicula1,pelicula2,pelicula3,pelicula4,pelicula5]

var sumaValoracion = ({valoracion}) => valoracion >= 5 ? valoracion += 1 : valoracion +=0;

console.log(peliculas.map(sumaValoracion))

// REDUCE

var miValoracion = (acum,{valoracion}) =>  acum+valoracion
console.log(peliculas.reduce(miValoracion,0))


//CREAR NUEVO OBJETO
console.log('------------CREACION DE NUEVO OBJETO------------')
let nuevoObjeto = ({valoracion}) => {
    valoracion >= 5 ? valoracion += 1 : valoracion += 0;
    var objeto = {}
    objeto ["valoracion"] = valoracion
    return objeto
}

var miNuevaValoracion = peliculas.map(nuevoObjeto)
console.log(peliculas)
console.log(miNuevaValoracion)
