####-------Ahorcado 2.0-------------###
import random
IMÁGENES_AHORCADO = ['''

 +---+
 | |
 |
 |
 |
 |
 =========''', '''

 +---+
 | |
 O |
 |
 |
 |
 =========''', '''
 
 +---+
 | |
 O |
 | |
 |
 |
 =========''', '''
 
 +---+
 | |
 O |
/| |
 |
 |
 =========''', '''
 
 +---+
 |  |
 O  |
/|\ |
 |
 |
  =========''', '''
 
 +---+
 |  |
 O  |
/|\ |
/|
 |
 =========''', '''
 
 +---+
 |  |
 O  |
/|\ |
/ \ |
 |
 =========''','''
+---+
 |  |
 O] |
/|\ |
/ \ |
 |
 =========''','''
+---+
 |  |
[O] |
/|\ |
/ \ |
 |
 =========''']

palabras = {
"animales" : """hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo 
            perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra 
            nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso 
            serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra celular empanada proactivo hijueputa""".split(),
"colores": "amarillo cafe azul verde violeta blanco rosado negro rojo celeste dorado plateado gris magenta".split(),
"formas": "triangulo cuadrado rectangulo circulo cilindro hexagono".split(),
"paises": "argentina colombia venezuela ecuador españa inglaterra bolivia peru canada uruguay paraguay chile mexico guatemala panama".split(),}

###----funcion que extrae una palabra al azar del diccionario-----###
def obtenerPalabraAlAzar(listaDePalabras):
    clave_de_diccionario = random.choice(list(listaDePalabras.keys()))             ###-----convierte las claves del diccionario en una lista y las almacena en la variable
    indice = random.randint(0, len(listaDePalabras[clave_de_diccionario])-1)       ###-----almacena un numero aleatorio el cual servira como indice
    return listaDePalabras[clave_de_diccionario][indice], clave_de_diccionario     ###-----devuelve la palabra secreta, y la clave para la ayuda del usuarios 

###-----funcion que le pide a un usuario ingresar la palabra que quiere que otro usuario adivine-----###
def palabra_jugador():
    p_jugador = input("Escribe la palabra que quieres que adivinen: ").lower()
    return p_jugador    

###-----funcion que muestra en la consola el progreso del usuario--------####

def mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMÁGENES_AHORCADO[len(letrasIncorrectas)])
    print()                                                   
 
    print('Letras incorrectas:', end='')
   
    for letra in letrasIncorrectas:
        print(letra, end=' ')
       
 
    espaciosVacíos = '_' * len(palabraSecreta)
 
    for i in range(len(palabraSecreta)): # completar los espacios vacíos con las letras adivinadas
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]
    print()
    for letra in espaciosVacíos: # mostrar la palabra secreta con espacios entre cada letra
        
        print(letra, end=' ')
      
 

 # Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado sólo una letra, y no otra cosa.

def obtenerIntento(letrasProbadas):

    while True:
        
        intento = input("Adivina una letra: ").lower()
        
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa una LETRA.')
        
        else:
            return intento
 

 #--------------------------Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.

def jugarDeNuevo():

    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')

 
 
print('A H O R C A D O')

###-----se declaran las variables-----------------------------------###
letrasIncorrectas = ''
letrasCorrectas = ''
juegoTerminado = False
aux = 0         ###----variable auxiliar

###-----------------selecciona el modo de juego, solo o multijuador------###
###-----------------este bucle lo unico que hace es asignar el valor a la variable palabraSecreta-------####
###-----------------si va a ser una palabra de un usuario o una palabra del porgrama-------------###

print("Bienvenido/a desea jugar solo o con un friend? 1 o 2: ")
while 1:
   
    player = input("")
    if player == "1":

            palabraSecreta, clave_secreta = obtenerPalabraAlAzar(palabras)             ###------la funcion devuelve dos valores y los almacena en las variables
            break

    elif player == "2":
        
            palabraSecreta = palabra_jugador()
            break

    else: 
            print("Pon una opción correcta..")

###------------empieza el juego------------------------###
while True:
    ###------condicional que le muestra una ayuda al usuario si la desea, solo una vez por eso el auxiliar
    if player == "1" and 4 == len(letrasIncorrectas) and aux == 0:         
                                                                                            
        ayuda = input("Desea una ayuda (si o no): ").lower().startswith("s")
        if ayuda:
            print("--------------------------------","-"*len(clave_secreta))
            print("la palabra esta en el conjuno de:" , clave_secreta)
            print("--------------------------------","-"*len(clave_secreta))
            aux += 1

    

    mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
    
    # Permite al jugador escribir una letra.
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)
 
    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento
 
        # Verifica si el jugador ha ganado.
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
        if encontradoTodasLasLetras:
            print('¡Sí! ¡La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
            juegoTerminado = True
            
    else:
        letrasIncorrectas = letrasIncorrectas + intento
 
 # Comprobar si el jugador ha agotado sus intentos y ha perdido.
        if len(letrasIncorrectas) == len(IMÁGENES_AHORCADO) - 1:
            mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + str(palabraSecreta) + '"')
            juegoTerminado = True
            
 
 # Preguntar al jugador si quiere volver a jugar (pero sólo si el juego ha terminado).
 ###-----Juegos es True en los dos casos de que pierda o gane, entonces entra si o si en el condicional, la funcion jugar de nuevo es True si el usuario
 ###-----ingresa un string que empieze con "s" de lo contratio se devuelve False y por ende pasa al else y sale del juego.

    if juegoTerminado:               
        if jugarDeNuevo():             ###-----reasignamos todos los valores de las variable---
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            while 1:
                print("Desea jugar solo o con alguien? 1 0 2")
                player = input("")
                if player == "1":
                    palabraSecreta,clave_secreta = obtenerPalabraAlAzar(palabras)
                    break
                elif player == "2":
                    palabraSecreta = palabra_jugador()
                    break
                else: 
                    print("Pon una opción correcta..") 
        
        else: 
            opinion_usuario = input("Ayudenos a mejorar, comentenos que le parecio el juego: \n")
            print("Espero que se haya divertido, vuelva cuando quiera hp..♥")
            break
