# !/usr/bin/env python
# coding: utf-8
from lib import (entregas, json_to_dict, saida_final, total_pizzas, valor,
                 clientes, entregas, tamanho)

arquivo_pizzaria = 'orders.json'
saida = 'saida.json'

resultado = json_to_dict(arquivo_pizzaria)
total = total_pizzas(resultado)
cara, lucro, erro = valor(resultado)
total_gastos = clientes(resultado)
total_entregas = entregas(resultado)
tamanhos = tamanho(resultado)
resumo = {
    'total de pizzas': total,
    'Pizza mais cara': f'R$ {cara:.2f}',
    'Faturamento do dia': f'R$ {lucro:.2f}',
    'Entregas do dia': total_entregas,
    'total de gastos': total_gastos[1],
    'melhor cliente' : total_gastos[0],
    'Tamanhos': tamanhos[0],
    "Erros": erro + total_gastos[2] + tamanhos[1]
}
saida_final(saida, resumo)