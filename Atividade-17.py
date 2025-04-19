#função para receber os dados de velocidade e tempo de viagem, calcular a velocidade média e devolver 
def velocidade_media(distancia, tempo):
    vm = distancia / tempo
    return vm

#lista vazia que será preenchidas com os dados que voltam da função
velocidades_medias = []

#coleta a distancia e tempo da viagem e manda para a função calcular
for dia in ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']: 
    distancia = float(input(f'\nInforma a distancia percorrida na  {dia}: '))
    tempo = float(input(f'Informe o tempo de viagem da {dia}: '))
    #chama a função e os dados que retornam são colocados na lista
    velocidades_medias.append(velocidade_media(distancia, tempo))

#exibe a lista que era vazia após ela ser preenchida com os dados retornados pela função
print(f'A velocidade média referente aos dias da semana foi de {velocidades_medias}')