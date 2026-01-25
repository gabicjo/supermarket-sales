import pandas as pd
from pathlib import Path
from main import Loja

caminho = Path('dados')
arquivo = caminho / 'supermarket_sales.csv'

df = pd.read_csv(arquivo, sep=',')
mercado = Loja(df)

opcoes = {
    '1': ('Vendas por Filial', mercado.vendas_por_filial),
    '2': ('Vendas por Linha de Produto', mercado.vendas_por_linha),
    '3': ('Quantidade Total', lambda: mercado.quantidade_total),
    '4': ('Total Vendido', lambda: mercado.total_vendido),
    '5': ('Ticket Médio', lambda: mercado.ticket_medio),
    '6': ('Vendas por Tipo de Cliente', mercado.vendas_por_tipo_cliente),
    '7': ('Vendas por Gênero', mercado.vendas_por_genero),
    '8': ('Métodos de Pagamento', mercado.metodos_pagamento_mais_usados),
    '9': ('Horários de Pico', mercado.horarios_pico),
    '10': ('Ranking por Filial', mercado.ranking_por_filial),
    '11': ('Ranking por Categoria', mercado.ranking_por_categoria),
    '12': ('Ranking por Gênero', mercado.ranking_por_genero),
    '13': ('Margem Bruta por Categoria', mercado.margem_bruta_por_categoria),
    '14': ('Ticket Médio por Tipo de Cliente', mercado.ticket_por_tipo_cliente),
}

def exibir_menu():
    print("\n" + "="*50)
    print("ANÁLISE DE VENDAS - SUPERMERCADO")
    print("="*50)
    for key, (nome, _) in opcoes.items():
        print(f"{key}. {nome}")
    print("0. Sair")
    print("="*50)

def main():
    while True:
        exibir_menu()
        try:
            escolha = input("\nEscolha uma opção: ").strip()
            
            if escolha == '0':
                print("\nEncerrando...")
                break
            
            if escolha not in opcoes:
                print("\n❌ Opção inválida! Digite um número entre 0 e 14.")
                continue
            
            nome, funcao = opcoes[escolha]
            print(f"\n{'='*50}")
            print(f"{nome}")
            print("="*50)
            
            resultado = funcao()
            
            if isinstance(resultado, pd.DataFrame):
                print(resultado.to_string(index=False))
            else:
                print(f"Resultado: {resultado}")
            
            print()
        
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido.")
            break
        except Exception as e:
            print(f"\n❌ Erro: {str(e)}")

if __name__ == "__main__":
    main()
