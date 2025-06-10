# PASSO 2 CRIA AS ETIQUETAS PARA IMPRESSÃO

import csv
import step3 as s3
import webbrowser
import os

# Caminho do arquivo HTML
arquivo = f'./Etiquetas_HTML/etiq.html'

def cria_etiquetas(sct,t_eqp):

    #Verifica se usuário deseja cadastrar no SAU
    def continua_cadastro():
        while True:
            resposta = input("Deseja cadastrar equipamentos no S.A.U? S/N ")
            r = resposta.upper()

            if r == 'S':
                s3.run_cadastro(sct,t_eqp)
                
                break
            elif r == 'N':
                print("Tarefa Concluída!!!")
                break
            else:
                print("Selecione S ou N para prosseguir!")

    def abre_etiquetas():
        
        # Converte o caminho para um formato compatível com URLs
        full_path = os.path.abspath(arquivo)
        # Abre o arquivo HTML no navegador padrão
        webbrowser.open(f'file://{full_path}')
        print("\n")
        continua_cadastro()

    # Lê o arquivo CSV
    filename = 'nova_lista.csv'
    #filename = f'./nova_lista/{sct}_lista.csv'
    tables_data = []

    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Pula a primeira linha (cabeçalho)

        for row in csvreader:
            tables_data.append(row)

    # Início do HTML
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link rel="stylesheet" href="mystyle.css">
    </head>
    <body>
    """

    # Cria tabelas separadas para cada linha do CSV
    for data in tables_data:
        
        patrimonio = data[0]
        departamento = data[1]
        secretaria = data[2]

        html += f"""
        <table style="width: 400px;">
            
            <tr>
                <td rowspan="4"><img src="logo.png"></td>
                <td id="mytxt" colspan="2" >Prefeitura Municipal De Praia Grande</td>
            </tr>
            <tr>
                <td>{secretaria}</td>
            </tr>
            <tr>
                <td>{patrimonio}</td>
            </tr>
            <tr>
                <td>{departamento}</td>
            </tr>
        </table>
        <br>  <!-- Adiciona espaço entre tabelas -->
        """

    # Finaliza o HTML
    html += """
    </body>
    </html>
    """

    # Salva o HTML em um arquivo
    with open(arquivo, "w") as file:
        file.write(html)

    print("Etiquetas criadas com sucesso!\n")

    
    while True:
        resposta = input("Deseja visualizar as Etiquetas? S/N ")
        r = resposta.upper()

        if r == 'S':
            abre_etiquetas()
            break
        elif r == 'N':
            continua_cadastro()
            break
        else:
            print("Selecione S ou N para prosseguir!")

    # input("Click para sair!!!")
    ##OBS: Descomentar só para cadastro de CPU...

    #s3.run_cadastro(sct,t_eqp)

    
