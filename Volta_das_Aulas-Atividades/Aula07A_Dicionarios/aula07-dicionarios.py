eng2sp = dict()
print(eng2sp)

eng2sp["one"] = "uno"
print(eng2sp)

eng2sp = {"one" : "uno",
          "two": "dos",
          "three": "tres"
}
print(eng2sp)
print(eng2sp["one"])

print("dos" in eng2sp)

valores = eng2sp.values()
print("two" in valores)

def count_letras(palavra):
    dicionario = dict()
    for caracter in palavra:
        if caracter not in dicionario:
            dicionario[caracter] = 1
        else:
            dicionario[caracter] +=1
    return dicionario

s = "russi"
print()

print(count_letras(s))
print()
