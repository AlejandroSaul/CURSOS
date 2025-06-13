for (i = 0; i < 10; i++) {
  if (i == 1) {
    console.log("Hola " + i + " vez");
  } else {
    console.log("Hola " + i + " veces");
  }
}

//------------

var arreglo = ["Hola",1,true]

for(let i = 0 ; i< arreglo.length;i++ ){
    console.log(arreglo[i])
}

var persona1 = {
    nombre: "Ciapfa",
    edad: 2
}

var persona2 = {
    nombre: "Alejo",
    edad: 24
}

var personas = [persona1,persona2]

for(var index = 0 ; index< personas.length ; index++){
    if(personas[index].edad >= 20){
        break;
    }
    const element = personas[index].nombre;
    console.log(element)
}

personas.forEach(element => console.log(element.edad))

arreglo.forEach(cualquiertexto => console.log(cualquiertexto))