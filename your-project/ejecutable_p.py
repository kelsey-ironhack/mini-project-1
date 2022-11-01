import random
import urllib.request 
import webbrowser



juego = True
dinero = 0

def preguntar(pregunta,respuestas, correcto, monto) :
    print(pregunta) 
    
    for respuesta in respuestas :
        print(respuesta)
        
    participante = input('ingresa tu respuesta (A,B,C o D) ') 
    while participante not in ['A', 'B', 'C', 'D' , 'a', 'b', 'c', 'd'] :
        print('ingrese respuesta valida')
        participante = input('ingresa tu respuesta (A,B,C o D) ')
            
    
    if participante.upper() == correcto :
        respuestabuena(monto)
    else :
        game_over()
        
def respuestabuena(monto) :
    print('correcto!!!')
    global dinero 
    dinero = monto
    
    print(f'muy bien {nombre}!!! llevas {dinero} acumulado')

def game_over() :
    global juego
    juego = False
    
    print('buuuuuuu, te equivocaste, lo perdiste todo')
    
    


pregunta1 = '¿A cuánto equivale una unidad astronómica?'
respuestas1 = [ 'A) La distancia entre el Sol y la Tierra' , 'B) La distancia entre la Vía Láctea y Próxima Cerntauri ', 'C) La distancia entre México y Venezuela ' , 'D) La distancia entre la Luna y Saturno']
correcto1 = 'A'
monto1 = 100

pregunta2 = '¿Cuál de los siguientes países pertenece a Asia Central?'
respuestas2 = [ 'A) Bolivia' , 'B) India', 'C) Sri Lanka' , 'D) Kirguistán']
correcto2 = 'D'
monto2 = 100

pregunta3 = '¿Cuál de los siguientes cetaceos tiene dientes?'
respuestas3 = [ 'A) Rourcal' , 'B) Ballena de Groenlandia', 'C) Ballena Azúl' , 'D) Cachalote']
correcto3 = 'D'
monto3 = 100

pregunta4 = '¿Quién es el heroe nacional de Venezuela?'
respuestas4 = [ 'A) Confucio' , 'B) Simón Bolivar', 'C) José de San Martín' , 'D) Miguel Hidalgo']
correcto4 = 'B'
monto4 = 100

pregunta5 = '¿A cuanto equivale 56 elevado a la 0 (56^0)?'
respuestas5 = [ 'A) 1' , 'B) 578', 'C) 11' , 'D) 0.765']
correcto5 = 'A'
monto5 = 100

pregunta6 = '¿En dónde vive Oscar Landivar?'
respuestas6 = [ 'A) México' , 'B) Chile', 'C) Perú' , 'D) Panamá']
correcto6 = 'A'
monto6 = 100

pregunta7 = '¿Cuál de los siguientes es un lenguaje de programación?'
respuestas7 = [ 'A) Excel' , 'B) C++', 'C) Adobe' , 'D) SQL']
correcto7 = 'B'
monto7 = 100

pregunta8 = '¿La expresión map en Python es similar a?'
respuestas8 = [ 'A) For' , 'B) Filter', 'C) Lambda' , 'D) Pandas']
correcto8 = 'A'
monto8 = 100

pregunta9 = '¿Cuál de las siguientes es una librería en Python?'
respuestas9 = [ 'A) stdio' , 'B) Excite', 'C) Kiis' , 'D) Numpy']
correcto9 = 'D'
monto9 = 100

pregunta10 = '¿Python es portable?'
respuestas10 = [ 'A) No' , 'B) Depende...', 'C) Si' , 'D) Solo si uso una Mac']
correcto10 = 'C'
monto10 = 100

pregunta11 = '¿En que país es fabricado el Iphone?'
respuestas11 = [ 'A) Japón' , 'B) Vietnam', 'C) China' , 'D) Estados Unidos']
correcto11 = 'C'
monto11 = 100

pregunta12 = '¿La desviación estandar se puede calcualar a partir de la raíz cuadrada de la varianza?'
respuestas12 = [ 'A) Con Python no' , 'B) Con Python si', 'C) No' , 'D) Si']
correcto12 = 'D'
monto12 = 100

pregunta13 = '¿Cuál de los siguientes gases respira el ser humano?'
respuestas13 = [ 'A) Hidrógeno' , 'B) Nitrógeno', 'C) Neón' , 'D) Helio']
correcto13 = 'B'
monto13 = 100

pregunta14 = '¿Las tuplas inmutables...?'
respuestas14 = [ 'A) Inmutables' , 'B) Grises ', 'C) Mutables' , 'D) No usadas']
correcto14 = 'A'
monto14 = 100

pregunta15 = '¿Qué lugar en los oceanos es el más profundo?'
respuestas15 = [ 'A) El Ártico' , 'B) El Caribe', 'C) Mar Mediterraneo' , 'D) La fosa de las Marianas']
correcto15 = 'D'
monto15 = 100

pregunta16 = '¿Aplicaremos el teorema de Bayes en el curso DAPT 2022?'
respuestas16 = [ 'A) Si' , 'B) No', 'C) Quizás' , 'D) Sólo con Python']
correcto16 = 'A'
monto16 = 100

pregunta17 = '¿Cuál de los siguientes es una parte un agujero negro?'
respuestas17 = [ 'A) gravedad' , 'B) espacio', 'C) horizonte de eventos' , 'D) anillo']
correcto17 = 'C'
monto17 = 100

pregunta18 = '¿Cuál es la velocidad máxima a la que corre la chita?'
respuestas18 = [ 'A) 78 km/h' , 'B) 40 km/h', 'C) 90 km/h' , 'D) 75 km/h']
correcto18 = 'C'
monto18 = 100

pregunta19 = '¿La matrices se pueden dividir entre si?'
respuestas19 = [ 'A) No' , 'B) Calculando la desviación estandar', 'C) Si' , 'D) Elevandolas al cuadrado']
correcto19 = 'A'
monto19 = 100

pregunta20 = '¿Cuántos habitantes tiene México, aproximadamente?'
respuestas20 = [ 'A) 190 millones' , 'B) 130 millones', 'C) 85 millones' , 'D) 250 millones']
correcto20 = 'B'
monto20 = 100

pregunta21 = '¿En dónde fueron los juegos olímpicos de 1992?'
respuestas21 = [ 'A) Sidney' , 'B) Seúl', 'C) Los Ángeles' , 'D) Barcelona']
correcto21 = 'D'
monto21 = 100

pregunta22 = '¿Quién gano el mundial de Estados Unidos de 1994?'
respuestas22 = [ 'A) Portugal' , 'B) Argentina', 'C) Brasil' , 'D) Alemania']
correcto22 = 'D'
monto22 = 100

pregunta23 = '¿Cuántas temporadas se han publicado de Naruto?'
respuestas23 = [ 'A) 7' , 'B) 9', 'C) 11' , 'D) 5']
correcto23 = 'B'
monto23 = 100

pregunta24 = '¿Cuál es el valor de la gravedad en Marte?'
respuestas24 = [ 'A) 3.721 m/s2' , 'B) 9.81 m/s2', 'C) 6.45 m/s2' , 'D) 7.8 m/s2']
correcto24 = 'A'
monto24 = 100

pregunta25 = '¿De la división territorial de Rusia cuántos son Óblast?'
respuestas25 = [ 'A) 50' , 'B) 48', 'C) 31' , 'D) 24']
correcto25 = 'B'
monto25 = 100

pregunta26 = '¿En que país esta la playa de Fernández Noroña?'
respuestas26 = [ 'A) Honduras' , 'B) Venezuela', 'C) México' , 'D) Brasil']
correcto26 = 'D'
monto26 = 100

pregunta27 = '¿Cómo identificar espacios en Regex?'
respuestas27 = [ 'A) {2,}' , 'B) \s ', 'C) [ ]' , 'D) .*']
correcto27 = 'B'
monto27 = 100

pregunta28 = 'Expresión en Regex que coincide con caracteres alfabéticos (letras):'
respuestas28 = [ 'A) (...)' , 'B) {n} ', 'C) [:alpha:]' , 'D) [^...]']
correcto28 = 'C'
monto28 = 100

pregunta29 = 'Las variables locales de Python se declaran dentro de una .....'
respuestas29 = [ 'A) Función' , 'B) en un String ', 'C) de un diccionario' , 'D) en la llave de un diccionario']
correcto29 = 'A'
monto29 = 100

pregunta30 = 'Se utiliza cuando se necesita algún bloque de código sintácticamente, pero se desea omitir su ejecución'
respuestas30 = [ 'A) Except' , 'B) Continue ', 'C) Break' , 'D) Pass']
correcto30 = 'D'
monto30 = 100


if __name__ == "__main__":
    
    nombre = input('cual es tu nombre:  ' )


    if nombre == 'huevo de pascua' : 
        url= 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  

        webbrowser.open_new_tab(url)  



    if len(nombre) in [1,2]  :
        preguntar(pregunta30 , respuestas30, correcto30, 100)

        if juego == True :
            preguntar(pregunta29 , respuestas29, correcto29, 300)

        if juego == True :
            preguntar(pregunta5 , respuestas5, correcto5, 500)

        if juego == True :
            preguntar(pregunta6 , respuestas6, correcto6, 1000)

        if juego == True :
            preguntar(pregunta25 , respuestas25, correcto25, 1500)

        if juego == True :
            preguntar(pregunta26 , respuestas26, correcto26, 2000)

        if juego == True :
            preguntar(pregunta27 , respuestas27, correcto27, 3000)

        if juego == True :
            preguntar(pregunta28 , respuestas28, correcto28, 5000)

        if juego == True :
            preguntar(pregunta9 , respuestas9, correcto9, 8000)

        if juego == True :
            preguntar(pregunta1 , respuestas1, correcto1, 10000)

        if juego == True :

            dinero = 0
            print('tu dinero se a actualizado a 0')
            print(f'felicidades {nombre}, el verdadero premio son los amigos que hacemos en el camino')
            url= 'https://www.youtube.com/watch?v=3GwjfUFyY6M'  
            webbrowser.open_new_tab(url)
    if len(nombre) == 3 :
        preguntar(pregunta11 , respuestas11, correcto11, 100)

        if juego == True :
            preguntar(pregunta12 , respuestas12, correcto12, 300)

        if juego == True :
            preguntar(pregunta13 , respuestas13, correcto13, 500)

        if juego == True :
            preguntar(pregunta14 , respuestas14, correcto14, 1000)

        if juego == True :
            preguntar(pregunta15 , respuestas15, correcto15, 1500)

        if juego == True :
            preguntar(pregunta16 , respuestas16, correcto16, 2000)

        if juego == True :
            preguntar(pregunta17 , respuestas17, correcto17, 3000)

        if juego == True :
            preguntar(pregunta18 , respuestas18, correcto18, 5000)

        if juego == True :
            preguntar(pregunta19 , respuestas19, correcto19, 8000)

        if juego == True :
            preguntar(pregunta20 , respuestas20, correcto20, 10000)

        if juego == True :

            dinero = 0
            print('tu dinero se a actualizado a 0')
            print(f'felicidades {nombre}, el verdadero premio son los amigos que hacemos en el camino')

    if len(nombre) == 4 :
        preguntar(pregunta13 , respuestas13, correcto13, 100)

        if juego == True :
            preguntar(pregunta12 , respuestas12, correcto12, 300)

        if juego == True :
            preguntar(pregunta30 , respuestas30, correcto30, 500)

        if juego == True :
            preguntar(pregunta16 , respuestas16, correcto16, 1000)

        if juego == True :
            preguntar(pregunta5 , respuestas5, correcto5, 1500)

        if juego == True :
            preguntar(pregunta26 , respuestas26, correcto26, 2000)

        if juego == True :
            preguntar(pregunta20 , respuestas20, correcto20, 3000)

        if juego == True :
            preguntar(pregunta18 , respuestas18, correcto18, 5000)

        if juego == True :
            preguntar(pregunta9 , respuestas9, correcto9, 8000)

        if juego == True :
            preguntar(pregunta2 , respuestas2, correcto2, 10000)

        if juego == True :

            dinero = 0
            print('tu dinero se a actualizado a 0')
            print(f'felicidades {nombre}, el verdadero premio son los amigos que hacemos en el camino')

    if len(nombre) == 5 :
        preguntar(pregunta16 , respuestas16, correcto16, 100)

        if juego == True :
            preguntar(pregunta22 , respuestas22, correcto22, 300)

        if juego == True :
            preguntar(pregunta23 , respuestas23, correcto23, 500)

        if juego == True :
            preguntar(pregunta14 , respuestas14, correcto14, 1000)

        if juego == True :
            preguntar(pregunta25 , respuestas25, correcto25, 1500)

        if juego == True :
            preguntar(pregunta6 , respuestas6, correcto6, 2000)

        if juego == True :
            preguntar(pregunta27 , respuestas27, correcto27, 3000)

        if juego == True :
            preguntar(pregunta18 , respuestas18, correcto18, 5000)

        if juego == True :
            preguntar(pregunta9 , respuestas9, correcto9, 8000)

        if juego == True :
            preguntar(pregunta10 , respuestas10, correcto10, 10000)

        if juego == True :

            dinero = 0
            print('tu dinero se a actualizado a 0')
            print(f'felicidades {nombre}, el verdadero premio son los amigos que hacemos en el camino')

    if len(nombre) == 6 :
        preguntar(pregunta10 , respuestas10, correcto10, 100)

        if juego == True :
            preguntar(pregunta20 , respuestas20, correcto20, 300)

        if juego == True :
            preguntar(pregunta30 , respuestas30, correcto30, 500)

        if juego == True :
            preguntar(pregunta24 , respuestas24, correcto24, 1000)

        if juego == True :
            preguntar(pregunta15 , respuestas15, correcto15, 1500)

        if juego == True :
            preguntar(pregunta6 , respuestas6, correcto6, 2000)

        if juego == True :
            preguntar(pregunta27 , respuestas27, correcto27, 3000)

        if juego == True :
            preguntar(pregunta18 , respuestas18, correcto18, 5000)

        if juego == True :
            preguntar(pregunta29 , respuestas29, correcto29, 8000)

        if juego == True :
            preguntar(pregunta19 , respuestas19, correcto19, 10000)

        if juego == True :

            dinero = 0
            print('tu dinero se a actualizado a 0')
            print(f'felicidades {nombre}, el verdadero premio son los amigos que hacemos en el camino')

    if len(nombre) == 7 :
        preguntar(pregunta19 , respuestas19, correcto19, 100)

        if juego == True :
            preguntar(pregunta21 , respuestas21, correcto21, 300)

        if juego == True :
            preguntar(pregunta3 , respuestas3, correcto3, 500)

        if juego == True :
            preguntar(pregunta4 , respuestas4, correcto4, 1000)

        if juego == True :
            preguntar(pregunta25 , respuestas25, correcto25, 1500)

        if juego == True :
            preguntar(pregunta16 , respuestas16, correcto16, 2000)

        if juego == True :
            preguntar(pregunta7 , respuestas7, correcto7, 3000)

        if juego == True :
            preguntar(pregunta8 , respuestas8, correcto8, 5000)

        if juego == True :
            preguntar(pregunta9 , respuestas9, correcto9, 8000)

        if juego == True :
            preguntar(pregunta20 , respuestas20, correcto20, 10000)

        if juego == True :

            dinero = 0
            print('tu dinero se a actualizado a 0')
            print(f'felicidades {nombre}, el verdadero premio son los amigos que hacemos en el camino')

    if len(nombre) == 8 :
        preguntar(pregunta12 , respuestas12, correcto12, 100)

        if juego == True :
            preguntar(pregunta29 , respuestas29, correcto29, 300)

        if juego == True :
            preguntar(pregunta3 , respuestas3, correcto3, 500)

        if juego == True :
            preguntar(pregunta24 , respuestas24, correcto24, 1000)

        if juego == True :
            preguntar(pregunta25 , respuestas25, correcto25, 1500)

        if juego == True :
            preguntar(pregunta6 , respuestas6, correcto6, 2000)

        if juego == True :
            preguntar(pregunta27 , respuestas27, correcto27, 3000)

        if juego == True :
            preguntar(pregunta8 , respuestas8, correcto8, 5000)

        if juego == True :
            preguntar(pregunta30 , respuestas30, correcto30, 8000)

        if juego == True :
            preguntar(pregunta10 , respuestas10, correcto10, 10000)

        if juego == True :

            dinero = 0
            print('tu dinero se a actualizado a 0')
            print(f'felicidades {nombre}, el verdadero premio son los amigos que hacemos en el camino')

    if len(nombre) == 9 :
        preguntar(pregunta1 , respuestas1, correcto1, 100)

        if juego == True :
            preguntar(pregunta2 , respuestas2, correcto2, 300)

        if juego == True :
            preguntar(pregunta3 , respuestas3, correcto3, 500)

        if juego == True :
            preguntar(pregunta4 , respuestas4, correcto4, 1000)

        if juego == True :
            preguntar(pregunta5 , respuestas5, correcto5, 1500)

        if juego == True :
            preguntar(pregunta6 , respuestas6, correcto6, 2000)

        if juego == True :
            preguntar(pregunta7 , respuestas7, correcto7, 3000)

        if juego == True :
            preguntar(pregunta8 , respuestas8, correcto8, 5000)

        if juego == True :
            preguntar(pregunta9 , respuestas9, correcto9, 8000)

        if juego == True :
            preguntar(pregunta10 , respuestas10, correcto10, 10000)

        if juego == True :

            dinero = 0
            print('tu dinero se a actualizado a 0')
            print(f'felicidades {nombre}, el verdadero premio son los amigos que hacemos en el camino')

    if len(nombre) == 10 :
        preguntar(pregunta11 , respuestas11, correcto11, 100)

        if juego == True :
            preguntar(pregunta2 , respuestas2, correcto2, 300)

        if juego == True :
            preguntar(pregunta13 , respuestas13, correcto13, 500)

        if juego == True :
            preguntar(pregunta24 , respuestas24, correcto24, 1000)

        if juego == True :
            preguntar(pregunta15 , respuestas15, correcto15, 1500)

        if juego == True :
            preguntar(pregunta6 , respuestas6, correcto6, 2000)

        if juego == True :
            preguntar(pregunta17 , respuestas17, correcto17, 3000)

        if juego == True :
            preguntar(pregunta28 , respuestas28, correcto28, 5000)

        if juego == True :
            preguntar(pregunta19 , respuestas19, correcto19, 8000)

        if juego == True :
            preguntar(pregunta20 , respuestas20, correcto20, 10000)

        if juego == True :

            dinero = 0
            print('tu dinero se a actualizado a 0')
            print(f'felicidades {nombre}, el verdadero premio son los amigos que hacemos en el camino')

    if len(nombre) > 10 :
        preguntar(pregunta21 , respuestas21, correcto21, 100)

        if juego == True :
            preguntar(pregunta22 , respuestas22, correcto22, 300)

        if juego == True :
            preguntar(pregunta23 , respuestas23, correcto23, 500)

        if juego == True :
            preguntar(pregunta24 , respuestas24, correcto24, 1000)

        if juego == True :
            preguntar(pregunta25 , respuestas25, correcto25, 1500)

        if juego == True :
            preguntar(pregunta26 , respuestas26, correcto26, 2000)

        if juego == True :
            preguntar(pregunta27 , respuestas27, correcto27, 3000)

        if juego == True :
            preguntar(pregunta28 , respuestas28, correcto28, 5000)

        if juego == True :
            preguntar(pregunta29 , respuestas29, correcto29, 8000)

        if juego == True :
            preguntar(pregunta30 , respuestas30, correcto30, 10000)

        if juego == True :

            dinero = 0
            print('tu dinero se a actualizado a 0')
            print(f'felicidades {nombre}, el verdadero premio son los amigos que hacemos en el camino')