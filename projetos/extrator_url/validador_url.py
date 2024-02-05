import re

# TESTANDO REGEX
# https://www.bytebank.com.br/cambio


url = "https://www.bytebank.com.br/cambio"

padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
match = padrao_url.match(url)

if not match:
    raise ValueError("A URL não é válida")
else:
    print("A URL é válida")