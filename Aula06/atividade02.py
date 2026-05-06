def verificar_nota(nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input("Digite novamente a nota: "))
    return nota

nota1 = float(input("Digite nota 1: "))
nota1 = verificar_nota(nota1)

nota2 = float(input("Digite nota 2: "))
nota2 = verificar_nota(nota2)

media = (nota1+nota2)/2
print(f"Sua Média é: {media}")