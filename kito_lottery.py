from random import randint
from time import sleep

# Lotería Kito
CANTIDAD_NUMEROS_PREMIADOS = 6
NUMEROS_POSIBLES = 41

numeros_premiados = list()
numeros_seleccionados = list()

def generar_sorteo():
    print("\nGenerando sorteo", end='')
    sleep(1)
    print(".", end='')
    sleep(1)
    print(".", end='')
    sleep(1)
    print(".")
    while len(numeros_premiados) != CANTIDAD_NUMEROS_PREMIADOS:
        numero_premiado = randint(1, NUMEROS_POSIBLES)
        if numero_premiado in numeros_premiados:
            continue
        numeros_premiados.append(numero_premiado)
    print("\nLos números ganadores para esta ronda son: ")
    for numero_premiado in numeros_premiados:
        print(f"{numero_premiado} .", end=' ')

def seleccionar_numero():
    global numeros_seleccionados
    cantidad_faltante = CANTIDAD_NUMEROS_PREMIADOS - len(numeros_seleccionados)
    msj = f"Ingrese número a jugar: (Te falta elegir {cantidad_faltante} más)"
    print(msj)
    texto_ingresado = input()
    if texto_ingresado.isdigit():
        numero_seleccionado = int(texto_ingresado)
        if numero_seleccionado in numeros_seleccionados:
            print("Número ya seleccinado, intente nuevamente.")
        elif numero_seleccionado > NUMEROS_POSIBLES or 1 > numero_seleccionado:
            print(f"Fuera de rango: el límite para cada número es desde 1 hasta {NUMEROS_POSIBLES}")
        else:
            numeros_seleccionados.append(numero_seleccionado)
    else:
        print("Sólo se permiten números para este sorteo.")

def revisar_numeros_seleccionados():
    CANTIDAD_ACIERTOS = CANTIDAD_NUMEROS_PREMIADOS * 2 - len(set(numeros_premiados + numeros_seleccionados))
    if CANTIDAD_ACIERTOS == CANTIDAD_NUMEROS_PREMIADOS:
        print("\n¡FELICIDADES, GANASTE EL PREMIO MAYOR!")
    print(f"\nLograste encontrar {CANTIDAD_ACIERTOS} números premiados.")
    if CANTIDAD_ACIERTOS > 0 and CANTIDAD_ACIERTOS != CANTIDAD_NUMEROS_PREMIADOS:
        print("Le acertaste al: ", end='')
        for numero_acertado in set.intersection(set(numeros_premiados), set(numeros_seleccionados)):
            print(f"{numero_acertado}", end=' ')

def main():
    print("Bienvenido a Kito, el juego de lotería.\n")
    numeros_seleccionados.clear()
    numeros_premiados.clear()
    while len(numeros_seleccionados) != CANTIDAD_NUMEROS_PREMIADOS:
        seleccionar_numero()
    print("\nTus números seleccionados fueron: ")
    for numero_seleccionado in numeros_seleccionados:
        print(f"{numero_seleccionado} .", end=' ')
    print()
    generar_sorteo()
    print()
    revisar_numeros_seleccionados()
    if input('\n\n¿Volver a jugar? S/N\n').upper() == 'S':
        main()

main()
