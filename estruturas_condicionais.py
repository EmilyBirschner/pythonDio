MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar cnh")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas teóricas")
else:
    print("Ainda não pode tirar cnh")