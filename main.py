import pandas as pd
from pathlib import Path
import plotly.express as px

class Loja:
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    def vendas_por_filial(self, grafico: bool = True):
        vendas = self.df.groupby('filial')['total'].agg(['sum', "count"]).reset_index().sort_values('sum', ascending=False)
        vendas['sum'] = round(vendas['sum'], 2)

        if grafico:
            fig = px.bar(vendas, 'filial', 'sum', color='filial')
            fig.update_layout(
                xaxis_title='Filiais', 
                yaxis_title='Faturamento', 
                showlegend=False, 
                bargap=0.5
                )

            return fig

        else:
            return vendas
    
    def vendas_por_linha(self, grafico: bool = True):
        vendas = self.df.groupby('linha_produto')['total'].agg(['sum', 'count']).reset_index().sort_values('sum', ascending=False)
        vendas['sum'] = round(vendas['sum'], 2)

        if grafico:
            fig = px.bar(vendas, x='linha_produto', y='sum', color='linha_produto')
            fig.update_layout(
                xaxis_title='Linhas',
                yaxis_title='Faturamento',
                showlegend=False
            )

            return fig

        else:
            return vendas
    
    def vendas_por_tipo_cliente(self, grafico: bool = True):
        vendas = self.df.groupby('tipo_cliente')['total'].agg(['sum', 'count']).reset_index().sort_values('sum', ascending=False)
        vendas['sum'] = round(vendas['sum'], 2)

        if grafico:
            fig = px.bar(vendas, 'tipo_cliente', 'sum', color='tipo_cliente')
            fig.update_layout(
                xaxis_title='Tipo de Cliente',
                yaxis_title='Faturamento',
                showlegend=False
            )

            return fig

        else:
            return vendas
    
    def vendas_por_genero(self, grafico: bool = True):
        vendas = self.df.groupby("genero")['total'].agg(['sum', 'mean', 'count']).reset_index().sort_values('sum', ascending=False)
        vendas['sum'] = round(vendas['sum'], 2)
        vendas['mean'] = round(vendas['mean'], 2)

        if grafico:
            fig = px.bar(vendas, 'genero', 'sum', color='genero')
            fig.update_layout(
                xaxis_title='Genero do Cliente',
                yaxis_title='Faturamento',
                showlegend=False
            )

            return fig

        else:
            return vendas
    
    def vendas_por_periodo(self, periodo: str = 'W', grafico: bool = True):
        self.df['data'] = pd.to_datetime(self.df['data'])
        vendas = self.df.set_index('data').resample(periodo.upper())['total'].sum().reset_index()

        if grafico:
            fig = px.line(vendas, 'data', 'total', markers=True)
            fig.update_layout(
                xaxis_title='Periodo',
                yaxis_title='Faturamento',
                showlegend=False
            )

            return fig

        else:
            return vendas

    @property
    def quantidade_total(self):
        return self.df['quantidade'].sum()
    
    @property
    def total_vendido(self):
        return self.df['total'].sum()
    
    @property
    def ticket_medio(self):
        return round(self.df['total'].mean(), 2)

    def metodos_pagamento_mais_usados(self, grafico: bool = True):
        metodos = self.df.groupby("pagamento")['total'].count().reset_index()

        if grafico:
            fig = px.pie(metodos, 'pagamento', 'total', color='pagamento')
            fig.update_traces(hole=0.7)
            fig.update_layout(legend_orientation='h')

            return fig

        else:
            return metodos
    
    def horarios_pico(self, grafico: bool = True):
        self.df['hora'] = pd.to_datetime(self.df['hora'], format='%H:%M').dt.hour
        horarios = self.df.groupby('hora').size().reset_index(name='quantidade')

        if grafico:
            fig = px.line(horarios, 'hora', 'quantidade', markers=True)
            fig.update_traces(line_shape='spline', line_smoothing=1.3)
            fig.update_layout(
                xaxis_title='Horarios',
                yaxis_title='Numero de Vendas',
                showlegend=False
            )

            return fig

        else:
            return horarios

    def ranking_por_filial(self, grafico: bool = True):
        ranking = self.df.groupby('filial')['avaliacao'].mean().reset_index(name="ranking").sort_values('ranking', ascending=False)
        ranking['ranking'] = round(ranking['ranking'], 2)

        if grafico:
            fig = px.bar(ranking, 'filial', 'ranking', color='filial')
            fig.update_layout(
                xaxis_title='Filial',
                yaxis_title='Media de Avaliações',
                showlegend=False
            )

            return fig

        else:
            return ranking

    def ranking_por_categoria(self, grafico: bool = True):
        ranking = self.df.groupby('linha_produto')['avaliacao'].mean().reset_index(name="ranking").sort_values('ranking', ascending=False)
        ranking['ranking'] = round(ranking['ranking'], 2)

        if grafico:
            fig = px.bar(ranking, 'linha_produto', 'ranking', color='linha_produto')
            fig.update_layout(
                xaxis_title='Linha do Produto',
                yaxis_title='Media de Avaliações',
                showlegend=False
            )

            return fig

        else:
            return ranking
    
    def ranking_por_genero(self, grafico: bool = True):
        ranking = self.df.groupby('genero')['avaliacao'].mean().reset_index(name="ranking").sort_values('ranking', ascending=False)
        ranking['ranking'] = round(ranking['ranking'], 2)

        if grafico:
            fig = px.bar(ranking, 'genero', 'ranking', color='genero')
            fig.update_layout(
                xaxis_title='Genero do cliente',
                yaxis_title='Media de Avaliação',
                showlegend=False
            )

            return fig

        else:
            return ranking
    
    def margem_bruta_por_categoria(self, grafico: bool = True):
        margem = self.df.groupby('linha_produto')['renda_bruta'].sum().reset_index().sort_values('renda_bruta', ascending=False)

        if grafico:
            fig = px.pie(margem, 'linha_produto', 'renda_bruta', color='linha_produto')
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(showlegend=True)

            return fig

        else:
            return margem
    
    def ticket_por_tipo_cliente(self, grafico: bool = True):
        ticket = self.df.groupby('tipo_cliente')['total'].mean().reset_index(name='ticket_medio').sort_values('ticket_medio', ascending=False)
        ticket['ticket_medio'] = round(ticket['ticket_medio'], 2)

        if grafico:
            fig = px.bar(ticket, 'tipo_cliente', 'ticket_medio', color='tipo_cliente')
            fig.update_layout(
                xaxis_title='Tipo de cliente',
                yaxis_title='Ticket Medio',
                showlegend=False
            )

            return fig

        else:
            return ticket


caminho = Path('dados')
arquivo = caminho / 'supermarket_sales.csv'

df = pd.read_csv(arquivo, sep=',')
store = Loja(df=df)