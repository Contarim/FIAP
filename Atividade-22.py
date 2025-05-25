#Aprendendoo a criar e mostrar chaves e valores de um dicionário
dicionario = {
    "Produto 1": "Notebook",
    "Produto 2": "Geladeira",
    "Produto 3": "Microondas",
    "Produto 4": "Cama",
    "Produto 5": "Ventilador",
    "Produto 6": "Mesa",
}
print("\n")
print(dicionario["Produto 2"])

print("\n")
print(dicionario.get("Produto 3"))

print("\n")
print(dicionario.keys())

print("\n")
for chave in dicionario.keys():
    print(dicionario[chave])

print("\n")    
print(len(dicionario.values()))

print("\n")
print("Produto 1" in dicionario)

print("\n")
print(dicionario.items())

print("\n")
for produto, descricao in dicionario.items():
    print(f"O {produto} é um(a) {descricao}")


