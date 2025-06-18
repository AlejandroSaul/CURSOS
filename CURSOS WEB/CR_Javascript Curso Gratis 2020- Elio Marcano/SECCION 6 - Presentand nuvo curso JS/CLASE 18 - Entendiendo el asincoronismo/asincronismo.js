var funcionParam = () => console.log("Soy una funcion")

let funcion = (callback) => {
    console.log("Hola funcion")
    callback
}

funcion(funcionParam())

console.log("-------------Parte 2-------------")

setTimeout(() => console.log("Hola Mundo") , 10)
console.log(1)
console.log(2)
console.log(3)
console.log(4)
console.log(5)
console.log(6)
console.log(7)
console.log(8)
console.log(9)

for(let index = 1; index < 999; index++){
    console.log("Ya termino este bucle")
}

for(let index = 1; index < 9999; index++){
    console.log("Ya termino este bucle")
}