# Solicita ao usuário o valor bruto do pacote de viagem
valor_bruto = float(input("Insira o valor bruto do pacote: ")) 

# Exibe as opções de categorias de assento
print("\nCategorias dos assentos para o Voo\n1 - Econômica\n2 - Executiva\n3 - Primeira Classe\n")

# Solicita ao usuário a categoria escolhida
categoria = int(input("Informe a categoria do assento do Voo: "))

# Solicita a quantidade de pessoas que irão viajar
qntd_pessoas = int(input("Informe a quantidade de pessoas que vão viajar: "))

# Inicializa as variáveis com zero para evitar erros
desconto = 0
valor_liquido = 0
media_viajante = 0

# Verifica se a categoria é válida (1, 2 ou 3)
if categoria >= 1 and categoria <= 3:
    
    # Categoria 1: Econômica
    if categoria == 1:
        if qntd_pessoas <= 2:
            desconto = valor_bruto * 0.03  # 3% de desconto
        elif qntd_pessoas == 3:
            desconto = valor_bruto * 0.04  # 4% de desconto
        else:
            desconto = valor_bruto * 0.05  # 5% de desconto

    # Categoria 2: Executiva
    elif categoria == 2:
        if qntd_pessoas <= 2:
            desconto = valor_bruto * 0.05  # 5% de desconto
        elif qntd_pessoas == 3:
            desconto = valor_bruto * 0.07  # 7% de desconto
        else:
            desconto = valor_bruto * 0.08  # 8% de desconto

    # Categoria 3: Primeira Classe
    elif categoria == 3:
        if qntd_pessoas <= 2:
            desconto = valor_bruto * 0.10  # 10% de desconto
        elif qntd_pessoas == 3:
            desconto = valor_bruto * 0.15  # 15% de desconto
        else:
            desconto = valor_bruto * 0.20  # 20% de desconto

    # Calcula o valor líquido
    valor_liquido = valor_bruto - desconto

    # Calcula a média por viajante
    media_viajante = valor_liquido / qntd_pessoas

    # Exibe os resultados finais
    print(f"\nValor bruto da Viagem: R$ {valor_bruto:.2f}")
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Valor líquido da viagem: R$ {valor_liquido:.2f}")
    print(f"Valor médio por viajante: R$ {media_viajante:.2f}\n")

else:
    # Mensagem de erro caso a categoria informada seja inválida
    print("\nA categoria selecionada está incorreta, revise a categoria escolhida.\n")
