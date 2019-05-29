## Implemente uma função recursiva que, dados dois números
## inteiros x e n,
## calcula o valor de x^n.

x=int(input("Digite um numero para ser elevado: "))
n=int(input("Digite o valor para ele se elevar"))
def função(n,x):
    if n == 0:
        return 1
    else:
        return x * função(n -1,x)


print(função(n,x))