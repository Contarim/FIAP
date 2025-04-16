# mostra os dias para escolher  
print("Dias disponíveis para votação")
print("1 - Segunda-feira\n2 - Terça-feira\n3 - Quarta-feira\n4 - Quinta-feira\n5 - Sexta-feira")

# coleta a quantidade de colaboradores que vão votar
quantidade = int(input("\nQuantos colaboradores irão votar? "))

# dicionário para contar os votos
votos = {
    1: 0,  # segunda
    2: 0,  # terça
    3: 0,  # quarta
    4: 0,  # quinta
    5: 0   # sexta
}

# dicionário dos nomes e números dos respectivos dias
nomes_dias = {
    1: "Segunda-feira",
    2: "Terça-feira",
    3: "Quarta-feira",
    4: "Quinta-feira",
    5: "Sexta-feira"
}

# coleta os votos dos colaboradores
for i in range(quantidade):
    voto = int(input(f"Colaborador {i+1}, digite o número do dia (1 a 5): "))
    if voto in votos:
        votos[voto] += 1
    else:
        print("Número incorreto! Voto não foi contabilizado.")

# mostra os resultados
print("\nResultado da votação:")
for numero in votos:
    print(f"{nomes_dias[numero]}: {votos[numero]} voto(s)")

# verifica os dias votados
maior_voto = max(votos.values())
dias_mais_votados = []

for numero in votos:
    if votos[numero] == maior_voto:
        dias_mais_votados.append(numero)

# retorna o resultado final informando se houve um dia mais votado ou se teve empate, em caso de mais de 1 empate, mostra todos os dias que obteram a mesma quantidade de votação
if len(dias_mais_votados) == 1:
    print(f"\nDia escolhido para a live: {nomes_dias[dias_mais_votados[0]]}")
else:
    print("\nHouve um empate entre os seguintes dias:")
    for numero in dias_mais_votados:
        print(f"- {nomes_dias[numero]}")
