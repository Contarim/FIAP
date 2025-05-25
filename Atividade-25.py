#Utilizando dicionários dentro de dicionários e função FOR para melhorar a exibição e visualização dos dados.
contato = {
    "João":
        {"celular": "123",
         "Email": "joao@gmail.com"},
    "Roger":
        {"Celular": "456",
         "Email": "Roger@gmail.com"},
    "Juliano":
        {"celular": "789",
         "Email": "Juliano@gmail.com"}
}

for nome, forma_contato in contato.items():
    print(f"{nome}")
    
    for tipo, contato in forma_contato.items():
        print(f"{tipo} - {contato}")
    print("-------------------------")