import requests

#a linha abaixo é para buscar as informações na internet
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
#a linha abaixo é para pegar os dados organizados (parecido como dicionários)
cotacoes = cotacoes.json()

#abaixo são exemplos de utilizações dos dados extraidos do endereço na internet:
cotacao_dolar = cotacoes['USDBRL']["bid"]
cotacao_euro = cotacoes['EURBRL']["bid"]
cotacao_bitcoin = cotacoes['BTCBRL']["bid"]

print("Cotação do Dólar Americano/Real Brasileiro: ", cotacao_dolar)
print("Cotação do Euro/Real Brasileiro: ", cotacao_euro)
print("Cotação do Bitcoin/Real Brasileiro: ", cotacao_bitcoin)
print("Cotações sem formatação: \n",cotacoes)