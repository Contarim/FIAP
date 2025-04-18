numero_usuario = int(input("Digite um número inteiro: "))
print("")

ant1 = 1
ant2 = 0 

#loop para calcular e mostra os numeros da sequência
for n_elementos in range(1, numero_usuario + 1, 1):
    atual = ant1 + ant2
    ant1 = ant2
    ant2 = atual
    print(atual, end=" ")
    #condição caso o numero esteja na sequência
    if numero_usuario == atual:
        print("\n\nNúmero informado está na sequência de Fibonacci!")
        break
    #condição caso o número NÂO esteja na sequência
    elif numero_usuario < atual:
        print("\n\nNúmero informado não está na sequência de Fibonnaci :(\n")
        break
    