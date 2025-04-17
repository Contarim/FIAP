playstation = 0
xbox = 0
nintendo = 0

for i in range(1, 6):
    print(f"Voto do membro {i}:")
    print("1 - PLAYSTATION")
    print("2 - XBOX")
    print("3 - NINTENDO\n")
    voto = int(input("Escolha o número correspondente ao console: "))

    if voto == 1:
        playstation += 1
    elif voto == 2:
        xbox += 1
    elif voto == 3:
        nintendo += 1
    else:
        print("\nVoto inválido, o mesmo não foi computado.\n")

# Verificando o console mais votado
if playstation > xbox and playstation > nintendo:
    print(f"\nO console escolhido foi o PLAYSTATION com {playstation} votos.")
elif xbox > playstation and xbox > nintendo:
    print(f"\nO console escolhido foi o XBOX com {xbox} votos.")
elif nintendo > playstation and nintendo > xbox:
    print(f"\nO console escolhido foi o NINTENDO com {nintendo} votos.")
else:
    print("\nHouve um empate!")  
