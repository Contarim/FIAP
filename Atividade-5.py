print("Tipos de Assinatura") 
print("\n1 - Basic\n2 - Silver\n3 - Gold\n4 - Platinum\n")

assinatura = int(input("Informe o número correspondente a sua assinatura: "))
faturamento = float(input("Informe seu faturamento anual: "))

bonus = 0

if assinatura == 1:
    bonus = faturamento * 0.30

elif assinatura == 2:
    bonus = faturamento * 0.20

elif assinatura == 3:
    bonus = faturamento * 0.10

elif assinatura == 4:
    bonus = faturamento * 0.05

else:
    print("Número que corresponde à assinatura está incorreto.")
    exit()  # Encerra o programa se o número da assinatura não for entre 1 e 4

print(f"Sua assinatura é a {assinatura}, seu faturamento foi {faturamento} e o bônus a pagar é de {bonus:.2f}")
