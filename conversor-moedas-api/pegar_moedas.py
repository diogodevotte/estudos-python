import xmltodict
import os

def nome_moedas(): 
    # Caminho para o arquivo com os nomes das moedas
    caminho_moedas = os.path.join('sources','moedas.xml')

    # Fecha o arquivo automaticamente 
    with open(caminho_moedas, 'rb') as arquivo_moedas:
        dic_moedas = xmltodict.parse(arquivo_moedas)
    moedas = dic_moedas['xml']
    return moedas

def conversoes_disponiveis():
    # Caminho para o arquivo com as conversões 
    caminho_conversões = os.path.join('sources','conversoes.xml')

    # Fecha o arquivo automaticamente 
    with open(caminho_conversões, 'rb') as arquivo_conversoes:
        dic_conversoes = xmltodict.parse(arquivo_conversoes)

    conversoes = dic_conversoes['xml']
    dic_conversoes_disponiveis = {}

    for par_conversao in conversoes:
        moeda_origem, moeda_destino = par_conversao.split('-') # Separa as strings
        if moeda_origem in dic_conversoes_disponiveis:
            dic_conversoes_disponiveis[moeda_origem].append(moeda_destino)
        else: 
            dic_conversoes_disponiveis[moeda_origem] = [moeda_destino]
    
    return dic_conversoes_disponiveis