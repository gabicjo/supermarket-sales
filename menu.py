import pandas as pd
import os
from pathlib import Path
from main import Loja

caminho = Path('dados')
arquivo = caminho / 'supermarket_sales.csv'

df = pd.read_csv(arquivo, sep=',')
mercado = Loja(df)

# Opciones que requerem parámetro grafico
opcoes_com_grafico = {
    '1': ('Vendas por Filial', mercado.vendas_por_filial),
    '2': ('Vendas por Linha de Produto', mercado.vendas_por_linha),
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

# Opções que não requerem parâmetro (métricas simples)
opcoes_sem_grafico = {
    '3': ('Quantidade Total', lambda: mercado.quantidade_total),
    '4': ('Total Vendido', lambda: mercado.total_vendido),
    '5': ('Ticket Médio', lambda: mercado.ticket_medio),
}

opcoes_completas = {**opcoes_com_grafico, **opcoes_sem_grafico}

def exibir_menu():
    os.system('cls')
    print("\n" + "="*50)
    print("ANÁLISE DE VENDAS - SUPERMERCADO")
    print("="*50)
    for key, (nome, _) in opcoes_completas.items():
        print(f"{key}. {nome}")
    print("0. Sair")
    print("="*50)

def pedir_tipo_exibicao():
    """Pede ao usuário se deseja ver gráfico ou tabela"""
    while True:
        print("\nEscolha o tipo de visualização:")
        print("1. Gráfico")
        print("2. Tabela")
        escolha = input("\nDigite sua opção (1 ou 2): ").strip()
        
        if escolha == '1':
            return True
        elif escolha == '2':
            return False
        else:
            print("❌ Opção inválida! Digite 1 para gráfico ou 2 para tabela.")

def main():
    os.system('cls')
    while True:
        try:
            exibir_menu()
            escolha = input("\nEscolha uma opção: ").strip()
            
            if escolha == '0':
                print("\n✅ Encerrando...")
                break
            
            if escolha not in opcoes_completas:
                print("\n❌ Opção inválida! Digite um número entre 0 e 14.")
                input("\nPressione ENTER para continuar...")
                continue
            
            nome, funcao = opcoes_completas[escolha]
            
            # Se a opção requer gráfico, pede ao usuário
            if escolha in opcoes_com_grafico:
                grafico = pedir_tipo_exibicao()
                os.system('cls')
                print(f"\n{'='*50}")
                print(f"{nome}")
                print("="*50 + "\n")
                
                if grafico:
                    print("⏳ Aguarde enquanto o gráfico está sendo gerado...")
                    funcao(grafico=True)
                    print("\n✅ Gráfico gerado com sucesso!")
                    print("📊 Abra seu navegador para visualizar o gráfico.")
                    print("💡 Se o navegador não abrir automaticamente, procure pela aba com um IP.")
                else:
                    funcao(grafico=False)
            else:
                # Opções sem gráfico apenas exibem o resultado
                os.system('cls')
                print(f"\n{'='*50}")
                print(f"{nome}")
                print("="*50 + "\n")
                resultado = funcao()
                print(f"✅ Resultado: {resultado}")
            
            input("\nPressione ENTER para continuar...")
        
        except KeyboardInterrupt:
            print("\n\n⚠️ Programa interrompido pelo usuário.")
            break
        except FileNotFoundError:
            os.system('cls')
            print("❌ Erro: Arquivo 'supermarket_sales.csv' não encontrado.")
            print("Certifique-se de que o arquivo está na pasta 'dados/'")
            input("\nPressione ENTER para continuar...")
        except pd.errors.EmptyDataError:
            os.system('cls')
            print("❌ Erro: O arquivo CSV está vazio.")
            input("\nPressione ENTER para continuar...")
        except Exception as e:
            os.system('cls')
            print(f"❌ Erro inesperado: {str(e)}")
            input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()
