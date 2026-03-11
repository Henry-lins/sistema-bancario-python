menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Leave
=> """
saldo = 0
limite= 500
extrato = ""
numero_de_saques= 0
LIMITES_SAQUES_DIARIOS = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Qual o valor do depósito: "))

        if valor > 0:
           saldo += valor
           extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Por favor, insira um valor válido!")

    elif opcao =="2":
        valor = float(input("Qual o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_de_saques > LIMITES_SAQUES_DIARIOS
        if excedeu_saldo:
           print("Erro, Saldo insuficiente. ")
        elif excedeu_limite:
           print("Erro, seu limite foi atingido, o saque excedeu o limite. ")
        elif excedeu_saques:
           print("Erro, limite de saques disponíveis atingidos. ")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
        else:
            print("Por favor, insira um valor válido!")
    elif opcao =="3":
         print("Abrindo extrato bancário... ")
         print("Não foram realizadas operações bancárias." if not extrato else extrato)
         print(f" Saldo: R$ {saldo:.2f}" )
    elif opcao =="0":
        break     
    else:
     print("Por favor, insira um valor válido. ")             


        