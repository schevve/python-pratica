notas = []
for i in range(3):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

print("A média é:", sum(notas) / len(notas)) 