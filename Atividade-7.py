quantidade_alimentos = int(input("Informe a quantidade de alimentos que você consumiu hoje: "))

total_calorias = 0

#loop com a quantidade de alimentos que foi informada solicitando a quantidade de calorias que cada um deles tinha, nesse mesmo loop será calculado o total de calorias.
for alimento in range(1, quantidade_alimentos + 1, 1):
    calorias = float(input(f"\nInforme as calorias do alimento {alimento}: "))
    total_calorias = total_calorias + calorias

print(f"\nVocê consumiu {quantidade_alimentos} alimentos\nTotal de calorias consumidas: {total_calorias:.2f}\nMédia de calorias por alimento: {total_calorias / quantidade_alimentos:.2f}\n")