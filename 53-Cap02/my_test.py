2 + 2

print("Olá, Mundo!")

# Cria uma lista com os números entre 1 e 100
numeros = list(range(0,101))
type(numeros)

# Percorre a lista e verifica se o número é par e divisível por 4
for numero in numeros:
  if numero % 2 == 0 and numer % 4 == 0:
    print(numero)

# Cria uma lista com os números entre 1 e 100
numeros = list(range(0,101))
# Usa a list comprehension para gerar uma lista somente com os números pares e divisíveis por 4
pares_div4 = [numero for numero in numeros if numero % 2 == 0 and numero % 4 == 0]
# Imprime a lista gerada
print(pares_div4)
type(pares_div4)

# FIM
