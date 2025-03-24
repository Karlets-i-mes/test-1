# JUEGO CONECTA 4

# VARIABLES GLOBALES
jugador1 = 1
jugador2 = 2
color_jugador1 = "RED"  # Asociamos colores a los jugadores
color_jugador2 = "YELLOW"
tablero =""
n_movimientos = 0
partidas_ganadas_jugador1 = 0
partidas_ganadas_jugador2 = 0
turno = jugador1
fila_vacia=""
x=""
y=""

# FUNCIONES
def obtener_entrada_valida(eje):  # Función para validar entradas
    """
    Función para comprobar si la fila o columna introducidas son válidas

    Args:
        eje: x para fila; y para columna

    Returns:
        verifica si el dato introducido es correcto
    """
    while True:
        entrada = input(f"Escribe un número entero de 0 a 6 para la {eje}: ")
        if entrada.isdigit() and 0 <= int(entrada) <= (5 if eje == "Fila" else 6):
            return int(entrada)
        else:
            print("Entrada inválida.")

def crear_tablero():
    """
    Imrpime el tablero de forma inversa
    recorriendo desde la fila 6 hacia abajo, como se veria en un tablero

    Args:
        tablero: Una lista de listas que representa el tablero de Conecta 4.

    Returns:
        Imprime el tablero como se veria en un tablero
    """
    tablero = [[0 for _ in range(7)] for _ in range(6)]
    return tablero

def cambiar_turno():
    """
    Función para cambiar el turno del jugador

    Args:
        sin argumentos, al utilizar la variable global turno

    Returns:
        cambia la variable global turno y devuelve el turno del jugador
    """
    global turno
    #print(f"Turno del jugador {turno}:")
    #print("cambiamos turno")
    turno = jugador1 if turno == jugador2 else jugador2
    #print(f"Ahora es el turno del jugador {turno}:")
    return turno

def mostrar_tablero(tablero):
    """
    Imrpime el tablero de forma inversa
    recorriendo desde la fila 6 hacia abajo, como se veria en un tablero

    Args:
        tablero: Una lista de listas que representa el tablero de Conecta 4.

    Returns:
        Imprime el tablero como se veria en un tablero
    """
    for fila in reversed(tablero): #Iteramos sobre el tablero en orden inverso
        print(fila) #Imprime cada fila del tablero

def encontrar_fila_vacia(tablero, columna):
  """
  Encuentra la primera fila vacía (0) en una columna del tablero,
  recorriendo desde la fila 0 hacia abajo.

  Args:
    tablero: Una lista de listas que representa el tablero de Conecta 4.
    columna: El índice de la columna en la que buscar.

  Returns:
    El índice de la primera fila vacía en la columna, o None si la columna está llena.
  """
  for fila in range(6):  # Recorremos las filas desde 0 hasta el final
    if tablero[fila][columna] == 0:
      #print(f"{fila}, {columna} es {tablero[fila][columna]}")
      return fila  # Devolvemos el índice de la primera fila vacía encontrada
    #else:
    #  print(f"{fila}, {columna} es {tablero[fila][columna]}")
  #return None  # La columna está llena

def comprobar_ganador(turno=turno, x=x, y=fila_vacia, tablero=tablero):
    """
    La idea es comprobar si la tirada del turno  que se hace, gana la partida
    Comprueba en todas las direcciones posibles si hay 4 en raya

    Args:
        utiliza las variables globales

    Returns:
        True/False dependiendo si se ha ganado o no
    """
    
    
    # Comprobamos las direcciones horizontales
    for fila in range(6):
        for columna in range(4):
            if tablero[fila][columna] == tablero[fila][columna + 1] == tablero[fila][columna + 2] == tablero[fila][columna + 3] == turno:
                return True

    # Comprobamos las direcciones verticales
    for fila in range(3):
        for columna in range(7):
            if tablero[fila][columna] == tablero[fila + 1][columna] == tablero[fila + 2][columna] == tablero[fila + 3][columna] == turno:
                return True

    # Comprobamos las direcciones diagonales positivas
    for fila in range(3):
        for columna in range(4):
            if tablero[fila][columna] == tablero[fila + 1][columna + 1] == tablero[fila + 2][columna + 2] == tablero[fila + 3][columna + 3] == turno:
                return True

    # Comprobamos las direcciones diagonales negativas    
    for fila in range(3):
        for columna in range(3, 7):
            if tablero[fila][columna] == tablero[fila + 1][columna - 1] == tablero[fila + 2][columna - 2] == tablero[fila + 3][columna - 3] == turno:
                return True

def jugar_de_nuevo():
    """
    después de finalizar una partida, pregunta si quieren hacer otra partida,
    otro juego, o salir

    Args:
        utiliza las variables globales

    Returns:
        otra partida: inicia una nueva partida y conserva contadores de partida
        otro juego:  inicia una nueva partida y reinicia los contadores
        salir: acaba el juego
    """
    
    jugar_de_nuevo = input("¿Quieres jugar otra partida? (s/n): ")
    if jugar_de_nuevo.lower() == "s":
        iniciar_partida()
    else:
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_de_nuevo.lower() == "s":
            iniciar_juego()
        else:
            print("¡Hasta luego!")

def jugar():
    """
    Función princial, en bucle principal hasta que se gane
    inicia preguntando fila y columna
    comprueba si la celda esta vacia y si es así cua es la primera fila libre donde poner la ficha.
    Comprueba si hay ganador, en ese caso se sale del bucle principal
    pregunta si quieren jugar de nuevo

    Args:
        utiliza las variables globales

    Returns:
        ganador, partidas_ganadas_jugador1, partidas_ganadas_jugador2
        Cambia de turno, dentro del bucle, en caso de no haber ganador    
    """

    # recuperamos el valor de las variables globales
    global turno, n_movimientos, tablero, partidas_ganadas_jugador1, partidas_ganadas_jugador2  # Indicamos que modificaremos variables globales

    ganar = False

    while ganar==False:
        # indicamos quien juega y su color
        print(f"Turno del jugador {turno} ({color_jugador1 if turno == jugador1 else color_jugador2}):")

        # pregunamos fila y columna, con función que verifica si es correcta la respuesta
        x = obtener_entrada_valida("Fila")
        y = obtener_entrada_valida("Columna")

        # comprobamos si la celda esta vacia
        if tablero[x][y] == 0:  # Verificamos si la celda está vacía

            # comprobar la última fila de la columna que esta llena
            fila_vacia = encontrar_fila_vacia(tablero, y)
            #print(fila_vacia)
            
            #ponemos la ficha en la primera fila disponible de la columna [y]
            tablero[fila_vacia][y] = turno

            #mostramos el tablero como ha quedado
            mostrar_tablero(tablero)
            
            #comprobamos si hay ganador
            if comprobar_ganador(turno, x, fila_vacia, tablero)==True:
                print(f"El jugador {turno} ha ganado!")  

                # incrementamos las partidas ganadas
                if turno == jugador1:
                    partidas_ganadas_jugador1 += 1
                else:
                    partidas_ganadas_jugador2 += 1

                print(f"Partidas ganadas jugador 1: {partidas_ganadas_jugador1}")
                print(f"Partidas ganadas jugador 2: {partidas_ganadas_jugador2}") 

                # salir del bucle
                ganar = True 

            else: # Si no hay ganador, cambiaos turno e incrementamos n_movimientos
                #cambiamos el turno
                turno = cambiar_turno()
                # incrementamos n_movimientos
                n_movimientos += 1

        else: # else del ==0
            print(f"La celda ({x}, {y}) ya esta ocupada.")

    # funcion si se quiere jugar de nuevo
    jugar_de_nuevo()

def iniciar_juego():
    print("Comienza el juego!")
    print("Las filas son del 0 al 5 y las columnas del 0 al 6.")
    global turno, n_movimientos, tablero, partidas_ganadas_jugador1, partidas_ganadas_jugador2
    turno = jugador1
    n_movimientos = 0
    tablero = crear_tablero()
    partidas_ganadas_jugador1 = 0
    partidas_ganadas_jugador2 = 0
    '''
    print(f"Turno inicial: Jugador {turno}")
    print(f"Número de movimientos inicial: {n_movimientos}")
    mostrar_tablero(tablero) #Usamos la funcion creada para mostrar el tablero
    print(f"Jugador 1: {jugador1}")
    print(f"Jugador 2: {jugador2}")
    '''
    jugar()

def iniciar_partida():
    print("Comienza la partida")
    print("Las filas son del 0 al 5 y las columnas del 0 al 6.")
    global turno, n_movimientos, tablero, partidas_ganadas_jugador1, partidas_ganadas_jugador2
    #turno = jugador2
    n_movimientos = 2
    tablero = crear_tablero()
    mostrar_tablero(tablero=tablero)
    partidas_ganadas_jugador1 = 2
    partidas_ganadas_jugador2 = 20
    '''
    print(f"Turno inicial: Jugador {turno}")
    print(f"Número de movimientos inicial: {n_movimientos}")
    mostrar_tablero(tablero) #Usamos la funcion creada para mostrar el tablero
    print(f"Jugador 1: {jugador1}")
    print(f"Jugador 2: {jugador2}")
    print(f"Jugador 1: {jugador1}: {partidas_ganadas_jugador1}")
    print(f"Jugador 2: {jugador2}: {partidas_ganadas_jugador2}")
    '''
    jugar()

#Ejemplo de como iniciar el juego.
#iniciar_juego()

#Ejemplo de como iniciar una nueva partida.
iniciar_partida()



'''
if __name__ == "__main__":  # Comprobamos si el archivo se esta ejecutando directamente
    iniciar_juego()
 '''   
