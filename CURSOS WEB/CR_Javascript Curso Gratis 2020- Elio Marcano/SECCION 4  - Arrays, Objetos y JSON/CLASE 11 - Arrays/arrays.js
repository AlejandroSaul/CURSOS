/* Basico */
var miArray = ["Ciapfa",2020,34.9,true]

console.log(miArray[2])

/* Anidados*/
var miArray2 = ["Ciapfa",2020,34.9,true,[1,2,3]]

console.log(miArray2[4][0])

/* Con funciones*/
console.log("---Con funciones---")

var permitido = "Usuario permitido"
var miFuncion = acceso => acceso

var persona = {
    nombre : "Pepe",
    edad : 25
}

var miArray3 = [miFuncion(permitido),persona]
console.log(miArray3[0])
console.log(miArray3[1].nombre)

/*Objetos anidados en array*/

var persona2 = {
    nombre : "Pepe",
    miAutomovil : [
        pintura = {
            marca : "Marca",
            Precio : 20000
        },
        vendedor = {
            nombre: "Ciapfa",
            edad : 20
        }
    ]
}

console.log(persona2.miAutomovil[1].edad)