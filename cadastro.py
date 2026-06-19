nome = input("Digite seu nome: ")
sobrenome = str(input("Digite o sobrenome: "))
curso = input("Digite seu curso: ")
cidade = input("Digite sua cidade: ")
idade = int(input("Digite sua idade: "))
print(f"Aluno(a) {nome} {sobrenome} tem {idade} anos e faz o curso de {curso} e mora em {cidade}.")
if idade >= 18:
    print("O aluno é maior de idade.")
else:
    print("O aluno é menor de idade.")