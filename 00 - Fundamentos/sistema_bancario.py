menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    deposito = 0
    saque = 0
    
    if opcao == "d":
        deposito = float(input("digite o valor para depositar => "))
               
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"     
        else:
            print("O valor informado é inválido") 
                 
    elif opcao == "s":     
        saque = float(input("digite o valor que deseja sacar => "))
          
        excedeu_saldo = saque > saldo
        
        excedeu_limite = saque > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Saldo insuficiente")
        elif excedeu_limite:
            print("Valor do saque excede o limite")
        elif excedeu_saques:
            print("Número máximo de saques excedido")
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n" 
            numero_saques += 1
        else:
            print("O valor informado é inválido")
            
    elif opcao == "e":
        print("\n **** EXTRATO ****")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print("*************************")      
        
    elif opcao == "q":
        break
    
    else:
        print("Opção inválida!")