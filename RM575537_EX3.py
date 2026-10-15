# Pergunta o valor da dívida
divida = float(input("Digite o valor da dívida: "))

# Verifica se o valor informado é válido
while divida <= 0:
    print("Valor inválido. Digite um valor maior que zero.")
    divida = float(input("Digite o valor da dívida: "))


# --------------------------------------------------
# CALCULANDO AS OPÇÕES DE PAGAMENTO
# --------------------------------------------------

# Começando com 1 parcela
parcelas = 1


# Enquanto a quantidade de parcelas for menor ou igual a 12, continuamos a repetição
while parcelas <= 12:

    # Verifica a quantidade de parcelas e define o percentual de juros correspondente
    if parcelas == 1:
        percentual = 0

    elif parcelas == 3:
        percentual = 0.10

    elif parcelas == 6:
        percentual = 0.15

    elif parcelas == 9:
        percentual = 0.20

    elif parcelas == 12:
        percentual = 0.25


    # Calcula o valor dos juros
    juros = divida * percentual

    # Soma os juros ao valor inicial da dívida
    total = divida + juros

    # Calcula o valor de cada parcela
    valor_parcela = total / parcelas

    # Mostra os resultados
    print(f"Total: R$ {total:.2f} Juros: R$ {juros:.2f} Número de parcelas: {parcelas} Valor da Parcela: R$ {valor_parcela:.2f}")

    # Define a próxima quantidade de parcelas
    if parcelas == 1:
        parcelas = 3
    else:
        parcelas = parcelas + 3