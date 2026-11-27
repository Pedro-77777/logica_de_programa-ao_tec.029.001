# entrada de dados 
nome = input("informe seu nome: ").strip().title()
idade = int(input("informe sua idade: "))

# estrutura de decisao 
if idade >= 18:
    print(f"{nome} e maior de idade.")
else:
    print(f"{nome} e menor de idade.")
    