pokemon = ['Charmander', 'Bulbasaur', 'Squirtle', 'Pikachu', 'Scyther']
print(f'Lista completa\n\n{pokemon}\n')

#Removendo o ultimo item utilizando POP
pokemon.pop()
print(f'Lista após remoção do último item\n\n{pokemon}\n')

#Removendo um elemento específico da lista usando também o POP
pokemon.pop(1)
print(f'Lista após remoção de uma posição específica\n\n{pokemon}\n')

#Removendo um pokemon pelo nome utilizando o REMOVE
pokemon.remove('Squirtle')
print(f'Lista após a remoção do pokemon pelo nome\n\n{pokemon}\n')

#Apagando todos os itens da lista usando CLEAR
pokemon.clear()
print(f'Lista após a remoção de todos os pokemons\n\n{pokemon}\n')
