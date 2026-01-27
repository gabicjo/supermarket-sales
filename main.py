import pandas as pd
from pathlib import Path
import plotly.express as px

class Loja:
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    # * A filial C tem maior faturamento
    # ? Sera que as avaliações delas são boas?
    # ! Sim, a filial c tem as melhoras avaliações
    def vendas_por_filial(self):
        vendas = self.df.groupby('filial')['total'].agg(['sum', "count"]).reset_index().sort_values('sum', ascending=False)
        vendas['sum'] = round(vendas['sum'], 2)

        fig = px.bar(vendas, 'filial', 'sum', title='Vendas por Filial', color='filial')
        fig.update_layout(xaxis_title='Filiais', yaxis_title='Faturamento')

        return fig.show()
    
    # * comida é o setor com mais vendas
    def vendas_por_linha(self):
        vendas = self.df.groupby('linha_produto')['total'].agg(['sum', 'count']).reset_index().sort_values('sum', ascending=False)
        vendas['sum'] = round(vendas['sum'], 2)

        fig = px.bar(vendas, x='linha_produto', y='sum', color='linha_produto', title='Vendas por Linha')
        fig.update_layout(xaxis_title='Linhas', yaxis_title='Faturamento')

        return fig.show()
    
    # * membros gastam mais
    def vendas_por_tipo_cliente(self):
        vendas = self.df.groupby('tipo_cliente')['total'].agg(['sum', 'count']).reset_index().sort_values('sum', ascending=False)
        vendas['sum'] = round(vendas['sum'], 2)

        fig = px.bar(vendas, 'tipo_cliente', 'sum', title="Vendas por Tipo de Cliente", color='tipo_cliente')
        fig.update_layout(xaxis_title='Tipo de Cliente', yaxis_title='Faturamento')

        return fig.show()
    
    # * as mulheres gastam mais que homens
    # ? as mulheres costumam dar avaliações positivas?
    # ! não, as mulheres dão avaliações piores do que homens
    def vendas_por_genero(self):
        vendas = self.df.groupby("genero")['total'].agg(['sum', 'mean', 'count']).reset_index().sort_values('sum', ascending=False)
        vendas['sum'] = round(vendas['sum'], 2)
        vendas['mean'] = round(vendas['mean'], 2)

        fig = px.bar(vendas, 'genero', 'sum', title='Vendas por Genero', color='genero')
        fig.update_layout(xaxis_title='Genero do Cliente', yaxis_title='Faturamento')

        return fig.show()
    
    def vendas_por_periodo(self, periodo: str = 'W'):
        self.df['data'] = pd.to_datetime(self.df['data'])

        vendas = self.df.set_index('data').resample(periodo.upper())['total'].sum().reset_index()

        fig = px.line(vendas, 'data', 'total', title='Vendas por Periodo', markers=True)
        fig.update_layout(xaxis_title='Periodo', yaxis_title='Faturamento')

        return fig.show()

    @property
    def quantidade_total(self):
        return self.df['quantidade'].sum()
    
    @property
    def total_vendido(self):
        return self.df['total'].sum()
    
    @property
    def ticket_medio(self):
        return round(self.df['total'].mean(), 2)

    # * os clientes preferem pagar com ewallet, mas gastam mais quando é no dinehiro.
    def metodos_pagamento_mais_usados(self):
        metodos = self.df.groupby("pagamento")['total'].agg(["mean", 'count']).reset_index().sort_values('count', ascending=False)
        metodos['mean'] = round(metodos['mean'], 2)
        return metodos
    
    # * os clientes costumam comprar mais as 19h
    # ! mas o volume maior de clientes acontece durante a tarde
    def horarios_pico(self):
        self.df['hora'] = pd.to_datetime(self.df['hora'], format='%H:%M').dt.hour
        horarios = self.df.groupby('hora').size().reset_index(name='quantidade').sort_values('quantidade', ascending=False)
        return horarios

    # * a filial C tem as melhores avaliações
    def ranking_por_filial(self):
        ranking = self.df.groupby('filial')['avaliacao'].mean().reset_index(name="ranking").sort_values('ranking', ascending=False)
        ranking['ranking'] = round(ranking['ranking'], 2)
        return ranking

    # * alaviações relacionadas as comidas são geralmente melhores
    # ! o setor de produtos pra casa tem o pior desempenho
    def ranking_por_categoria(self):
        ranking = self.df.groupby('linha_produto')['avaliacao'].mean().reset_index(name="ranking").sort_values('ranking', ascending=False)
        ranking['ranking'] = round(ranking['ranking'], 2)

        return ranking
    
    # * homens costumam dar melhores avaliações
    def ranking_por_genero(self):
        ranking = self.df.groupby('genero')['avaliacao'].mean().reset_index(name="ranking").sort_values('ranking', ascending=False)
        ranking['ranking'] = round(ranking['ranking'], 2)

        return ranking
    
    # * o setor de comida continua sendo o maior triulfo da loja
    def margem_bruta_por_categoria(self):
        margem = self.df.groupby('linha_produto')['renda_bruta'].sum().reset_index().sort_values('renda_bruta', ascending=False)
        return margem
    
    # * membros costuma  gastar um pouco mais
    def ticket_por_tipo_cliente(self):
        ticket = self.df.groupby('tipo_cliente')['total'].mean().reset_index(name='ticket-medio').sort_values('ticket-medio', ascending=False)
        ticket['ticket-medio'] = round(ticket['ticket-medio'], 2)

        return ticket
    
caminho = Path('dados')
arquivo = caminho / 'supermarket_sales.csv'

df = pd.read_csv(arquivo, sep=',')
mercado = Loja(df)
print(mercado.vendas_por_periodo())