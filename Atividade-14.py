valores = [2, 1, 30, 4, 50, 10, 15, 2, 1]

#exibição da lista
print(f'A lista foi criada assim {valores}')

#contando quantas vezes o elemento especificado aparece na lista
contagem = valores.count(1)
print(f'A quantidade de numero 1 na lista é de: {contagem}')

#invertendo a lista
valores.reverse()
print(f'Lista invertida: {valores}')

#ordenando a lista
valores.sort()
#usando REVERSE TRUE OU FALSE para ordenar a lista invertida
#valores.sort(reverse=true)
print(f'Lista em ordem crescente: {valores}')

#tamanho da lista:
quantidade = len(valores)
print(f'A lista tem {quantidade} elementos dentro dela')

#somando os elementos da lista
soma = sum(valores)
print(f'A soma de todos os itens da lista é de: {soma}')