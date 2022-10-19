# !/usr/bin/env python
# coding: utf-8
import json
from lib import (json_to_dict, saida_final, total_pizzas, valor,
                clientes)


# 1. Quantas pizzas foram vendidas hj?
# 2. Qual a pizza mais cara?
# 3. Quanto eu faturei hoje?
# 4. Qual o meu melhor cliente?
# 5. Quantas entregas tivemos hoje?
# 6. Quantas pequenas e quantas grandes?

arquivo_pizzaria = 'orders.json'
saida = 'saida.json'

resultado = json_to_dict(arquivo_pizzaria)
total = total_pizzas(resultado)
cara, lucro = valor(resultado)
melhor_cliente = clientes(resultado)
resumo = {
    'total de pizzas': total,
    'Pizza mais cara': f'R$ {cara:.2f}',
    'Faturamento do dia': f'R$ {lucro:.2f}'
}
saida_final(saida, resumo)


# importar função abre_arquivo
# importar funções que processam o arquivo
# importar funções escreve arquivo de saida