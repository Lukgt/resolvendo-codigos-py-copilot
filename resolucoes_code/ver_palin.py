# Solicita uma palavra do usuário
palavra = input("Por favor, insira uma palavra: ")

# Inverte a palavra
palavra_invertida = palavra[::-1]

# Verifica se a palavra é um palíndromo
if palavra == palavra_invertida:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")