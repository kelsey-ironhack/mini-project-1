import time
from os import system
import sys
## import time
#from os import system

hola = 'hola'

turno = ["X", "0"]

tablero = [
	[" ", " ", " "],
	[" ", " ", " "],
	[" ", " ", " "],
]

lista_jugadas_guardadas = []

def mostrar_tablero_cordenadas():
    tablero_ini = u'\u001b[38;5;84m' + '''Tablero con cordenadas validas:
	["1,1", "1,2", "1,3"],
	["2,1", "2,2", "2,3"],
	["3,1", "3,2", "3,3"],
    ''' + u'\u001b[0m'
    mensaje_con_delay(tablero_ini)
    #print(tablero_ini)



def mostrar_tablero(tablero):
    
    print("\n    1    2    3")
    f=0
    for fila in tablero:
        f=f+1
        print (f,fila)

def actualizar_tablero(posicion, jugador):
	tablero[posicion[0]][posicion[1]] = jugador        

def procesar_posicion(posicion):
	fila, columna = posicion.split(",")
	return [int(fila)-1, int(columna)-1]      
        
def posicion_correcta(posicion):
	if 0 <= posicion[0] <= 2 and 0 <= posicion[1] <= 2:
		if tablero[posicion[0]][posicion[1]] == " ":
			return True
	return False        

def ha_ganado(j):
	#compara las filas del tablero
	if tablero[0] == [j,j,j] or tablero[1] == [j,j,j] or tablero[2] == [j,j,j]:
		return True
	#compara las columnas
	elif tablero[0][0] == j and tablero[1][0] == j and tablero[2][0] == j:
		return True
	elif tablero[0][1] == j and tablero[1][1] == j and tablero[2][1] == j:
		return True
	elif tablero[0][2] == j and tablero[1][2] == j and tablero[2][2] == j:
		return True
	#compara las diagonales
	elif tablero[0][0] == j and tablero[1][1] == j and tablero[2][2] == j:
		return True
	elif tablero[0][2] == j and tablero[1][1] == j and tablero[2][0] == j:
		return True
	return False

def siguiente_turno(lista_jugadas):
    from random import randint
    fila = randint(1, 9)
    jugador = '0'
    cpu=1
    jugador3='CPU'
    
    pre, lista_jugadas = guardar_jugada(fila, lista_jugadas)
    if pre:
        tabla = {1:(0,0) , 2:(0,1) , 3:(0,2), 4:(1,0) , 5:(1,1) , 6:(1,2), 7:(2,0), 8:(2,1) , 9:(2,2)}
        num = tabla.get(fila)
        num = list(num)
        jugador4='CPU'
        posicion_l = num
        actualizar_tablero(posicion_l, '0')
        time.sleep(0.5) # Sleep for 3 seconds
        print(f"Turno {nombre_col(jugador4)}")
        time.sleep(0.5) # Sleep for 3 seconds
        mostrar_tablero(tablero)
        print('\n')
        time.sleep(0.5) # Sleep for 3 seconds
        mostrar_tablero_cordenadas()
    else:
        siguiente_turno(lista_jugadas)
    if ha_ganado(jugador):
        print ("1 {} ha ganado!!!".format(jugador3))
        imprimir_per()
        cpu=1
        #continuar_juego()
        return cpu

def num_jugada(jugada):
    tabla = {1:(0,0) , 2:(0,1) , 3:(0,2), 4:(1,0) , 5:(1,1) , 6:(1,2), 7:(2,0), 8:(2,1) , 9:(2,2)}

    for key, value in tabla.items():
        if list(value) == jugada:
            return(key)

def guardar_jugada(num,lista_jugadas):
    x=0
    for numero in lista_jugadas:
        if numero == num:
            x=1
    if x==1:
        lista_jugadas.remove(num)
        return(True,lista_jugadas)
    else:
        return(False,lista_jugadas)
    
def imprimir_log():
    print(u'\u001b[34m' + '''                                                         
 (                  )             (                )      
 )\))(   (       ( /(   (   (     )\ )       )  ( /(      
((_)()\  )\  (   )\()) ))\  )(   (()/(    ( /(  )\()) (   
(_()((_)((_) )\ (_))/ /((_)(()\   /(_))_  )(_))(_))/  )\  
|  \/  | (_)((_)| |_ (_))   ((_) (_)) __|((_)_ | |_  ((_) 
| |\/| | | |(_-<|  _|/ -_) | '_|   | (_ |/ _` ||  _|/ _ \ 
|_|  |_| |_|/__/ \__|\___| |_|      \___|\__,_| \__|\___/ '''+ u'\u001b[0m')
    #input('Pulse enter para CONTINUAR.....')
    input(mensaje_con_delay('Pulse enter para CONTINUAR.....'))
    system("clear")
    return

def imprimir_vic():
    print(u'\u001b[34m' + '''
_._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-                                        
                     )                    
 (   (   (        ( /(      (   (      )  
 )\  )\  )\   (   )\()) (   )(  )\  ( /(  
((_)((_)((_)  )\ (_))/  )\ (()\((_) )(_)) 
\ \ / /  (_) ((_)| |_  ((_) ((_)(_)((_)_  
 \ V /   | |/ _| |  _|/ _ \| '_|| |/ _` | 
  \_/    |_|\__|  \__|\___/|_|  |_|\__,_|'''+ u'\u001b[35m')
    #input('Pulse enter para CONTINUAR.....')
    #system("clear")
    return

def imprimir_per():
    print(u'\u001b[36m' + '''\n      |\__/,|   
(`\
  _.|o o  |_   ) )
-(((---(((--------
 (                                         
 )\ )             (                )       
(()/(   (   (     )\ )  (       ( /(   (   
 /(_)) ))\  )(   (()/(  )\  (   )\()) ))\  
(_))  /((_)(()\   ((_))((_) )\ (_))/ /((_) 
| _ \(_))   ((_)  _| |  (_)((_)| |_ (_))   
|  _// -_) | '_|/ _` |  | |(_-<|  _|/ -_)  
|_|  \___| |_|  \__,_|  |_|/__/ \__|\___|  ''' + u'\u001b[36m')
    #input('Pulse enter para CONTINUAR.....')
    #system("clear")
    return

def imprimir_emp():
    print(u'\u001b[33m' + '''\n        |\      _,,,---,,_
  ZZZzz /,`.-'`'    -.  ;-;;,_
       |,4-  ) )-,_. ,\ (  `'-'
       '---''(_/--'  `-'\_)                                         
                              )       
 (       )              )  ( /(   (   
 )\     (     `  )   ( /(  )\()) ))\  
((_)    )\  ' /(/(   )(_))(_))/ /((_) 
| __| _((_)) ((_)_\ ((_)_ | |_ (_))   
| _| | '  \()| '_ \)/ _` ||  _|/ -_)  
|___||_|_|_| | .__/ \__,_| \__|\___|  
             |_| ''' + u'\u001b[33m')
    #input('Pulse enter para CONTINUAR.....')
    #system("clear")
    return

def imprimir_log2():
    print('''\n░░░▄▀▌░▄▀▌░░░░░░░░░░░░
░▄██▀▀▀█▀▀▀▄╔╦╗╔╗╔╗╗╗╗
▐███░▐░█░▐░█║║║╠╝║║║║║
███████╥████╝╝╝╚╝╚╝╩╩╝
█████╚═╩═╝██░░░░░░░░░░''')
    #input('Pulse enter para CONTINUAR.....')
    #system("clear")
    return

def mensaje_con_delay(mensaje, delay_mensaje=0.03, delay_post=0.01):
    for char in mensaje:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay_mensaje)

    time.sleep(delay_post)
    return '\n'


def continuar_juego():
    #imprimir_log2()
    continuar = input("\nDesea continuar \t")
    continuar = continuar.lower()
    if continuar == 'no':
        #print ("Adios!!!")
        return False
    try:
        if continuar == 'si':
            #print('continuar') 
            return True
            
        else: 
            x=1/0
    except:
        print ("Respuesta no valida ")
        return continuar_juego()
    
def nombre_col(nombre):
    nombre = u'\u001b[38;5;209m' + nombre.upper() + u'\u001b[0m'
    return nombre

#print(f'Hola {nombre_col(nombre)} de apellido {apellido}, como te va?') "\u001b[34m"
    
def juego(tablero , lista_jugadas_guardadas):
    system("clear")
    imprimir_log()
    mostrar_tablero_cordenadas()
    print('\n')
    jugador2 = input('\n Ingresa nombre del jugador \t')
    mostrar_tablero(tablero)
    lista_jugadas=[1,2,3,4,5,6,7,8,9]
    #lista_jugadas_guardadas = []
    x="X"
    jugador='X'
    cpu=0
    while True:
        posicion = input(f"\n{nombre_col(jugador2)}, elige una posicion (fila, columna) de 1 a 3.\nO 'salir' para salir \t")
        posicion = posicion.lower()
        if posicion == 'salir':
            print ("Adios!!!")
            break
        try:
            posicion_l = procesar_posicion (posicion)			
        except:
            print (f"Error, posicion {posicion} no es válida. ")
            continue
        if posicion_correcta(posicion_l):
            actualizar_tablero(posicion_l, jugador)
            time.sleep(.5)
            mostrar_tablero(tablero)
            time.sleep(1.5) # Sleep for 3 seconds
            system("clear")
            print('\n')
            num= num_jugada(posicion_l)
            pre ,lista_jugadas = guardar_jugada(num,lista_jugadas)
            if len(lista_jugadas) ==0:
                if ha_ganado(jugador):
                    print (f"2 {nombre_col(jugador2)} ha ganado!!!")
                    imprimir_vic()
                    break
                else: 
                    #print("Empate")
                    imprimir_emp()
                    break
            if ha_ganado(jugador):
                print (f"3 {nombre_col(jugador2)} ha ganado!!!")
                imprimir_vic()
                if continuar_juego():
                    lista_jugadas_guardadas = []
                    tablero = [
                    [" ", " ", " "],
                    [" ", " ", " "],
                    [" ", " ", " "],
                    ]
                    juego(tablero , lista_jugadas_guardadas)
                    #print('cotinuar')
                else :
                    break
                    #print('adios')
                
                #break
            cpu = siguiente_turno(lista_jugadas)
            if cpu==1:
                break
            
            
        else:
            print (f"Posicion {posicion} no válida")
	
juego(tablero , lista_jugadas_guardadas)