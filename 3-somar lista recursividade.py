##Usando recursividade, calcule a soma de todos os
##valores de um array de números reais.



valor=int(input('Digite a quantidade de numeros :'))
index=valor-1
numeros=[]

for x in range(0, valor):
    numeros.append(int(input('Digite os numeros:' )))
print(index)
print(valor)

def função(valor,numeros):
        if (valor == 0):
            return 0
        else:
            return numeros[index]+ função(valor-1,numeros)

print("A soma de todos os numeros é "+str (função(valor,numeros)))
