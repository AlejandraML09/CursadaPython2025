lista_numeros = []
n = int(input("Ingresa una lista de numeros enteros. Finaliza con el numero 99"))

while n != 99:
    lista_numeros.append(n)
    n = int(input())

cadena = ""

#Excluyo a los múltiplos de 3 con el mod = 0
for numero in lista_numeros:
    if numero % 3 == 0: 
        continue
    else:
# En la cadena le voy sumando los numeros convertidos en string, luego que agrego uno los voy separando con un -        
        cadena += str(numero)
        cadena += "-"
print(f'Imprimo la lista de numeros antes de la conversión: {lista_numeros}')
print(f'Imprimo la cadena convertida:{cadena}')