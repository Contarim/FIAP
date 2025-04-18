print("\nGostaria de fazer a tabuada de um número?")
condicao = str(input("\nS - SIM / N - NÃO = "))

while condicao.lower() == "s": 

    numero = int(input("\nInforme o numero para fazermos a tabuada: "))

    for calculo in range(1,11):
        resultado = calculo * numero
        print(f"{calculo} x {numero} = {resultado}")
        
    print("\nGostaria de fazer a tabuada de outro número?")
    condicao = str(input("\nS - SIM / N - NÃO = "))

print("\nVocê optou por não fazer uma tabuada. O programa será encerrado!\n")