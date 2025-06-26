#Mensagem de Boas-Vindas
print("Seja bem-vindo,Douglas Guimarães:")

valor_do_pedido = float(input("Digite o valor do pedido: "))             #entrada do valor do pedido e Quantidade De parcelas
quantidadeParcelas = int(input("Digite a quantidade de parcelas: "))     #informações das entradas para o Usuário


#Informaçoes para analisar a quantidade de parcelas para determinar o juros
if quantidadeParcelas <4:
    juros =0

elif quantidadeParcelas >=4 and quantidadeParcelas <6:
    juros = 4 / 100

elif quantidadeParcelas >=6 and quantidadeParcelas <9:
    juros = 8 / 100

elif quantidadeParcelas >=9 and quantidadeParcelas <13:
    juros = 16 / 100

else:
    juros = 32 / 100

#cálculo do valor final,com o juros inserido.
valor_da_parcela = (valor_do_pedido *(1+juros)) / quantidadeParcelas

valor_total_parcelado = valor_da_parcela * quantidadeParcelas

#informações finais ao digitar o valor do pedido e a quantidade de parcelas
print("\nResultado Final:")
print(f"Quantidade de parcelas: {quantidadeParcelas}")
print(f"Juros aplicado: {juros * 100:.0f}%")
print(f"Valor de cada parcela: R$ {valor_da_parcela:.2f}")
print(f"Valor total parcelado: R$ {valor_total_parcelado:.2f}")








