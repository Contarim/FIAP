#Testando inserção fixa nos dicionários
dicionario = {}

dicionario["produto 1"] = "geladeira"
print(dicionario)

dicionario.update({"produto 2": "Notebook"})
print(dicionario)


#Adicionando items no dicionario com base na entrada do usuário
print("\n\n")
funcionarios = {}

while input("Gostaria de cadastrar um funcionario? S para SIM / N para NÃO\n").strip().upper() == "S":
    nome = input("Digite o nome do funcionario: ")
    cargo = input("Digite o cargo do funcionario: ")
    funcionarios.update({nome:cargo})
    
print(funcionarios)