notas = []

while input('Deseja inserir uma nota? S - SIM | N - NÃO : ').upper() != "N":
    notas.append(float(input('Por favor, insira a nota: ')))

media = sum(notas) / len(notas)

print(f'\nPara as notas digitas a média foi de {media:.2f}')