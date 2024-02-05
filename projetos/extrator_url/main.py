from ExtratorURL import ExtratorURL

extrator_url = ExtratorURL("bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100")
valor_quantidade = extrator_url.get_valor_parametro("quantidade")

print(extrator_url)