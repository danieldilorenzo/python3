###
#   Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada
###

nome = input("Qual seu nome? ")
dia = input("Qual seu dia de nascimento? ")
mes = input("Em qual mês você nasceu? (favor escrever por extenso) ")
ano = int(input("Em qual ano você nasceu? "))
# anoint = int(ano)
idade = 2023 - ano

print("Desafio 002")
print(
    "Olá {}, muito prazer! Pelo que você me passou de informação, você nasceu dia {} de {} de {}. Logo em 2023, você está com {} anos!".format(
        nome, dia, mes, ano, idade
    )
)
