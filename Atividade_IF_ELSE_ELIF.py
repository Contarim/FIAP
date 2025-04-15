#Uma empresa vai dar uma quantidade de bônus de internet de acordo com a pontuação que o cliente tem, para isso, vamos solicitar ao cliente para informar a quantidade de pontos que ele tem e devolver o resultado de informando o quanto de bônus ele vai ganhar

# 500 pontos = 6GB bonus
# 200 pontos = 3GB bonus
# 100 pontos = 1GB bonus

pontuacao = int(input('Digite a quantidade de pontos que você possui: '))

if pontuacao >= 500:
    print('Você receberá 6Gb de Bonus de internet!')

elif pontuacao >= 200:
    print('Você receberá 3Gb de Bonus de internet!')
    
elif pontuacao >= 100:
    print('Você receberá 1Gb de Bonus de internet!')
    
else:
    print('Você não receberá Bonus de internet, pois a quantidade mínima para receber um Bonus é de 100 Pontos')

