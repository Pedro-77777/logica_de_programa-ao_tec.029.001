# entrada de dados
nome = input("informe o nome: ").strip().title()
nota1 = int(input("informe a nota 1: "))
nota2 = int(input("informe a nota 2: "))

# processamento de dados 
media = (nota1+nota2)/2

# saida de dados 
print(f"Media: {media}")

# estrutura de decisao 
if media >= 7:
    print(f"{nome} esta aprovado.")
elif media >= 5:
    print(f"{nome} esta de recuperaçao.")
else: 
    print(f"{nome} esta reprovado.")
    
