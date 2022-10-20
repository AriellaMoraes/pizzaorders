import json

def json_to_dict(nome):
    # Função que abre o arquivo:
    with open(nome) as file:
        data = json.load(file)
        return data

def total_pizzas(conteudo):
    # Funções que processam o arquivo:
    return len(conteudo['orders'])

def saida_final(saida, resumo):
    # Função que escreve o arquivo
    with open(saida, 'w') as file:
        json.dump(resumo, file, indent=4)

def valor(conteudo):
    erro = []
    lista_pizza = []
    for pedido in conteudo['orders']:
        try:
            lista_pizza.append(float(pedido['price']))
        except KeyError as e:
            erro.append(f'No pedido {pedido["id"]} esta faltando {e}')
    return max(lista_pizza), sum(lista_pizza), erro

def clientes(conteudo):
    total_gastos = {}
    melhor_cliente = ''
    maior_pedido = 0
    erro = []
    for pedido in conteudo['orders']:
        try:
            nome = pedido['client']['name']
            pedido_price = float(pedido['price'])
            if nome in total_gastos.keys():
                total_gastos[nome] = total_gastos[nome] + pedido_price
            else:
                total_gastos[nome] = pedido_price
        except KeyError as e:
            erro.append(f'No pedido {pedido["id"]} esta faltando {e}')   
    for cliente, valor in total_gastos.items():
        if valor > maior_pedido:
            maior_pedido = valor
            melhor_cliente = cliente
    return [melhor_cliente, total_gastos, erro]

def entregas(conteudo):
    total_entregas = 0
    for pedido in conteudo['orders']:
        if pedido['delivery']:
            total_entregas += 1
    return total_entregas

def tamanho(conteudo):
    pequenas = 0
    medias = 0
    grandes = 0
    tamanhos = {}
    erro = []
    for pedido in conteudo['orders']:
        try:
            if pedido['size'] == 'large':
                grandes += 1
            elif pedido['size'] == 'medium':
                medias += 1
            elif pedido['size'] == 'small':
                pequenas += 1
        except KeyError as e:
            erro.append(f'No pedido {pedido["id"]} esta faltando {e}')
    tamanhos['pequenas'] = pequenas
    tamanhos['grandes'] = grandes
    tamanhos['medias'] = medias
    return [tamanhos, erro]


        

  

