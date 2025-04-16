# coleta o valor da dívida 
divida = float(input("Digite o valor da dívida: "))
print("\n")

# listas com parcelas e juros conforme exemplo citado no exercício
parcelas = [1, 3, 6, 9, 12]
juros = [0, 10, 15, 20, 25]

# loop para calcular juros, total e o valor de cada parcela, após o calculo ele vai mostrar o resultado e repetir até que seja feito para todas as opções das listas
for i in range(len(parcelas)):
    qnt_parcela = parcelas[i]
    taxa_juros = juros[i]
    
    valor_juros = divida * taxa_juros / 100
    total = divida + valor_juros
    valor_parcela = total / qnt_parcela
    
    print(f"Total:R$ {total:.2f} Juros:R$ {valor_juros:.2f}, Número de parcelas:{qnt_parcela} Valor da Parcela:R$ {valor_parcela:.2f}")

print("\n")
