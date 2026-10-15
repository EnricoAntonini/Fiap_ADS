# Pergunta o preço do carro
preco = float(input("Digite o preço do carro: "))

# Verifica se o preço informado é válido
while preco <= 0:
    print("Preço inválido. Digite um valor maior que zero.")
    preco = float(input("Digite o preço do carro: "))

# --------------------------------------------------
# PREÇO PARA PAGAMENTO À VISTA
# --------------------------------------------------

# O pagamento à vista possui 20% de desconto
desconto = preco * 0.2
preco_avista = preco - desconto

print(f"O preço final à vista com desconto 20% é: R$ {preco_avista:.2f}")


# --------------------------------------------------
# PREÇOS PARCELADOS
# --------------------------------------------------

# Parcelas se desenvolvem em multiplos de 6
parcelas = 6

# Como o exercicio pede uma extrutura de repetição na saida, enquanto a quantidade de parcelas for menor ou igual a 60 temos.

while parcelas <= 60:

    # A cada desenvolvimento de 6 parcelas, o acréscimo aumenta 3%
    # Por isso temos a seguinte lógica.
    percentual = parcelas * 0.5 / 100

    # Calcula o valor do acréscimo
    acrescimo = preco * percentual

    # Soma o acréscimo ao preço original
    preco_parcelado = preco + acrescimo

    # Divide o preço parcelado pela quantidade de parcelas
    valor_parcela = preco_parcelado / parcelas

    # Mostra os valores calculados
    print(f"O preço final parcelado em {parcelas} X é de R$ {preco_parcelado:.2f} com parcelas de R$ {valor_parcela:.2f}")

    # Aumenta a quantidade de parcelas em 6 para seguir a lógica
    parcelas = parcelas + 6