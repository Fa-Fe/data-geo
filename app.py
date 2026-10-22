# %%
import pandas as pd

dfTotal = pd.read_csv('anel_leste_faltante.csv')

df = dfTotal[dfTotal['processado'] == 0]

lista_enderecos = df['endereco_completo'].tolist()


# %%

import requests
import os
from dotenv import load_dotenv

url = "https://geocode.googleapis.com/v4/geocode/destinations"

headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": os.getenv('key_fabricio'),
    "X-Goog-FieldMask": "*"
}


# %%
import json
import Pathlib

path = Pathlib.Path('responses')
path.mkdir(exist_ok=True)

for endereco in lista_enderecos:
    payload = {
        "addressQuery": {
            "addressQuery": endereco
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=30
    )

    with open(f'responses/{endereco}.json', 'w') as f:
        json.dump(response.json(),f)
    

# %%
import json
with open('dois.json', 'w') as f:
    json.dump(response.json(),f)


