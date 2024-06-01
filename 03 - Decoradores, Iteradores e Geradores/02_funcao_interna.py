def principal():
    print("Executando a função principal...")
    
    def funcao_interna():
        print("Executando a função interna...")
        
    def funcao_interna_2():
        print("Executando a função interna 2...")
        
    funcao_interna()
    funcao_interna_2()
    
principal()