# --------------------------------------------------
# ESCOLHA DO TIPO DE INVESTIMENTO
# --------------------------------------------------

# Professor cogitei fazer aqui aquele menu que se repete com while, e uma opção final para sair do programa, mas vi que ficaria fora do modelo de saida apresentado no exercicio então preferi fazer desta forma.

print("Escolha o tipo de investimento:")
print("1. CDB")
print("2. LCI")
print("3. LCA")

investimento = int(input("Digite o tipo de investimento (1, 2 ou 3): "))

# Verifica se o tipo de investimento é válido
while investimento < 1 or investimento > 3:
    print("Tipo de investimento inválido. Digite 1, 2 ou 3.")
    investimento = int(input("Digite o tipo de investimento (1, 2 ou 3): "))

# --------------------------------------------------
# VALORES DO RESGATE
# --------------------------------------------------

# Pergunta o valor que será resgatado
valor = float(input("Digite o valor a ser resgatado: "))

# Verifica se o valor informado é válido
while valor <= 0:
    print("Valor inválido. Digite um valor maior que zero.")
    valor = float(input("Digite o valor a ser resgatado: "))

# --------------------------------------------------
# CÁLCULO DO IMPOSTO DE RENDA
# --------------------------------------------------

# LCI e LCA são isentas de Imposto de Renda, por isso não é necessário informar o número de dias. Então não os incluí nestas opções.
if investimento == 2 or investimento == 3:
    imposto = 0

# Para CDB, verifica a quantidade de dias para descobrir a alíquota correspondente
elif investimento == 1:
    dias = int(input("Digite o número de dias que o valor permaneceu investido: "))

    # Verifica se a quantidade de dias é válida
    while dias <= 0:
        print("Quantidade de dias inválida. Digite um valor maior que zero.")
        dias = int(input("Digite o número de dias que o valor permaneceu investido: "))

    # Até 180 dias, a alíquota é de 22,5%
    if dias <= 180:
        imposto = valor * 0.225

    # De 181 até 360 dias, a alíquota é de 20%
    elif dias <= 360:
        imposto = valor * 0.20

    # De 361 até 720 dias, a alíquota é de 17,5%
    elif dias <= 720:
        imposto = valor * 0.175

    # Acima de 720 dias, a alíquota é de 15%
    else:
        imposto = valor * 0.15

# --------------------------------------------------
# RESULTADO
# --------------------------------------------------

print(f"O valor do imposto de renda a ser pago é: R$ {imposto:.2f}")