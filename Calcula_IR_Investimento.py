print("Escolha o tipo de investimento\n") 
print("1. CDB\n2. LCI\n3. LCA\n")

# solicitando ao cliente o tipo de investimento que ele irá fazer o resgate
tipo = int(input("Digite o tipo de investimento (1, 2 ou 3): "))

# condição IF para verificar se o tipo selecionado é válido
if tipo < 1 or tipo > 3:
    print("Tipo de investimento inválido!")
    
else:
    valor = float(input("Digite o valor a ser resgatado: "))
    dias = int(input("Digite o número de dias que o valor permaneceu investido: "))
    
    imposto = 0

# condição IF para verificar se o tipo é igual a 1 (CDB) que é o único investimento com IR, ou seja, se o investimento não for 1 o IR será 0 e vamos pular para o PRINT informando o valor do IR a ser pago
if tipo == 1: 
    if dias <= 180:
            imposto = valor * 0.225
    elif dias <= 360:
            imposto = valor * 0.20
    elif dias <= 720:
            imposto = valor * 0.175
    else:
            imposto = valor * 0.15

    print(f"\nO valor do imposto de renda(IR) a ser pago é: R$ {imposto:.2f}\n")

else:
    print("\nEste tipo de investimento (LCI/LCA) é isento de imposto de renda.")
