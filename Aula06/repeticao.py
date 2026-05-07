# Continue Retorna para o laço, pulando o código abaixo dele e retornando ao loop
cp = 0
while cp < 12:
    cp += 1
    if cp == 3 or cp ==5 or cp == 7:
        continue
    print(f"Produto {cp}")


#while decrescente de 4 até 1
i = 4
while i >= 1:
    print(i)
    i -= 1
