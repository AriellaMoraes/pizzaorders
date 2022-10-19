# !/usr/bin/env python
# coding: utf-8

import json

# como ler arquivos
with open('orders.json') as file:
    data = json.load(file)
    
dados = {
    'nome': 'Ana', 
    'idade': 18,
    'sexo': True  
}
with open('saida.json', 'w') as file:
    json.dump(dados, file)