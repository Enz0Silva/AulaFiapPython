def boas_vindas(nome):
    print(f"Olá {nome}!! Seja bem-vindo!!")

nome_digitado = input("Digite seu nome: ")
boas_vindas(nome_digitado)


def soma(num_a, num_b):
    return num_a + num_b

resultado = soma(7, 4)
print(resultado)


num_a = int(input("Digite o primeiro número: "))
num_b = int(input("Digite o segundo número: "))
print(soma(num_a, num_b))


def pode_aprovar(idade):
    if idade >= 18:
        return True
    else:
        return False

idade = int(input("Digite sua idade: "))
print(pode_aprovar(idade))