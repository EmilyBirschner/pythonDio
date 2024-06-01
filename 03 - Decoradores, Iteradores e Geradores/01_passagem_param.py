def mensagem (nome):
    print('executando mensagem')
    return f'Oi {nome}!'

def mensagem_longa (nome):
    print('Executando mensagem longa')
    return f'Olá, tudo bem com vc, {nome}?'

def executar (funcao, nome):
    print('executando executar...')
    return funcao(nome)

print(executar(mensagem,"joao"))
print(executar(mensagem_longa,"maria"))