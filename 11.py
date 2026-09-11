class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

alunos = []
for i in range(5):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    nota = int(input(f"Digite a nota do {i + 1}º aluno: "))
    aluno = Aluno(nome, nota)
    alunos.append(aluno)

maiorNota = 0
somaNotas = 0
for aluno in alunos:
    print(f"Aluno {aluno.nome}, nota {aluno.nota}")
    somaNotas += aluno.nota
    if aluno.nota > maiorNota:
        maiorNota = aluno.nota

print("A média das notas dos alunos é: " + str(somaNotas / len(alunos)))
print("A maior nota é: " + str(maiorNota))