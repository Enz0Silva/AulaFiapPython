# Lógica E (And)
from dask.array import logical_or
from sympy import false

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entrar no programa")


# Lógica OU (Or)

logical_ou  = false or false or false
print(logical_ou)



# not
negacao = not True
print(negacao)

if not verifica_senha:
    print(("Senha incorreta papi..."))



