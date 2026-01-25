import pandas as pd
from pathlib import Path

caminho = Path('dados')
arquivo = caminho / 'supermarket_sales.csv'

df = pd.read_csv(arquivo, sep=',')

class Loja:
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    # * A filial C tem maior faturamento
    # ! Sera que as avaliações delas são boas?
    def vendas_por_filial(self):
        vendas = self.df.groupby('filial')['total'].agg(['sum', "count"]).reset_index().sort_values('sum', ascending=False)
        vendas['sum'] = round(vendas['sum'], 2)
        return vendas
    
    # * comida é o setor com mais faturamento
    def receita_por_linha(self):
        receita = self.df.groupby('linha_produto')['renda_bruta'].agg(['sum', 'count']).reset_index().sort_values('sum', ascending=False)
        receita['sum'] = round(receita['sum'], 2)
        return receita
    
    def quantidade_total(self):
        return self.df['quantidade'].sum()
    
    def total_vendido(self):
        return self.df['total'].sum()
    
    # * membros gastam mais
    def vendas_por_tipo_cliente(self):
        vendas = self.df.groupby('tipo_cliente')['total'].agg(['sum', 'count']).reset_index().sort_values('sum', ascending=False)
        vendas['sum'] = round(vendas['sum'], 2)
        return vendas
    
    # * as mulheres gastam mais que homens
    # ! as mulheres costumam dar avaliações positivas?
    def vendas_por_genero(self):
        vendas = self.df.groupby("genero")['total'].agg(['sum', 'mean', 'count']).reset_index().sort_values('sum', ascending=False)
        vendas['sum'] = round(vendas['sum'], 2)
        vendas['mean'] = round(vendas['mean'], 2)
        return vendas
    
    # * os clientes preferem pagar com ewallet, mas gastam mais quando é no dinehiro.
    def metodos_pagamento_mais_usados(self):
        metodos = self.df.groupby("pagamento")['total'].agg(["mean", 'count']).reset_index().sort_values('count', ascending=False)
        metodos['mean'] = round(metodos['mean'], 2)
        return metodos
    
    def vendas_por_periodo(self, periodo: str = 'ME'):
        self.df['data'] = pd.to_datetime(self.df['data'])
        self.df = self.df.set_index('data')

        vendas = self.df.resample(periodo.upper())['total'].count().reset_index().sort_values('total', ascending=False)
        return vendas


mercado = Loja(df)
