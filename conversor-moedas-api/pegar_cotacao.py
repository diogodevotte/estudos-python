import requests

def pegar_cotacao_moeda(moeda_origem, moeda_destino):
    link = f'https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}'
    requisicao = requests.get(link) # 200 - Requisição funcionou
    
    cotacao = requisicao.json()[f'{moeda_origem}{moeda_destino}']['bid']
    return cotacao