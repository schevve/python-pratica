def fatorial(n):
    if n == 1:
        return n
    return fatorial(n - 1) * n

n = int(input("Digite um numero: "))
print(f"O fatorial de {n} é {fatorial(n)}")
