import json
from textwrap import indent

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
    lista_pizza = []
    for pedido in conteudo['orders']:
        lista_pizza.append(float(pedido['price']))

    return max(lista_pizza), sum(lista_pizza)

def clientes(conteudo):
    for pedido in conteudo['orders']:
        nome = pedido['client']['name']


    

