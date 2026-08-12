endpoints = ["/login", "/produtos", "/pedidos"]

status = [
    [200, 200, 401, 200, 500],  # login
    [200, 200, 200, 200, 200],  # produtos
    [201, 500, 502, 201, 500]   # pedidos
]


def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299


def dois_erros(requisicoes):
    for i in range(len(requisicoes) - 1):
        codigo_atual = requisicoes[i]
        prox_codigo = requisicoes[i + 1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True

    return False


def analisar_endpoint(requisicoes):
    qtd_sucesso = 0

    for codigo in requisicoes:
        if eh_sucesso(codigo):
            qtd_sucesso += 1

    qtd_requisicoes = len(requisicoes)
    qtd_erros = qtd_requisicoes-qtd_sucesso
    percentual_sucesso = (qtd_sucesso/qtd_requisicoes) * 100
    tem_erros_seguidos = dois_erros(requisicoes)
    if tem_erros_seguidos:
        classificacao = "Crítico"
    elif percentual_sucesso >= 80:
        classificacao = "Estável"
    else:
        classificacao = "Instável"

        return (qtd_sucesso,qtd_erros,percentual_sucesso,classificacao)

    # Percorrer Toda a Matriz

    maior_quantidade_erros = -1
    endpoint_mais_erros = ""
        for i in range(len(endpoints)):
            nome_endpoint = endpoints[i]
            requisicoes_endpoints = status [i]

            sucesso,erros,percentual,classificacao, = analisar_endpoint((requisicoes_endpoints))

            print(f"Endpoint: {nome_endpoint}")
            print(f"Requisicoes {requisicoes_endpoints}")
            print(f"Sucesso {sucesso}")
            print(f"Erros {erros}")
            print(f" % de Sucesso {percentual: .1f} %")
            print(f"Classificacao {classificacao}")
            print(f"-" * 30)
            print()

            if erros > maior_quantidade_erros:
                maior_quantidade_erros = erros
                endpoint_mais_erros = nome_endpoint

            print(f"Endpoint com + erros é {endpoint_mais_erros} ( {maior_quantidade_erros})")


