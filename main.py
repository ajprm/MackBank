import random
import re  #USA-SE PARA VALIDAÇÃO DE EMAIL

nomes = []
telefones = []
emails = []
senhas = []
n_contas = []
n_contas_poupanca = []
saldo_conta_poupanca = []
saldo_conta = []
limite = []
historico_operacoes = []
tentativas_saque = 0


# TELA INICIAL
def main():
  print("******** MACK BANK - ESCOLHA UMA OPÇÃO ********")
  print("(0)  CADASTRAR CONTA POUPANÇA")
  print("(1)   CADASTRAR CONTA CORRENTE")
  print("(2)   DEPOSITAR")
  print("(3)   SACAR")
  print("(4)   CONSULTAR SALDO")
  print("(5)   CONSULTAR EXTRATO")
  print("(6)   FINALIZAR")


##FUNÇÕES PRINCIPAIS


#  FUNÇÃO DA CONTA POUPANÇA
def poupanca():
  senha_poupanca = ""
  while True:
    print(
        "      O MACK BANK não envia e-mails pedindo seus dados... FIQUE ATENTO a golpes..     "
    )
    print()
    print("  Você está prestes a cadastrar uma conta poupança...  ")
    print()
    adesao = input(
        "      Você concorda com os termos de adesão?\nDigite 1 (Sim) ou 2 (Não) ou 3 para ler os termos.: "
    )
    if adesao == "1":
      break
    elif adesao == "2":
      print()
      print("Não é possível cadastrar a sua conta poupança.")
      print()
    elif adesao == "3":
      with open('adesao_poupanca.txt') as file_object:
        contents = file_object.read()
        print(contents)
    else:
      print()
      print("Digite um número de 1 a 3")
      print()
  print()
  print("CADASTRE-SE: ")
  # Gerar um número de conta aleatório
  n_conta_poupanca = random.randint(1000, 9999)
  print()
  print("NÚMERO DA CONTA:", n_conta_poupanca)
  print()
  nome = input("NOME DO CLIENTE: ")
  while nome == "":
    print()
    print("Digite seu nome!")
    print()
    nome = input("NOME DO CLIENTE: ")
    print()
  tel = input("TELEFONE.......: ")

  while len(tel) != 11 or not tel.isdigit():
    print(
        "Digite um número de telefone válido com 11 dígitos (apenas números).")
    print()
    tel = input("TELEFONE.......: ")

  else:
    print()
    print("Número de telefone válido:", tel)

  email_poupanca = input("EMAIL..........:")
  while validar_email(email_poupanca) is False:
    print("O e-mail é inválido.")
    print()
    email_poupanca = input("EMAIL..........:")

  saldo_poupanca = float(input("SALDO INICIAL...: $"))
  while saldo_poupanca < 1000:
    print("DIGITE UM SALDO MAIOR QUE R$ 1000")
    saldo_poupanca = float(input("SALDO INICIAL...: $"))
  print()
  n_contas.append(n_conta_poupanca)
  print(
      f"Conta poupança cadastrada com sucesso! Número da conta: {n_contas[-1]}"
  )
  print()
  print("    CADASTRE UMA SENHA    ")
  senha_poupanca = input("SENHA............: ")

  while len(senha_poupanca) != 6:
    print()
    print("**Insira senha de 6 caracteres**")
    senha_poupanca = input("SENHA............: ")
  print()
  rep_poupanca = input("REPITA A SENHA...: ")

  while senha_poupanca != rep_poupanca:
    print("**Insira senhas iguais**")
    print()
    senha_poupanca = input("SENHA............: ")
    rep_poupanca = input("REPITA A SENHA...: ")

  print("SENHA VÁLIDA")
  print()
  n_contas_poupanca.append(n_conta_poupanca)
  nomes.append(nome)
  telefones.append(tel)
  emails.append(email_poupanca)
  senhas.append(senha_poupanca)
  saldo_conta_poupanca.append(saldo_poupanca)


  # FUNÇÃO DA CONTA CORRENTE
def corrente():
  senha = ""
  while True:
    print(
        "O MACK BANK não envia e-mails pedindo seus dados... Fique atento a golpes"
    )
    print()
    print("Você está prestes a cadastrar uma CONTA CORRENTE...")
    print()
    adesao = input(
        "Você concorda com os termos de adesão?\nDigite 1 (Sim) ou 2 (Não) ou 3 para ler os termos. : "
    )
    if adesao == "1":
      break
    elif adesao == "2":
      print()
      print("Não é possível cadastrar a sua conta corrente.")
    elif adesao == "3":
      with open('adesao_corrente.txt') as file_object:
        contents = file_object.read()
        print(contents)

    else:
      print()
      print("Digite um número de 1 a 3")
      print()
  print()
  print("CADASTRE-SE: ")
  # Gerar um número de conta aleatório
  n_conta = random.randint(1000, 9999)
  print()
  print("NÚMERO DA CONTA:", n_conta)
  print()
  nome = input("NOME DO CLIENTE: ")
  while nome == "":
    print("Digite seu nome.")
    nome = input("NOME DO CLIENTE: ")
  print()
  tel = input("TELEFONE.......: ")

  while len(tel) != 11 or not tel.isdigit():
    print()
    print(
        "Digite um número de telefone válido com 11 dígitos (apenas números).")
    tel = input("TELEFONE.......: ")

  else:
    print()
    print("Número de telefone válido:", tel)
  print()
  email = input("EMAIL..........:")

  while validar_email(email) is False:
    print("O e-mail é INVÁLIDO.")
    email = input("EMAIL..........:")
  print()
  saldo = float(input("SALDO INICIAL...: $"))
  while saldo < 1000:
    print("DIGITE UM SALDO MAIOR QUE R$ 1000")
    saldo = float(input("SALDO INICIAL...: $"))
  # CALCULO DE LIMITE
  print()
  porcentagem_limite = 0.25
  limite_credito = saldo * porcentagem_limite
  # ADICIONANDO OS DADOS A LISTA DE HISTORICO DE OPERAÇÕES
  historico_operacoes.append({
      "cliente": nome,
      "conta": n_conta,
      "tipo": "CADASTRO",
      "valor": 0,
      "novo_saldo": saldo,
      "limite_credito": limite_credito,
  })

  print("LIMITE DE CRÉDITO: R$", limite_credito)
  if limite_credito >= 100:
    print("Ótimo, seu limite de crédito é maior que 100!!")
    print()
    credt = input("Deseja criar um cartão de crédito virtual? SIM/NÃO: ")

    if credt.lower() == "sim":
      cartao_ficticio = gerar_numero_cartao()
      print()
      print(
          "******      AVISO      ******\n Este é um número de cartão de crédito FICTÍCIO. Utilizá-lo para qualquer atividade ilegal é estritamente PROIBIDO."
      )
      print()
      print("Número do Cartão de Crédito Virtual:", cartao_ficticio)

  print()
  print("Cadastre uma senha:")
  senha = input("SENHA............: ")

  while len(senha) != 6:
    print("**Insira senha de 6 caracteres**")
    senha = input("SENHA............: ")

  rep = input("REPITA A SENHA...: ")

  while senha != rep:
    print("**Insira senhas iguais**")
    senha = input("SENHA............: ")
    rep = input("REPITA A SENHA...: ")

  print("CADASTRO EFETUADO!")

  # Adiciona os dados às listas
  n_contas.append(n_conta)
  nomes.append(nome)
  telefones.append(tel)
  emails.append(email)
  senhas.append(senha)
  saldo_conta.append(saldo)
  limite.append(limite_credito)
  print()
  print("NÚMERO DA CONTA:", n_conta, "\nNOME DO CLIENTE:", nome, "\nTELEFONE:",
        tel, "\nEMAIL:", email, "\nSENHA:", senha)
  print()


  # FUNÇÃO DE DEPÓSITO
def deposito():
  print("***MACK BANK – DEPÓSITO EM CONTA****")

  n_conta = int(input("INFORME O NÚMERO DA CONTA: "))

  if n_conta in n_contas and n_conta not in n_contas_poupanca:
    senha = input("Digite a senha: ")

    if senha in senhas:
      indice_cliente = n_contas.index(n_conta)
      nome_cliente = nomes[indice_cliente]
      print("NOME DO CLIENTE:", nome_cliente)
      print()
      deposito_valor = float(input("VALOR DO DEPÓSITO: "))

      if deposito_valor <= 0:
        print("Depósito deve ser maior que 0!")
      else:
        # Adiciona o valor do depósito ao saldo correspondente
        saldo_conta[0] += deposito_valor

        historico_operacoes.append({
            "cliente": nome_cliente,
            "conta": n_conta,
            "tipo": "DEPÓSITO",  # Adicionei o tipo de operação
            "valor": deposito_valor,
            "novo_saldo": saldo_conta[0],
        })
        print("DEPÓSITO REALIZADO COM SUCESSO!")
        print()
        print("NOVO SALDO: R$", saldo_conta[0])

    else:
      print("Senha incorreta.")
  else:
    print("Número da conta não encontrado.")
    print()
    print()
    print("DEPÓSITO EM CONTA POUPANÇA? ")
    print()
    while True:
      deposito_poupanca = input("DIGITE 1 (SIM) OU 2 (NÃO): ")
      if deposito_poupanca == "1":
        senha = input("DIGITE A SENHA: ")

        if senha in senhas:
          indice_cliente = n_contas.index(n_conta)
          nome_cliente = nomes[indice_cliente]
          print("NOME DO CLIENTE:", nome_cliente)

          deposito_valor = float(input("VALOR DO DEPÓSITO: "))
          if deposito_valor <= 0:
            print("Depósito deve ser maior que 0!")
          else:
            # Adiciona o valor do depósito ao saldo correspondente
            saldo_conta_poupanca[0] += deposito_valor
            historico_operacoes.append({
                "cliente": nome_cliente,
                "conta": n_conta,
                "tipo": "DEPÓSITO",  # Adicionei o tipo de operação
                "valor": deposito_valor,
                "novo_saldo": saldo_conta_poupanca[0],
            })
            print("DEPÓSITO REALIZADO COM SUCESSO!")
            print()
            print("NOVO SALDO: R$", saldo_conta_poupanca[0])
            break
        else:
          print("Senha incorreta. Tente novamente.")
          break  # Adicionei um break aqui para sair do loop caso a senha seja incorreta
      else:
        break
  # FUNÇÃO DE SAQUE


def saque():
  global tentativas_saque, saldo_conta, limite

  print("MACK BANK – SAQUE DA CONTA")
  print()
  n_conta = int(input("INFORME O NÚMERO DA CONTA: "))

  if n_conta in n_contas and n_conta not in n_contas_poupanca:
    senha_cadastrada = senhas[n_contas.index(n_conta)]

    while tentativas_saque < 3:
      senha = input("Digite a senha: ")

      if senha == senha_cadastrada:
        indice_cliente = n_contas.index(n_conta)
        nome_cliente = nomes[indice_cliente]
        print("NOME DO CLIENTE:", nome_cliente)

        saque_valor = float(input("VALOR DO SAQUE: "))
        saldo_disponivel = saldo_conta[0]
        limite_disponivel = limite[0]

        if saque_valor <= 0:
          print("O valor do saque deve ser maior que zero.")
        elif saque_valor <= saldo_disponivel:
          saldo_conta[0] -= saque_valor
          historico_operacoes.append({
              "cliente": nome_cliente,
              "conta": n_conta,
              "tipo": "SAQUE",  # Adicionei o tipo de operação
              "valor": saque_valor,
              "novo_saldo": saldo_conta[0],
          })
          print("Saque realizado com sucesso!")
          print("NOVO SALDO: R$", saldo_conta[0])
        elif saque_valor <= (saldo_disponivel + limite_disponivel):
          utilizado_limite = saque_valor - saldo_disponivel
          saldo_conta[0] = 0
          limite[0] -= utilizado_limite
          print("VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO")
          print()
          print("SAQUE REALIZADO COM SUCESSO!")
          print()
          print("NOVO LIMITE DE CRÉDITO: R$", limite[0])
        else:
          print("Saldo insuficiente. Saque não realizado.")
        break
      else:
        print("Senha incorreta. Tente novamente.")
        tentativas_saque += 1
        print("OPÇÕES 3,4 E 5 SERÃO BLOQUEADAS COM 3 TENTATIVAS")
    if tentativas_saque == 3:
      print(
          "Número máximo de tentativas excedido. Opções 3, 4 e 5 bloqueadas.")
  elif n_conta in n_contas_poupanca:
    print("Operação de saque não permitida para contas poupança.")
  else:
    print("Número da conta não encontrado.")

  # FUNÇÃO DE CONSULTA DE SALDO


def consulta_saldo_corrente():
  global tentativas_saque, saldo_conta, limite

  print("MACK BANK – CONSULTA SALDO")
  print()
  n_conta = int(input("INFORME O NÚMERO DA CONTA: "))

  if n_conta in n_contas:
    senha_cadastrada = senhas[n_contas.index(n_conta)]
    tentativas_saque = (
        0  # Reinicia o contador de tentativas para cada tentativa de consulta
    )

    while tentativas_saque < 3:
      senha = input("Digite a senha: ")

      if senha == senha_cadastrada:
        indice_cliente = n_contas.index(n_conta)
        nome_cliente = nomes[indice_cliente]
        print("NOME DO CLIENTE:", nome_cliente)
        print()
        print("Seu saldo é: R$ ", saldo_conta[0])
        print()
        print("Seu limite é: R$ ", limite[0])
        break
      else:
        print("Senha incorreta. Tente novamente.")
        tentativas_saque += 1
        print("OPÇÕES 3,4 E 5 SERÃO BLOQUEADAS COM 3 TENTATIVAS")
  else:
    print("Número da conta não encontrado.")


def consulta_saldo_poupanca():
  global tentativas_saque, saldo_conta_poupanca

  n_conta = int(input("INFORME O NÚMERO DA CONTA POUPANÇA: "))

  if n_conta in n_contas_poupanca:
    senha_cadastrada = senhas[n_contas_poupanca.index(n_conta)]
    tentativas_saque = 0

    while tentativas_saque < 3:
      senha = input("Digite a senha: ")

      if senha == senha_cadastrada:
        indice_cliente = n_contas_poupanca.index(n_conta)
        nome_cliente = nomes[indice_cliente]
        print("NOME DO CLIENTE:", nome_cliente)
        print()
        print("Seu saldo é: R$ ", saldo_conta_poupanca[indice_cliente])
        break
      else:
        print("Senha incorreta. Tente novamente.")
        tentativas_saque += 1
        print("OPÇÕES 3,4 E 5 SERÃO BLOQUEADAS COM 3 TENTATIVAS")

    else:
      print("Número da conta poupança não encontrado.")
  else:
    print("Número da conta poupança não encontrado.")
  # FUNÇÃO DE CONSULTA DE EXTRATO


def consulta_extrato_corrente():
  print("***MACK BANK – EXTRATO CONTA CORRENTE****")

  n_conta = int(input("INFORME O NÚMERO DA CONTA: "))

  if n_conta in n_contas and n_conta not in n_contas_poupanca:
    senha = input("Digite a senha: ")

    if senha in senhas:
      indice_cliente = n_contas.index(n_conta)
      nome_cliente = nomes[indice_cliente]
      print("NOME DO CLIENTE:", nome_cliente)

      if indice_cliente < len(saldo_conta):
        saldo_corrente = saldo_conta[indice_cliente]

        if indice_cliente < len(limite):
          limite_credito_cliente = limite[indice_cliente]
          print("LIMITE DE CRÉDITO: R$", limite_credito_cliente)
        else:
          print("Índice do cliente fora dos limites da lista de limites.")

        print("SALDO EM CONTA CORRENTE: R$", saldo_corrente)

        print("ÚLTIMAS OPERAÇÕES:")
        for operacao in historico_operacoes:
          if operacao["conta"] == n_conta and operacao["tipo"] in [
              "DEPÓSITO",
              "SAQUE",
              "LIMITE DE CRÉDITO",
          ]:
            print(f"{operacao['tipo']}: R$ {operacao['valor']}")

        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")

      else:
        print("Índice do cliente fora dos limites da lista de saldos.")
    else:
      print("Senha incorreta.")
  else:
    print("Número da conta não encontrado ou é uma conta poupança.")


def consulta_extrato_poupanca():
  global tentativas_saque, saldo_conta_poupanca, historico_operacoes, nomes, n_contas_poupanca

  print("MACK BANK – EXTRATO DA CONTA POUPANÇA")
  print()
  n_conta = int(input("INFORME O NÚMERO DA CONTA POUPANÇA: "))

  if n_conta in n_contas_poupanca:
    senha_cadastrada = input("INFORME A SENHA: ")
    tentativas_saque = 0

    while tentativas_saque < 3:
      senha = input("INFORME A SENHA: ")
      print()
      if senha == senha_cadastrada:
        indice_cliente = n_contas_poupanca.index(n_conta)
        nome_cliente = nomes[indice_cliente]

        # Extrato da conta poupança
        saldo_poupanca = saldo_conta_poupanca[indice_cliente]
        print("NOME DO CLIENTE:", nome_cliente)
        print("SALDO EM CONTA POUPANÇA: R$", saldo_poupanca)
        print()
        # Exibir histórico de operações
        print("ÚLTIMAS OPERAÇÕES:")
        for operacao in historico_operacoes:
          if operacao["conta"] == n_conta and operacao["tipo"] in [
              "DEPÓSITO",
              "SAQUE",
          ]:
            tipo_operacao = operacao["tipo"]
            valor_operacao = operacao["valor"]
            print(f"{tipo_operacao}: R$ {valor_operacao}")

        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        break
      else:
        print("Senha incorreta. Tente novamente.")
        tentativas_saque += 1

    else:
      print("Número da conta poupança não encontrado.")
  else:
    print("Número da conta poupança não encontrado.")


# FUNÇÃO PRINCIPAL ADICIONADA APÓS ERRO DE SENHA


def main2():
  print("******** MACK BANK - ESCOLHA UMA OPÇÃO ********")
  print("(00)    LOGIN")
  print("(0)   CADASTRAR CONTA POUPANÇA")
  print("(1)   CADASTRAR CONTA CORRENTE")
  print("(2)   DEPOSITAR")
  print("(6)   FINALIZAR")

  # FUNÇÃO LOGIN


def login():
  global tentativas_saque

  print("******** MACK BANK - LOGIN ********")
  n_conta = int(input("INFORME O NÚMERO DA CONTA: "))

  if n_conta in n_contas:
    senha_cadastrada = senhas[n_contas.index(n_conta)]
    tentativas = 0  # Reinicia o contador de tentativas para cada tentativa de login

    while tentativas < 3:
      senha = input("Digite a senha: ")

      if senha == senha_cadastrada:
        print("Login bem-sucedido!")
        # Resetar as tentativas de saque após um login bem-sucedido
        tentativas_saque = 0
        break
      else:
        print("Senha incorreta. Tente novamente.")
        tentativas_saque += 1

    if tentativas_saque == 3:
      print(
          "Número máximo de tentativas excedido. Opções 3, 4 e 5 bloqueadas.")
  else:
    print("Número da conta não encontrado.")


## FUNÇÕES EXTRAS
# EXTRATO DE corrente


# VALIDAÇÃO DE EMAIL
def validar_email(email):
  # Expressão regular para validar o formato do e-mail
  padrao_email = r"^\S+@\S+\.\S+$"

  # Verifica se o e-mail corresponde ao padrão
  return bool(re.match(padrao_email, email))


  #  GERADOR DE CARTÃO DE CRÉDITO
def gerar_numero_cartao():
  # Prefixo comum para números de cartão de crédito
  prefixo = "7"

  # Gera os próximos 15 dígitos de forma aleatória
  numeros_aleatorios = [str(random.randint(0, 9)) for _ in range(15)]

  # Combina o prefixo com os números aleatórios
  numero_cartao = prefixo + "".join(numeros_aleatorios)

  return numero_cartao


def consulta_saldo():
  print("MACK BANK – CONSULTA SALDO")
  print("Escolha o tipo de conta:")
  print("1. Conta Corrente")
  print("2. Conta Poupança")

  opcao_conta = input("Informe o número da opção desejada: ")

  if opcao_conta == "1":
    consulta_saldo_corrente()
  elif opcao_conta == "2":
    consulta_saldo_poupanca()
  else:
    print("Opção inválida. Tente novamente.")


def consulta_extrato():
  print("MACK BANK – CONSULTA EXTRATO")
  print("Escolha o tipo de conta:")
  print("1. Conta Corrente")
  print("2. Conta Poupança")

  opcao_conta = input("Informe o número da opção desejada: ")

  if opcao_conta == "1":
    consulta_extrato_corrente()
  elif opcao_conta == "2":
    consulta_extrato_poupanca()
  else:
    print("Opção inválida. Tente novamente.")


def final():
  print()
  print("*** MACK BANK – SOBRE ***")
  print("Este programa foi desenvolvido por:")
  print()
  print("ANNA JULIA SANTOS DE PAULA ")


sair = False
conta_poupanca_cadastrada = False
conta_corrente_cadastrada = False
bloqueio_opcoes = False
while not sair:
  if tentativas_saque < 3:
    main()
    escolha = input("SUA OPÇÃO: ")
    if escolha == "0" and not conta_poupanca_cadastrada:
      poupanca()
      conta_poupanca_cadastrada = True
    elif escolha == "0" and conta_poupanca_cadastrada:
      print("Conta poupança já cadastrada. Escolha outra opção.")
    if escolha == "1" and not conta_corrente_cadastrada:
      corrente()
      conta_corrente_cadastrada = True
    elif escolha == "1" and conta_corrente_cadastrada:
      print("Conta corrente já cadastrada. Escolha outra opção.")
    elif escolha == "2":
      deposito()
    elif escolha == "3":
      saque()
    elif escolha == "4":
      consulta_saldo()
    elif escolha == "5":
      consulta_extrato()
    elif escolha == "6":
      sair = True
    else:
      print("Opção inválida. Tente novamente.")

  else:
    bloqueio_opçoes = True
    main2()
    escolha = input("SUA OPÇÃO: ")
    if escolha == "":
      login()
    elif escolha == "0" and not conta_poupanca_cadastrada:
      poupanca()
      conta_poupanca_cadastrada = True
    elif escolha == "0" and conta_poupanca_cadastrada:
      print("Conta poupança já cadastrada. Escolha outra opção.")
    elif escolha == "1" and not conta_corrente_cadastrada:
      corrente()
      conta_corrente_cadastrada = True
    elif escolha == "1" and conta_corrente_cadastrada:
      print("Conta corrente já cadastrada. Escolha outra opção.")
    elif escolha == "2":
      deposito()
    elif escolha == "6":
      final()
      sair = True
    else:
      print("Opção inválida. Tente novamente.")
final()
