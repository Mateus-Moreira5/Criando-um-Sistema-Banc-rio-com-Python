saldo = 1000
saques_realizados = 0
limite_saque = 500
max_saques = 3

while True:
    comando = input("Escolha: \n[1] Sacar \n[2] Depositar \n[3] Mostrar saldo \n[4] Finalizar \nDigite aqui: ")
    
    if comando == '1':
        if saques_realizados >= max_saques:
            print("Você atingiu o limite máximo de saques diários.")
        else:
            sacar1 = int(input("Quanto deseja sacar: "))
            if sacar1 > saldo:
                print("Saldo insuficiente.")
            elif sacar1 > limite_saque:
                print(f"Valor inválido. O limite de saque é R${limite_saque}.")
            else:
                saldo -= sacar1
                saques_realizados += 1
                print(f"Você sacou R${sacar1} e o saldo é R${saldo}.")
    
    elif comando == '2':
        deposito1 = int(input("Quanto deseja depositar: "))
        saldo += deposito1
        print(f"Você depositou R${deposito1} e o saldo é R${saldo}.")
    
    elif comando == '3':
        print(f"Seu saldo é de R${saldo}.")
    
    elif comando == '4':
        print("Tarefa finalizada.")
        break
    
    else:
        print("Comando inválido. Tente novamente.")
