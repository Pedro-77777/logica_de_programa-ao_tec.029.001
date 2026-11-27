# entrada de dados
massa = float(input("informe a massa muscular: ").replace(",","."))
altura = float(input("informe sua altura: ").replace(",","."))

if massa <= 140 and altura >= 1.15:
    print(f"entrada do usuario permitida.")
else:
    print(F"entrada do usuario negada.")

