arquivo = open("C:\\Users\\Emily\\Documents\\Projetos\\pythonDio\\05 - Manipulação de arquivos\\teste.txt","w")
arquivo.write("novo texto para teste ")
arquivo.writelines([" escrevendo ", "um novo ", "texto"])
arquivo.close()