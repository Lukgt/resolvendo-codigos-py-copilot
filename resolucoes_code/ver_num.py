# Solicita um número inteiro do usuário
numero = int(input("Por favor, insira um número inteiro: "))

# Verifica se o número é par ou ímpar usando o operador de módulo
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")