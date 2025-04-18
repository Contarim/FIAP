numero = int(input("Informe o número para fazermos o fatorail: "))
fatorial = numero

#Calcula o fatoral de acordo com o numero informado pelo usuário
for qntd_loop in range(1, numero):
    fatorial = fatorial * qntd_loop

print(f"O resutado do fatorial de {numero} é: {fatorial}")