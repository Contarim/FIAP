print("Verificador de frequência cardíaca")

idade = int(input("Informe sua idade: "))
bpm = int(input("Informe seu BPM (Batimentos Por Minuto): "))

#Até 2 anos 120 a 140
#De 8 anos até 17 anos 80 a 100
#Adulto sedentário 70 a 80
#Idosos 50 a 60

#Condições para verificar se o BPM está na faixa adequada com a idade informada 
if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Frequência Cardíaca Normal!")
    else:
        print("Frequência Cardíaca fora do normal para a idade informada.")

elif idade >= 8 and idade <= 17:
    if bpm >= 80 and bpm <= 100:
        print("Frequência Cardíaca Normal!")
    else:
        print("Frequência Cardíaca fora do normal para a idade informada.")
        
elif idade >= 18 and idade <= 59:
    if bpm >= 70 and bpm <= 80:
        print("Frequência Cardíaca Normal!")
    else:
        print("Frequência Cardíaca fora do normal para a idade informada.")
        
else:
    if bpm >= 70 and bpm <= 80:
        print("Frequência Cardíaca Normal!")
    else:
        print("Frequência Cardíaca fora do normal para a idade informada.")
    
