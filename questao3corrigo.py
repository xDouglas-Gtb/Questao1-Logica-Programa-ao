# Mensagem de boas-vindas com nome e sobrenome
print("Seja Bem-Vindo, Douglas Guimarães:")
# Função feita  para escolher o modelo de camiseta
def escolha_modelo():
    while True:
        print("----Modelos Prontos---- ")
        print("MCS - Camiseta Manga Curta Simples - R$ 1.80")
        print("MLS - Camiseta Manga Longa Simples - R$ 2.10")
        print("MCE - Camiseta Manga Curta com Estampa - R$ 2.90")
        print("MLE - Camiseta Manga Longa com Estampa - R$ 3.20")
        modelo = input("Escreva o seu modelo de Camisa Desejada MCS/MLS/MCE/MLE: ").upper()
        if modelo == "MCS":
            return 1.80
        elif modelo == "MLS":
            return 2.10
        elif modelo == "MCE":
            return 2.90
        elif modelo == "MLE":
            return 3.20
        else:
            print("Modelo incorreto. Tente novamente!!")
# Função feita para desenvolver o número de camisetas com o cálculo de desconto
def numero_cmst():
    while True:
        try:
            qtd = int(input("Digite o número de camisetas desejadas: "))
            if qtd > 20000:
                print("Quantidade não permitida.")
                continue
            elif qtd >= 2000:
                return qtd * 0.88
            elif qtd >= 200:
                return qtd * 0.93
            elif qtd >= 20:
                return qtd * 0.95
            elif qtd > 0:
                return qtd * 1
            else:
                print("Digite uma quantidade maior que zero.")
        except:
            print("Valor incorreto,Digite somente números inteiro")
# Função para escolher o frete
def frete():
    while True:
        print("Opções de frete: ")
        print("0 - Retirada na fábrica - R$ 0")
        print("1 - Transportadora - R$ 100")
        print("2 - Sedex - R$ 200")
        escolha = input("Escreva a opção de frete 0- 1- 2-: ")
        if escolha == "0":
            return 0
        elif escolha == "1":
            return 100
        elif escolha == "2":
            return 200
        else:
            print("Opção de frete inválida. Tente novamente")
# Código principal (main)
try:
    preco_unico = escolha_modelo()
    quantidade_desconto = numero_cmst()
    valordo_frete = frete()

    total = (preco_unico * quantidade_desconto) + valordo_frete
    print(f"\nTotal a pagar: R$ {total:.2f}")
except:
    print("Aconteceu um erro. Tente novamente.")
