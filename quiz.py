print("Seja bem vindo ao quiz!")

playing = input("Deseja jogar? ")

if playing.lower() != "sim":
    quit()

print("ok, vamos jogar então!")

questoesAcertadas = 0

answer = input("o que significa uma CPU? ")
if answer.lower == "Unidade Central de Processamento":
    print("Correto! ")
    questoesAcertadas += 1
else:
    print("Errado!")

answer = input("O que signififca GPU? ")
if answer.lower == "Unidade de Processamento Gráfico":
    print("Correto! ")
    questoesAcertadas += 1
    
else:
    print("Errado!")

answer = input("O que significa RAM? ")
if answer.lower == "Memoria de Acesso Aleatório":
    print("Correto! ")
    questoesAcertadas += 1
else:
    print("Errado!")


answer = input("O que significa PSU? ")
if answer.lower == "Unidade de Fonte de Alimentação":
    print("Correto! ")
    questoesAcertadas += 1
else:
    print("Errado!")

print("Você acertou:",questoesAcertadas,"questões!")