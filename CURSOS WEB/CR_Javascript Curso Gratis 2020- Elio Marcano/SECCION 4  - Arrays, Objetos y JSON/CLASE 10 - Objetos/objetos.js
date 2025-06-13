var user = "Alejo"
var miObjeto = {
    //clave : valor
    nombre : "Ciapfa",
    edad : 2020,
    importante : true,
    texto : `Usuario ${user}`,
    miFuncion : (a,b) => a + b,
    otroObjeto : { //tambien lo podemos sacar en una variable
        nombre:"Alejo",
        sexo:"Masculino"
    },
    miFecha : new Date()
}

console.log(miObjeto)
console.log(miObjeto.nombre)
console.log(miObjeto.edad)
console.log(miObjeto.importante)
console.log(miObjeto.texto)
console.log(miObjeto.miFuncion(8,2))
console.log(miObjeto.otroObjeto)
console.log(miObjeto.otroObjeto.nombre)
console.log(miObjeto.miFecha)
console.log(miObjeto.miFecha.getFullYear())

//------DESTRUCTURACION DE OBJETOS --------
console.log("------DESTRUCTURACION DE OBJETOS --------")

var {nombre} = miObjeto
console.log(nombre) // Ciapfa

var otraFuncion = ({texto}) => texto
console.log(otraFuncion(miObjeto)) // Usuario Alejo

var otraFuncion = ({texto},{otroObjeto}) => {
    console.log(texto)
    console.log(otroObjeto)
} 
otraFuncion(miObjeto,miObjeto) //  Usuario Alejo y Objeto
