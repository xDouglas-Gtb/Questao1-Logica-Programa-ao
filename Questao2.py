print("-----Seja bem-vindo ao Restaurante do Douglas Guimarães Gomes da Silva-----")     # Mensagem de boas-vindas com nome,sobrenome e o menu
print("--------------------Cardápio--------------------")
print("------------------------------------------------")
print("---Variedades de Tamanhos: P , M , G ---")
print("---Sabores: BA (Bife acebolado), FF (Filé de Frango)---")
print("---BA - P: R$16,00 | M: R$18,00 | G: R$22,00---")
print("---FF - P: R$15,00 | M: R$17,00 | G: R$21,00---")
print("--------------- Fim do Cardápio ---------------")
print("------------------------------------------------")

valortotal = 0  # Inserindo Acumulador do valor total

while True:
    sabor = input("Digite o sabor desejado (BA ou FF): ").upper()     #Inserindo o input do sabor e do tamanho
    if sabor != "BA" and sabor != "FF":
        print(" Sabor inválido. Tente novamente.")
        continue  # volta ao início do while

    tamanho = input("Digite o tamanho desejado (P, M, G): ").upper()
    if tamanho != "P" and tamanho != "M" and tamanho != "G":
        print(" Tamanho inválido. Tente novamente.")
        continue

    # Estrutura aninhada utilizada para calcular o valor do sabor e tamanho
    if sabor == "BA":
        if tamanho == "P":
            valor = 16
        elif tamanho == "M":
            valor = 18
        else:  # G
            valor = 22
    else:  # FF
        if tamanho == "P":
            valor = 15
        elif tamanho == "M":
            valor = 17
        else:  # G
            valor = 21

    valortotal += valor
    print(f"Pedido feito com sucesso!: {sabor} tamanho {tamanho} - R$ {valor:.2f}")

    algum_pedido = input("Gostaria de fazer mais algum pedido? (S/N): ").upper()        #Inserindo outro input de pergunta
    if algum_pedido == "N":
        break
    elif algum_pedido != "S":
        print(" Opção incorreta. Tente novamente")
        break
    else:
        print("----------")
        print(f"Valor total do pedido: R$ {valortotal:.2f}")
        print("Continuando seu atendimento...\n")

print("----------")
print(f"Valor total do pedido: R$ {valortotal:.2f}")
print(" Parabéns, procedimento concluído com sucesso!")
