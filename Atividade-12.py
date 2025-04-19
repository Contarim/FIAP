personagem = ['Goku', 'Naruto']
print(f"Lista atual: {personagem}")

#inserindo um valor fixo
personagem.append("Vegeta")
print(f'lista após a primeira inserção: {personagem}')

#inserindo um elemento com input
personagem.append(input('Informe um personagem: '))
print(f'Lista após a inserção do personagem: {personagem}')

#lista após inserção de um personagem em uma posição específica
personagem.insert(3, 'Pikachu')
print(f'Lista após o personagem ser inserido na posição específicada: {personagem}')