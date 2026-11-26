# entrada de dados
nome = input("informe seu nome: ").strip().title()
email = input("informe seu email: ").strip().lower()
cpf = input("informe seu cpf: ").strip()
telefone = input("informe seu telefone: ").strip()
idade = int(input("informe sua idade: "))
altura = float(input("informe sua altura: ").replace(",","."))

# saida de dados
print(f"Nome: {nome}")
print(f"Email: {email}")
print(f"CPF: {cpf}")
print(f"Telefone: {telefone}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura} metros")

