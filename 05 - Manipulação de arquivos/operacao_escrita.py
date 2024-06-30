arquivo = open("C:\\Users\\Emily\\Documents\\Projetos\\pythonDio\\05 - Manipulação de arquivos\\teste.txt","w")
arquivo.write("novo texto para teste ")
arquivo.writelines(["\n","escrevendo ", "\num novo ", "\ntexto"])
arquivo.close()