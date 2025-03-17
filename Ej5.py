lista_numeros = []
n = int(input("Ingresa una lista de numeros del 1 al 10. Finaliza con el numero 10 "))

while n != 99999:
    lista_numeros.append(n)
    n = int(input())

for numero in lista_numeros:
    if numero < 0:
        break 
    print(f'El resultado es: {numero}')
