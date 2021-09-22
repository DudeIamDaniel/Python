import random

def main():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Escribe un numero: '))
    while numero_aleatorio != numero_elegido:
        if numero_elegido < numero_aleatorio:
            print('Escribe un numero mas grande')
        else:
            print('Escribe un numero mas pequeño')
        numero_elegido = int(input('Escribe otro numero: '))
    print('Ganaste')

if __name__ == '__main__':
    main()

