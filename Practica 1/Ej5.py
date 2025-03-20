lista_numeros = []
n = int(input("Ingresa una lista de numeros. Finaliza con el numero 99"))

while n != 99:
    lista_numeros.append(n)
    n = int(input())

for numero in lista_numeros:
    if numero < 0:
        print(f'Se encontró un número negativo.')
        break 
    print(f'El resultado es: {numero}')
