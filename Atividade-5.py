print("Tipos de Assinatura") 
print("\nBasic\nSilver\nGold\nPlatinum\n")

assinatura = input("Informe sua assinatura: ")
faturamento = float(input("Informe seu faturamento anual: "))

bonus = 0

if assinatura.upper() == "BASIC":
    bonus = faturamento * 0.05

elif assinatura.upper() == "SILVER":
    bonus = faturamento * 0.1

elif assinatura.upper() == "GOLD":
    bonus = faturamento * 0.2

elif assinatura.upper() == "PLATINUM":
    bonus = faturamento * 0.3

else:
    print("Número que corresponde à assinatura está incorreto.")
    exit()  # informa e encerra o programa se a assinatura foi informada errada

print(f"Sua assinatura é a {assinatura}, seu faturamento foi {faturamento} e o bônus a pagar é de {bonus:.2f}")
