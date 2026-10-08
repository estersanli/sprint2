idade = int(input())
renda = float(input())

if renda < 2000 and idade < 30:
    classificacao = "Bronze"
elif renda < 5000:
    classificacao = "Prata"
elif renda < 10000:
    classificacao = "Ouro"
else:
    classificacao = "Diamante"

print(classificacao)

print("1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão")
opcao = int(input())
num1 = float(input())
num2 = float(input())

match opcao:
    case 1:
        resultado = num1 + num2
    case 2:
        resultado = num1 - num2
    case 3:
        resultado = num1 * num2
    case 4:
        resultado = num1 / num2 if num2 != 0 else "Erro: Divisão por zero"
    case _:
        resultado = "Opção inválida"

print(resultado)

soma = 0
maior = None
menor = None

for i in range(5):
    num = float(input())
    soma += num
    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num

media = soma / 5
print(soma)
print(media)
print(maior)
print(menor)

senha_correta = "1234"
tentativas = 0
acertou = False

while tentativas < 3 and not acertou:
    senha = input()
    if senha == senha_correta:
        acertou = True
    else:
        tentativas += 1

if acertou:
    print("Acesso permitido")
else:
    print("Acesso bloqueado")