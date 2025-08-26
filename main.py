menu = """
****** Sistema Bancário *******

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

*******************************
"""

saldo = 0
limite = 500
extrato = ""
numero_saques  = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)
    if opcao == '1':
        valor = float(input('Insira o valor para deposito R$ '))
        if valor >0:
            print (f'\nDepósito de R${valor} realizado com sucesso \n')
            saldo += valor
            extrato += f'Depósito R${valor}\n'

    elif opcao == '2':
        valor = float(input('Insira o valor para saque R$ '))
        if (numero_saques <= LIMITE_SAQUES) and (valor <= limite) and (valor <= saldo):
            print (f'\nSaque de R${valor} realizado com sucesso \n')
            saldo -= valor
            extrato += f'Saque R${valor} \n'
            numero_saques +=1
        elif valor > saldo:
            print ('Saldo insuficiente')
        elif valor > limite:
            print (f'Limite de saque por operação de R${limite}. Por favor insira um valor menor')
        elif numero_saques > LIMITE_SAQUES:
            print ('Quantidades de saques diárias atingidas. Por favor retorne amanhã')
        else:
            print('Erro ao processar a operação, tente mais tarde.')


    elif opcao == '3':
        print("\n*********** EXTRATO ***********")
        print(f" {extrato}")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("*******************************")


    elif opcao == '0':
        
        print ('Sair')
        break
    else:
        print('Opção inválida, tente novamente')