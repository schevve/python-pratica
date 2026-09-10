numeros = []

for i in range(1, 4):
    n = int(input(f"Digite o {i} número: "))
    numeros.append(n)

maiorNumero = None
for n in numeros:
    if (maiorNumero is None):
        maiorNumero = n
        continue
    if maiorNumero < n:
        maiorNumero = n

print(f"O maior numero digitado foi: {maiorNumero}")