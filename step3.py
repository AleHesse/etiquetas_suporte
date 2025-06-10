# CADASTRA OS EQUIPAMENTO NO SAU

import time
import pandas as pd
import os
import csv
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By


def run_cadastro(sct,t_eqp):

    tipo_eqp = int(t_eqp)
    marca_eqp = "Não Cadastrado"
    modelo_eqp = "Não Cadastrado"
    modo_eqp = "Colorido"
    my_link = ""
    arquivo = 'nova_lista.csv'

    match tipo_eqp:
        case 1:
            my_link = "https://servico.intra.pg/sau/cpu_inc.asp"                     
        case 2:
            my_link = "https://servico.intra.pg/sau/monitor_inc.asp"
        case 3:
            my_link = "https://servico.intra.pg/sau/impressora_inc.asp"
        case 4:
            my_link = "https://servico.intra.pg/sau/scanner_inc.asp"
        case 5:
            my_link = "https://servico.intra.pg/sau/nobreak_inc.asp"

    # Carregando as variáveis de ambiente do arquivo .env
    load_dotenv()
    mylogin = os.getenv('login')
    mysenha = os.getenv('senha')

    with webdriver.Chrome() as driver:
        
        # Realizar Login SAU
       
        driver.get("https://servico.intra.pg/sau/login.asp")
        driver.set_window_size(900, 800)

        login = driver.find_element(By.NAME, 'txtLogin')
        login.send_keys(mylogin)
        senha = driver.find_element(By.NAME, 'txtSenha')
        senha.send_keys(mysenha)

        btn = driver.find_element(By.NAME,'button')
        btn.click()


        # Abre o arquivo CSV
        with open(arquivo, newline='', encoding='utf-8') as csvfile:
            # Lê o arquivo CSV usando o leitor DictReader para obter as colunas com nomes
            arquivo_csv = csv.DictReader(csvfile)
            
            # Itera sobre cada linha no arquivo CSV
            for linha in arquivo_csv:

                time.sleep(2)

                driver.get(my_link)

                # Armazena os dados de cada linha
                patrimonio = linha['PATRIMONIO']
                localizacao = linha['LOCAL']
                etiqueta = linha['ETIQUETA']
                
# CPU ............................................................
                def cadastra_cpu(patrimonio,localizacao,etiqueta):

                    # envia os dados ao frame cadastro de equipamentos
                    secret = driver.find_element(By.XPATH, '/html/body/form/table[1]/tbody/tr[1]/td/p/select')
                    secret.send_keys(sct)
                    local = driver.find_element(By.XPATH, '/html/body/form/table[1]/tbody/tr[2]/td/span/select')
                    local.send_keys(localizacao)
                    etiq = driver.find_element(By.XPATH, '/html/body/form/table[1]/tbody/tr[3]/td/table[1]/tbody/tr[1]/td[2]/input')
                    etiq.send_keys(etiqueta)
                    patrim = driver.find_element(By.XPATH, '/html/body/form/table[1]/tbody/tr[3]/td/table[1]/tbody/tr[2]/td[2]/input')
                    patrim.send_keys(patrimonio)
                    
                    btn = driver.find_element(By.XPATH,'/html/body/form/table[2]/tbody/tr/td/table/tbody/tr[2]/td/div/input[1]')
                    # time.sleep(1)
                    btn.click()

# Monitor..............................................
                def cadastra_monitor(patrimonio,localizacao,etiqueta,marca,modelo,modo):

                    secret = driver.find_element(By.XPATH, '/html/body/form/table[1]/tbody/tr[1]/td[2]/select')
                    secret.send_keys(sct)
                    local = driver.find_element(By.XPATH, '/html/body/form/table[1]/tbody/tr[1]/td[4]/span/select')
                    local.send_keys(localizacao)
                    etiq = driver.find_element(By.XPATH, '/html/body/form/table[1]/tbody/tr[2]/td[2]/input')
                    etiq.send_keys(etiqueta)
                    marca_equip = driver.find_element(By.XPATH, '/html/body/form/table[1]/tbody/tr[3]/td[2]/select')
                    marca_equip.send_keys(marca)
                    modelo_equip = driver.find_element(By.XPATH, '/html/body/form/table[1]/tbody/tr[3]/td[4]/span/select')
                    modelo_equip.send_keys(modelo)
                    modo_equip = driver.find_element(By.XPATH, '/html/body/form/table[1]/tbody/tr[4]/td[4]/select')
                    modo_equip.send_keys(modo)
                    patrim = driver.find_element(By.XPATH, '/html/body/form/table[1]/tbody/tr[2]/td[4]/input')
                    patrim.send_keys(patrimonio)   
                    btn = driver.find_element(By.XPATH,'/html/body/form/table[2]/tbody/tr/td/table/tbody/tr[2]/td/div/input[1]')
                    time.sleep(2)
                    btn.click()

# Impressora........................................................
                def cadastra_impressora(patrimonio,localizacao,etiqueta,marca,modelo):

                    secret = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[4]/td[2]/select')
                    secret.send_keys(sct)
                    local = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[5]/td[2]/span/select')
                    local.send_keys(localizacao)
                    etiq = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[1]/td[2]/input')
                    etiq.send_keys(etiqueta)
                    marca_equip = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td[2]/select')
                    marca_equip.send_keys(marca)
                    modelo_equip = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td[4]/span/select')
                    modelo_equip.send_keys(modelo)
                    patrim = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[1]/td[4]/input')
                    patrim.send_keys(patrimonio)        
                    btn = driver.find_element(By.XPATH,'/html/body/table[2]/tbody/tr/td/form/table[2]/tbody/tr[2]/td/input[1]')
                    time.sleep(2)
                    btn.click()

# Scanner.............................................................
                def cadastra_scanner(patrimonio,localizacao,etiqueta,marca,modelo):

                    secret = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[3]/td[2]/select')
                    secret.send_keys(sct)
                    local = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[4]/td[2]/span/select')
                    local.send_keys(localizacao)
                    etiq = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[1]/td[2]/input')
                    etiq.send_keys(etiqueta)
                    marca_equip = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td[2]/select')
                    marca_equip.send_keys(marca)
                    modelo_equip = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td[4]/span[2]/select')
                    modelo_equip.send_keys(modelo)
                    patrim = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[1]/td[4]/input')
                    patrim.send_keys(patrimonio)
                    btn = driver.find_element(By.XPATH,'/html/body/table[2]/tbody/tr/td/form/table[2]/tbody/tr[2]/td/input[1]')
                    time.sleep(2)
                    btn.click()
# Nobreak..............................................
                def cadastra_nobreak(patrimonio,localizacao,etiqueta,marca,modelo):

                    secret = driver.find_element(By.XPATH, '/html/body/form/table[1]/tbody/tr[1]/td[2]/select')
                    secret.send_keys(sct)
                    local = driver.find_element(By.XPATH, '/html/body/form/table[1]/tbody/tr[1]/td[4]/span/select')
                    local.send_keys(localizacao)
                    etiq = driver.find_element(By.XPATH, '/html/body/form/table[1]/tbody/tr[2]/td[2]/input')
                    etiq.send_keys(etiqueta)
                    marca_equip = driver.find_element(By.XPATH, '/html/body/form/table[1]/tbody/tr[3]/td[2]/select')
                    marca_equip.send_keys(marca)
                    modelo_equip = driver.find_element(By.XPATH, '/html/body/form/table[1]/tbody/tr[3]/td[4]/span/select')
                    modelo_equip.send_keys(modelo)
                    patrim = driver.find_element(By.XPATH, '/html/body/form/table[1]/tbody/tr[2]/td[4]/input')
                    patrim.send_keys(patrimonio)                       
                    btn = driver.find_element(By.XPATH,'/html/body/form/table[2]/tbody/tr/td/table/tbody/tr[2]/td/div/input[1]')
                    time.sleep(2)
                    btn.click()

# Tipo de equipamento.........................................................................................
                match tipo_eqp:
                    case 1:
                        cadastra_cpu(patrimonio,localizacao,etiqueta)                       
                    case 2:
                        cadastra_monitor(patrimonio,localizacao,etiqueta,marca_eqp,modelo_eqp,modo_eqp)
                    case 3:
                        cadastra_impressora(patrimonio,localizacao,etiqueta,marca_eqp,modelo_eqp)
                    case 4:
                        cadastra_scanner(patrimonio,localizacao,etiqueta,marca_eqp,modelo_eqp)
                    case 5:
                        cadastra_nobreak(patrimonio,localizacao,etiqueta,marca_eqp,modelo_eqp)

# Conclusão...................................................................................................
                print(f'Equipamento: {etiqueta} - Pat: {patrimonio} - Cadastrado com Sucesso!')
                   
                
