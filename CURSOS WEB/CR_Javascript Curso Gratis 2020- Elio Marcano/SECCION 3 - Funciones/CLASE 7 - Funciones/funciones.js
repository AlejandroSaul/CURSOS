//Son un conjunto de sentencias que realizan una tarea
function saludo(){
    console.log('Hola a todos')
}

function miSuma(a,b){
    let resultado = a + b 
    return resultado
}

var miSuma2 = function (a,b,c){
    let resultado = a + b + c
    return resultado
}

saludo()
console.log(miSuma(1,2))

console.log(miSuma2(1,2,11))
