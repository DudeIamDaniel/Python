def conversor(tipo_dato, valor_dolar):
    pesos = input('Cuantos pesos ' + tipo_dato + ' tienes?: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' '+ 'dolares')


menu = """
Bienvenido al el conversor de moneda 💲

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion:

"""

opcion = input(menu)

if opcion == '1':
    conversor('colombianos', 3875)
elif opcion == '2':
    conversor('argentinos', 65)
elif opcion == '3':
    conversor('mexicanos', 24)
else:
    print('Ingresa una opcion correcta')



# def suma(a, b):
#     print('La suma de los dos numeros es: ')
#     resultado = a + b
#     return resultado

# sumatoria = suma(2, 4)
# print(sumatoria)






