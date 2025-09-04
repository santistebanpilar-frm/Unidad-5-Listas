#Trabajo Practico 5 : Listas  -  Santisteban Pilar - 1 prog 2 
# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
lista_multiplos = list(range(0,100,4))
print("Los numero multiplos entre el 1 al 100 del cuatro son: ", lista_multiplos)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
#Negative indexing: Negative indices count from the end of the sequence. my_list[-1] accesses the last element, my_list[-2] accesses the second-to-last, and so on.
lista = ["azul", "rojo", "verde","amarillo", "naranja"]
print("El penultimo elemento de la lista es ",lista[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
# Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []
lista_vacia = []
print("Lista original: ", lista_vacia)
lista_vacia.append("hola")
lista_vacia.append("hello")
lista_vacia.append("ciao")
print("Lista luego del append: ", lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]
print("Lista original es: ", animales)
animales[-3], animales[-1]= "loro", "oso"
print("La lista luego de mofiicarla:", animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
#Muestra el número mayor de toda la lista al estar usando la funcion MAX
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros. (uso slicing el cual no incluye el valor final 0:2,tmn se puede poner el paso en el tercer vvalor)
lista = list(range(10,31,5))
print(lista[0:2])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
print("La lista original es: ", autos)
autos[1],autos[2]= "bmw", "logan"
print("Lista luego de modiicarla: ", autos) 

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente.
# Imprimir la lista resultante por pantalla.(para armar un tablero se puedde utilizar matrices)
dobles = []
print("Lista original: ", dobles)
dobles.append(10)
dobles.append(20)
dobles.append(30)
print("Lista modiicada: ", dobles)

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"],["arroz", "fideos", "salsa"],["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.(rfemove elimina el primro de la lista)
# d) Imprimir la lista resultante por pantalla
compras[2].append("jugo")
compras[1][1]="tallarrines"
compras[0].remove("pan")
print(compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.
lista_anidada = [[15],[True],[25.5, 57.9, 30.6,],[False]]
print(lista_anidada)