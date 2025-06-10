# GERA O NOME DAS ETIQUETAS E ADICIONA A LISTA

import pandas as pd
import step2 as s2
import step3 as s3
# from datetime import datetime

tipo_equipamento = ""

def atualizar_dados(df, patrimonio, etiqueta):
    # Remove espaços extras nos nomes das colunas
    df.columns = df.columns.str.strip()
    # Converte a coluna 'Etiqueta' para o tipo 'object'
    df['ETIQUETA'] = df['ETIQUETA'].astype(object)
    # Atualiza a coluna 'ETIQUETA' com a nova etiqueta
    df.loc[df['PATRIMONIO'] == patrimonio, 'ETIQUETA'] = etiqueta   


def run():
    
    df = pd.read_csv('lista.csv')

    # Verifica as colunas do DataFrame
    print("Colunas do DataFrame:", df.columns)

    # Remove espaços extras dos nomes das colunas
    df.columns = df.columns.str.strip()

    try:
        patrimonios = df['PATRIMONIO'].tolist()
    except KeyError:
        print("Erro: A coluna 'PATRIMONIO' não foi encontrada no arquivo csv.")
        return
    
    while True:
        tipo_equipamento = input("Selecione o tipo de equipamento: \n1: CPU\n2: Monitor\n3: Impressora\n4: Scanner\n5: Nobreak\n??? ==>  ")

        if tipo_equipamento == "1":
            print("CPU")
            break
        elif tipo_equipamento == "2":
            print("Monitor")
            break
        elif tipo_equipamento == "3":
            print("Impressora")
            break
        elif tipo_equipamento == "4":
            print("Scanner")
            break
        elif tipo_equipamento == "5":
            print("Nobreak")
            break
        else:
            print("Tipo não encontrado!!!")
            # O loop continuará, pedindo novamente a entrada

    
    secretaria = input('Digite a secretaria: ')
    num_ultima_etiq = input('Digite o numero da última etiqueta cadastrada: ')
    
    n = int(num_ultima_etiq)   # etiqueta inicial

    for i in patrimonios:
        n += 1
        etiqueta = f'{secretaria.upper()}-{n:04}'
        atualizar_dados(df, i, etiqueta)

    # Salva a planilha atualizada em um arquivo csv
    df.to_csv('nova_lista.csv', index=False)
    print(df.head(n))

    # Passando ao passo 2
    s2.cria_etiquetas(secretaria,tipo_equipamento)

    # s3.run_cadastro(secretaria,tipo_equipamento)

if __name__ == '__main__':
    run()
