import pandas as pd
from pathlib import Path

caminho = Path('dados')
arquivo = caminho / 'supermarket_sales.csv'

df = pd.read_csv(arquivo, sep=',')
df['data'] = pd.to_datetime(df['data'])
df = df.set_index('data')

vendas_por_filial = df.groupby('filial')['total'].agg(['sum', "count"]).reset_index().sort_values('sum', ascending=False)
vendas_por_filial['sum'] = round(vendas_por_filial['sum'], 2)