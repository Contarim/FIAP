#Minigame de batalha naval utiliando listas e tuplas

inimigos = [(10,5), (30,3), (1,50)]
inimigos_derrotados = 0

while len(inimigos) > 0:
    x = int(input("Digite um valor para o eixo X: "))
    y = int(input("Digite um valor para o eixo Y: "))

    if (x, y) in inimigos:
        print("\nVocê acertou um inimigo!")
        inimigos.remove((x, y))
        inimigos_derrotados += 1

    else:
        print("\nVocê Errou!")
    
    print(f"\nRestam {len(inimigos)} no mapa\n")

print(f"Parabéns! todos os {inimigos_derrotados} foram derrotados")