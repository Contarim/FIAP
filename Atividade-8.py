qntd_transacoes = int(input("Informe quantas transaçôes foram feitas: "))

total = 0
media = 0

#coleta os valores e calcula o total das transações
for transacao in range(1, qntd_transacoes+1, 1):
    valor = float(input(f"Informe o valor da transação {transacao}: "))
    total = total + valor

#calcula a média das transações
media = total / qntd_transacoes

#mostra os resultados finais
print(f"Quantidade de transações: {qntd_transacoes}\nValor total das transações: {total:.2f}\nValor médio das transações: {media:.2f}")
    