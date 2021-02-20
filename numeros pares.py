# Crear un programa que muestre los primeros 10 números pares a partir del producto de (10 x 10).

def generar_numeros_pares(n = 10):
    pares = []
    
    contador = 0
    numero = 0

    while contador < n:
        if numero % 2 == 0:
             pares.append(numero)
             contador += 1
        numero += 1

    return pares 

n = int(input('Escriba la cantidad de numeros:'))

if n > 0:
    pares = generar_numeros_pares(n)

    print(pares)
    print('cantidad de numeros pares:',len(pares))

else:
    print('El numero debe ser positivo')