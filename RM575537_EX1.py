# Pergunta quantos colaboradores vão participar da votação
colaboradores = int(input("Informe o número de colaboradores: "))
while colaboradores <= 0:
    print("O valor de colaboradores precisa ser maior que zero.")
    colaboradores = int(input("Informe o número de colaboradores: "))

# Contador para cada dia da semana
segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0

# Contador de colaboradores que já deram uma resposta válida
contador = 0

# Enquanto a quantidade de respostas válidas for menor que a quantidade de colaboradores, continua perguntando

while contador < colaboradores:

    # Pergunta o dia da preferência
    dia = input(
        "Informe o dia da sua preferência  \n(segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): "
    )

    # Transforma a resposta em letras maiúsculas para não diferenciar maiúsculas de minúsculas

    dia = dia.upper()

    # Verifica se o dia é válido
    if dia == "SEGUNDA-FEIRA":
        segunda = segunda + 1
        contador = contador + 1

    elif dia == "TERÇA-FEIRA":
        terca = terca + 1
        contador = contador + 1

    elif dia == "QUARTA-FEIRA":
        quarta = quarta + 1
        contador = contador + 1

    elif dia == "QUINTA-FEIRA":
        quinta = quinta + 1
        contador = contador + 1

    elif dia == "SEXTA-FEIRA":
        sexta = sexta + 1
        contador = contador + 1

    else:
        # Se não for nenhum dos dias acima, a resposta é inválida.
        # Resposta inválida, não aumenta o contador.

        print("Dia inválido. Digite novamente.")


# --------------------------------------------------
# DESCOBRINDO A MAIOR QUANTIDADE DE VOTOS
# --------------------------------------------------

maior = segunda

# OBSERVAÇÃO: Usei IF separados porque preciso verificar TODOS os dias, no caso de usar ELIF mesmo que uma condição seja verdadeira, ele deixaria de verificar as demais.

if terca > maior:
    maior = terca

if quarta > maior:
    maior = quarta

if quinta > maior:
    maior = quinta

if sexta > maior:
    maior = sexta


# --------------------------------------------------
# VERIFICANDO SE EXISTE EMPATE
# --------------------------------------------------

quantidade_maior = 0

# OBSERVAÇÃO: Mesmo caso anterior

if segunda == maior:
    quantidade_maior = quantidade_maior + 1

if terca == maior:
    quantidade_maior = quantidade_maior + 1

if quarta == maior:
    quantidade_maior = quantidade_maior + 1

if quinta == maior:
    quantidade_maior = quantidade_maior + 1

if sexta == maior:
    quantidade_maior = quantidade_maior + 1


# --------------------------------------------------
# MOSTRANDO O RESULTADO
# --------------------------------------------------

if quantidade_maior > 1:

    print("Houve empate entre os dias:")

    if segunda == maior:
        print("SEGUNDA-FEIRA")

    if terca == maior:
        print("TERÇA-FEIRA")

    if quarta == maior:
        print("QUARTA-FEIRA")

    if quinta == maior:
        print("QUINTA-FEIRA")

    if sexta == maior:
        print("SEXTA-FEIRA")


elif segunda == maior:
    print("O dia escolhido pelos colaboradores é: SEGUNDA-FEIRA")

elif terca == maior:
    print("O dia escolhido pelos colaboradores é: TERÇA-FEIRA")

elif quarta == maior:
    print("O dia escolhido pelos colaboradores é: QUARTA-FEIRA")

elif quinta == maior:
    print("O dia escolhido pelos colaboradores é: QUINTA-FEIRA")

elif sexta == maior:
    print("O dia escolhido pelos colaboradores é: SEXTA-FEIRA")