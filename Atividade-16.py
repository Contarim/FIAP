#função para receber os dados de velocidade e tempo de viagem, calcular a velocidade média e devolver para o usuário
def velocidade_media(distancia, tempo):
    vm = distancia / tempo
    print(f'A velocidade média foi de {vm:.2f}')

#coleta a distancia e tempo da viagem e manda para a função calcular
distancia = float(input('Informa a distancia percorrida: '))
tempo = float(input('Informe o tempo de viagem em horas:  '))

#chama a função
velocidade_media(distancia, tempo)