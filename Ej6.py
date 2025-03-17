lista_numeros = []
numeros_impares = []
numeros_pares = []
n = int(input("Ingresa una lista de numeros. Finaliza con el numero 99"))

while n != 99:
    lista_numeros.append(n)
    n = int(input())

for numero in lista_numeros:
    if numero % 2 != 0:
        numeros_impares.append(numero) 
    else:
        numeros_pares.append(numero)       

for numero_impar in numeros_impares:
    print(f'La lista de numeros impares es: {numero_impar}')

for numero_par in numeros_pares:
    print(f'La lista de numeros pares es: {numero_par}')