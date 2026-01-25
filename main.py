import pandas as pd
from pathlib import Path

caminho = Path('dados')
arquivo = caminho / 'supermarket_sales.csv'

df = pd.read_csv(arquivo, sep=',')
df['data'] = pd.to_datetime(df['data'])
df = df.set_index('data')

class Loja:
    def __init__(self, id_fatura, filial, cidade, tipo_cliente, genero, linha_produto, preco_unitario, quantidade, imposto_5pct, total, hora, pagamento, custo_mercadorias, pct_margem_bruta, renda_bruta, avaliacao):
        self.id_fatura = id_fatura
        self.filial = filial
        self.cidade = cidade
        self.tipo_cliente = tipo_cliente
        self.genero = genero
        self.linha_produto = linha_produto
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.imposto_5pct = imposto_5pct
        self.total = total
        self.hora = hora
        self.pagamento = pagamento
        self.custo_mercadorias = custo_mercadorias
        self.pct_margem_bruta = pct_margem_bruta
        self.renda_bruta = renda_bruta
        self.avaliacao = avaliacao
    
    # * A filial C tem maior faturamento
    # ! Sera que as avaliações delas são boas?
    def vendas_por_filial(self):
        vendas = df.groupby('filial')['total'].agg(['sum', "count"]).reset_index().sort_values('sum', ascending=False)
        vendas['sum'] = round(vendas['sum'], 2)
        return vendas
    
    # * comida é o setor com mais faturamento
    def receita_por_linha(self):
        receita = df.groupby('linha_produto')['renda_bruta'].agg(['sum', 'count']).reset_index().sort_values('sum', ascending=False)
        receita['sum'] = round(receita['sum'], 2)
        return receita
    
    def quantidade_total(self):
        return df['quantidade'].sum()
    
    def total_vendido(self):
        return df['total'].sum()
    
    # * membros gastam mais
    def vendas_por_tipo_cliente(self):
        vendas = df.groupby('tipo_cliente')['total'].agg(['sum', 'count']).reset_index().sort_values('sum', ascending=False)
        vendas['sum'] = round(vendas['sum'], 2)
        return vendas
    
    # * as mulheres gastam mais que homens
    # ! as mulheres costumam dar avaliações positivas?
    def vendas_por_genero(self):
        vendas = df.groupby("genero")['total'].agg(['sum', 'mean', 'count']).reset_index().sort_values('sum', ascending=False)
        vendas['sum'] = round(vendas['sum'], 2)
        vendas['mean'] = round(vendas['mean'], 2)
        return vendas
    
    # * os clientes preferem pagar com ewallet, mas gastam mais quando é no dinehiro.
    def metodos_pagamento_mais_usados(self):
        metodos = df.groupby("pagamento")['total'].agg(["mean", 'count']).reset_index().sort_values('count', ascending=False)
        metodos['mean'] = round(metodos['mean'], 2)
        return metodos


mercado = Loja(
    id_fatura=df['id_fatura'],
    filial=df['filial'],
    cidade=df['cidade'],
    tipo_cliente=df['tipo_cliente'],
    genero=df['genero'],
    linha_produto=df['linha_produto'],
    preco_unitario=df['preco_unitario'],
    quantidade=df['quantidade'],
    imposto_5pct=df['imposto_5pct'],
    total=df['total'],
    hora=df['hora'],
    pagamento=df['pagamento'],
    custo_mercadorias=df['custo_mercadorias'],
    pct_margem_bruta=df['pct_margem_bruta'],
    renda_bruta=df['renda_bruta'],
    avaliacao=df['avaliacao']
)