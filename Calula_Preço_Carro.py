# coleta o valor do carro 
valor = float(input("\nDigite o preço do carro: "))

# calcula e mostra o valor do carro se for pago á vista
vista = valor * 0.8
print(f"O preço final á vista com desconto 20% é: {vista}\n")

# lista com parcelas e acréscimos conforme exemplo do exercício
parcelas = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
acrescimos = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# loop para calcular e mostrar o valor total, valor de cada parcela e quantidade de parcelas
for i in range(len(parcelas)):
    p = parcelas[i]
    taxa = acrescimos[i]
    preco_final = valor + (valor * taxa / 100)
    valor_parcela = preco_final / p
    print(f"O preço final parcelado em {p}x é de R$ {preco_final:.2f} com parcelas de R$ {valor_parcela:.2f}")
    
print("\n")
