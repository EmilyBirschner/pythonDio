arquivo = open("C:\\Users\\Emily\\Documents\\Projetos\\pythonDio\\05 - Manipulação de arquivos\\lorem.txt", "r")
print(arquivo.read())
arquivo.close()

arquivo = open("C:\\Users\\Emily\\Documents\\Projetos\\pythonDio\\05 - Manipulação de arquivos\\lorem.txt", "r")
print("\n\nreadline",arquivo.readline())
arquivo.close()

arquivo = open("C:\\Users\\Emily\\Documents\\Projetos\\pythonDio\\05 - Manipulação de arquivos\\lorem.txt", "r")
print("\n\nreadlines",arquivo.readlines())
arquivo.close()

arquivo = open(
    "C:\\Users\\Emily\\Documents\\Projetos\\pythonDio\\05 - Manipulação de arquivos\\lorem.txt", "r")
# tip
while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()