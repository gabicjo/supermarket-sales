import pandas as pd
from pathlib import Path

caminho = Path('dados')
arquivo = caminho / 'supermarket_sales.csv'

df = pd.read_csv(arquivo, sep=',')
df['data'] = pd.to_datetime(df['data'])
df = df.set_index('data')

# * A filial C tem maior faturamento
# ! Sera que as avaliações delas são boas?
vendas_por_filial = df.groupby('filial')['total'].agg(['sum', "count"]).reset_index().sort_values('sum', ascending=False)
vendas_por_filial['sum'] = round(vendas_por_filial['sum'], 2)

# * comida é o setor com mais faturamento
receita_por_linha = df.groupby('linha_produto')['renda_bruta'].agg(['sum', 'count']).reset_index().sort_values('sum', ascending=False)
receita_por_linha['sum'] = round(receita_por_linha['sum'], 2)

quantidade_total = df['quantidade'].sum()
total_vendido = df['total'].sum()

# * membros gastam mais
vendas_por_tipo_cliente = df.groupby('tipo_cliente')['total'].agg(['sum', 'count']).reset_index().sort_values('sum', ascending=False)
vendas_por_tipo_cliente['sum'] = round(vendas_por_tipo_cliente['sum'], 2)