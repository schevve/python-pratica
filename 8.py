def fibonacci(n):
    # n é quantos numeros da sequencia devem ser retornados
    prev = 0
    curr = 1

    i = 0
    fibonacciNumbers = []
    while (i < n):
        fibonacciNumbers.append(prev)
        temp = curr
        curr = prev + curr
        prev = temp
        i += 1
    return fibonacciNumbers

qtd = int(input("Digite a quantidade de numeros da sequencia: "))

sequencia = fibonacci(qtd)

print(sequencia)