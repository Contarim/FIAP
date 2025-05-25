#Aprendendo a remover chaves, valores e itens dos dicionários

dicionario = {
    "produto 1" : "TV",
    "produto 2" : "Notebook",
    "produto 3" : "Mesa",
    "produto 4" : "Tênis",
    "produto 5" : "Chinelo",
}

print("\n",dicionario)

dicionario.pop("produto 1")
print("\n",dicionario)

dicionario.popitem()
print("\n",dicionario)

dicionario.clear()
print("\n",dicionario)
