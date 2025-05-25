#utilizando condição IF para verificar se o item digitado está dentro da tupla
Categorias = ("A", "B", "C", "D", "E")

Categoria = input("Digite a categoria de sua CNH: ")

if Categoria.upper() in Categorias:
    print("Categoria Válida!")
    
else:
    print("Categoria Inválida!") 