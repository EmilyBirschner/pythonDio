texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end= "")
        
else: #não é muito comum
    print() #adiciona uma quebra de linha
    print("Escuta no final do laço!")