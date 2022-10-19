# Importar o módulo
import email
import json


data_JSON =  """
{
    "size": "Medium",
    "price": 15.67,
    "toppings": ["Mushrooms", "Extra Cheese", "Pepperoni", "Basil"],
    "client": {
        "name": "Jane Doe",
        "phone": "455-344-234",
        "email": "janedoe@email.com"
    }
}
"""

# Converter a string em JSON em um dicionário
data_dict = json.loads(data_JSON)


dados = {
    'nome': 'Ana', 
    'idade': 18,
    'sexo': True  
}

# Converter o dicionário em Python para Json
dados_json = json.dumps(dados)
