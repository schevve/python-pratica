def menorNumero(vetor, indice = 0):
    if indice >= len(vetor) - 1:
        return vetor[indice]
    return vetor[indice] if menorNumero(vetor, indice + 1) > vetor[indice] else menorNumero(vetor, indice + 1)

def maiorNumero(vetor, indice = 0):
    if indice >= len(vetor) - 1:
        return vetor[indice]
    return vetor[indice] if maiorNumero(vetor, indice + 1) < vetor[indice] else maiorNumero(vetor, indice + 1)

numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

print(f"O menor numero é {menorNumero(numeros)}.")
print(f"O maior numero é {maiorNumero(numeros)}.")
print(f"A média dos valores é {sum(numeros) / len(numeros)}")