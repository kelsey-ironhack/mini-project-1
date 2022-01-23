import random
import time

jugar = True

while jugar == True:



    print("                                          BIENVENIDO A BLACKJACK!!!")

    print("---------------------------------------------------------------------------------------------------------------")
    print ("""OBJETIVO:
    Este juego consiste en enfrentarse de forma individual a la banca (computadora) comparando su mano con la del usuario,
    el ojetivo del juego es conseguir 21 puntos o el número más cercano posible sin pasarse.
    
    """)

    print("""INSTRUCCIONES:
    Para conseguir dicha puntuación se suman los valores de dos cartas que se reparten de inicio a cada jugador, con los de 
    aquellas nuevas cartas que, opcionalmente, se podrán añadir en el turno de juego. Si las dos cartas iniciales suman 21, 
    se denomina BLACKJACK, y es la mejor jugada. Cuando un jugador no suma 21 con sus dos cartas podrá pedir cartas para 
    conseguir dicho número o uno cercano pero si el jugador se pasa de esos 21 puntos pierde, indistintamente de lo que haga
    la banca.
    
    La banca también juega pero tiene unas reglas muy definidas que se han de tener en cuenta. Si la suma de las cartas de 
    la banca es 16 o menos, debe pedir carta y si suman 17 o más se debe plantar.
    La banca gana a todos los jugadores que se pasen de 21 y a aquellos que tengan un jugada de menor valor, por otro lado,
    empata con aquellos jugadores que tengan la misma suma. La mano de la banca pierde con los jugadores que tengan una mano
    superior a la suya o, si la banca se pasa, con todos aquellos que se plantaron, tengan la suma de puntos que tengan.
    
    """)
    print("""VAlOR DE LAS CARTAS EN EL BLACKJACK:
    El As es la única carta de la baraja que tiene dos valores, 1 y 11, siendo el jugador que lo posea quien elige el
    valor entre ambos según le convenga; Las cartas numeradas con índice del dos al diez tienen el valor correspondiente a 
    su numeración; finalmente, todas las figuras (Jack, Queen y King), tienen el mismo valor: 10. 
    
    """)
    print("---------------------------------------------------------------------------------------------------------------------")


    print("""INICIA EL JUEGO!!!"
          """)

    # Variables para geenrar la baraja.

    palos_baraja = ["♥️", "♠️", "♣️", "♦️"]  # C:corazones, P:picas, T: trebol y D:diamantes
    numero_baraja = ["A ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10 ", "J ", "Q ", "K "]
    cartas_list = [carta + palo for carta in numero_baraja for palo in palos_baraja]
    cartas_user = []
    cartas_dealer = []
    baraja = {}


    # La función crear_baraja genera la baraja de 52 cartas con la que se jugará:

    def crear_baraja(cartas):
        for i in cartas:
            if i[0] == "A":
                baraja[i] = (11)
            elif i[0] in "KQJ":
                baraja[i] = 10
            else:
                baraja[i] = int(i[0:2])

        return baraja

    bar = crear_baraja(cartas_list)        # Esta es la variable que representa el conjunto de 52 cartas.

    #print(len(bar))

    #print (crear_baraja(cartas_list))

    #
    # La función repartir_cartas se encarga de dar una carta aleatoria a cada jugador y eliminar esa carta de la baraja.

    def repartir_cartas(cartas):
        a = random.choices(list(cartas.items()))
        del cartas[a[0][0]]
        return a


    # Asignar cartas a cada jugador llamando a la funcion repartir_cartas:

    carta1_user = repartir_cartas(bar)
    cartas_user.append(carta1_user[0])
    print("Usuario:", cartas_user[0][0])
    time.sleep(1)

    carta1_dealer = repartir_cartas(bar)
    cartas_dealer.append(carta1_dealer[0])
    print("Dealer:", cartas_dealer[0][0])
    time.sleep(1)

    carta2_user = repartir_cartas(bar)
    cartas_user.append(carta2_user[0])
    print("Usuario:", cartas_user[1][0])
    time.sleep(1)


    carta2_dealer = repartir_cartas(bar)
    cartas_dealer.append(carta2_dealer[0])
    print("Dealer:", cartas_dealer[1][0])
    time.sleep(1)


    #print(cartas_user)
    #print(cartas_dealer)

    # Funcion para evaluar resultados de las primeras dos cartas:

    def resultado1(mano):
        suma = 0

        for i in range(len(mano)):
            suma += int(mano[i][1])

        return suma


    print("===============================================================================================================")

    #Contabiliza los puntajes de las cartas de cada jugador
    user = resultado1(cartas_user)
    print("Puntaje usuario: ", user)

    time.sleep(2.5)

    dealer = resultado1(cartas_dealer)
    print("Puntaje dealer: ", dealer)


    #Validar si alguno de los jugadores hizo BLACKJACK:
    if user == 21 or dealer == 21:

        if user == 21 and dealer != 21:
            print("Hiciste BLACKJACK!!!!")
        elif user != 21 and dealer == 21:
            print("El dealer hizo BLACKJACK!!!")
        else:
            print("EMPATE!!! Los dos hicieron BLACKJACK")

        exit()

    print("===============================================================================================================")

    time.sleep(2.5)

    # Contabilizar las primeras cartas del usuario y saber si quiere más cartas:

    if user <21:
        request=True
        while user < 21 and request == True:
            respuesta = (input("¿Quieres otra carta, SI teclea 1, NO teclea 2?"))
            contador = 1
            time.sleep(2.5)

            if respuesta == "1":
                carta3_user = repartir_cartas(bar)
                cartas_user.append(carta3_user[0])
                contador = contador +1

                if list(carta3_user[0]) == "A":
                    user = user + 1
                    print("Usuario:", cartas_user[contador][0])
                    time.sleep(2.5)
                    print("Nuevo puntaje del usuario:", user)


                else:
                    user = resultado1(cartas_user)
                    print("Usuario:", cartas_user[contador][0])
                    time.sleep(2.5)
                    print("Nuevo puntaje del usuario:", user)

            else:
                request = False
                print("Te quedas con las mismas cartas, tu puntaje final es: ", user)


    if user == 21:
        print("Hiciste 21 puntos...")

    if user > 21:
        print("                              PERDISTE, hiciste más de 21 puntos...")

        exit()


    #time.sleep(2.5)
    print("===============================================================================================================")
    # Conatbilizar las primeras cartas del dealer y saber si va por más:
    time.sleep(2.5)

    if dealer < 21:
        request2 = True
        while dealer < 21 and request2 == True:
            contador=1

            if dealer <= 16:
                print("Dealer tomará una carta")
                time.sleep(2.5)
                carta3_dealer = repartir_cartas(bar)
                cartas_dealer.append(carta3_dealer[0])
                contador = contador + 1

                if list(carta3_dealer[0]) == "A":
                    dealer = dealer + 1

                    print("Dealer:", cartas_dealer[contador][0])
                    print("Nuevo puntaje del dealer:", dealer)

                else:
                    dealer = resultado1(cartas_dealer)
                    print("Dealer:", cartas_dealer[contador][0])
                    print("Nuevo puntaje del dealer:", dealer)


            else:
                dealer = resultado1(cartas_dealer)
                time.sleep(2.5)
                print("Dealer no tomara más cartas, su puntaje final es:", dealer)
                request2 = False


    if dealer == 21:
        print("Dealer hizo 21 puntos.")

    if dealer > 21:
        print("GANASTE!!! Dealer hizo más de 21 puntos...")

        exit()


    time.sleep(3)

    # Establecer al ganador:

    if user <= 21 and dealer <= 21:

        if user > dealer:

            print("""                            
                                ERES EL GANADOR!!!! 
                                
                                """)

        elif dealer > user:
            print("""
                                LO SIENTO, PERDISTE!!!!
                                
                                """)

        elif user == dealer:

            print("""
                                ESTO ES UN EMPATE!!!
                            
                                """)
    time.sleep(3)

    print ("""
                                FIN DEL JUEGO, REGRESA PRONTO...""")

    pregunta = input("Quieres jugar nuevamente?, SI teclea 1, NO, teclea 2")

    if pregunta == "1":
        jugar = True

    else:
        jugar = False