url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

url = url.replace(" ", "")

if url == "":
    raise ValueError("URL inválida")

indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]

url_parametros = url[(indice_interrogacao+1):]
print(url_parametros)

parametro_busca = "moedaOrigem"
indice_parametro = url_parametros.find(parametro_busca)

indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find("&", indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)