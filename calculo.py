#Função de soma
def soma (a, b):
    return float(a) + float(b)

#Função de subtração
def subtracao (a, b):
    return float(a) - float(b)

#Função de divisão
def divisao (a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return float(a) / float(b)

#Função de multiplicação
def multiplicacao (a, b):
    return float(a) * float(b)