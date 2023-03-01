def fibonacci(n):

    fibonacci = [0, 1]

    i = 2
    while i < n:
        fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
        i += 1

    return "Numero informado está contido na sequencia de Fibonacci na posicao {:d}".format(fibonacci.index(n)) if n in fibonacci else "valor nao presente na sequencia de Fibonacci"
        

import json
def faturamento(json_path):
    maior, d_maior, menor, d_menor, media, dias = 0, 0, 0, 0, 0, 0
    d_acima_da_media = []
    with open(json_path) as arquivo:
        dic = json.load(arquivo)

    for x in dic:
        if dic[x] == None: dic[x] = 0
        dias += 1
        media += dic[x]
        if dic[x] > maior:
            maior =  dic[x]
            d_maior = x
        if dic[x] < menor and dic[x] != (0 or None):
            menor = dic[x]
            d_menor = x

    media = media / dias

    for x in dic:
        if dic[x] > media:
            d_acima_da_media.append(x)

    print("""Maior faturamento: {} | Dia: {}
Menor faturamento: {} | Dia: {}
Media do mes: {}
Dias cujo faturamento foram maiores que a media: {} | Numero de dias: {}""".format(maior, d_maior, menor, d_menor, media, d_acima_da_media, len(d_acima_da_media)))


def faturamento_relativo():
    faturamento = { "SP" : 67836.43, "RJ" : 36678.66, "MG" : 29229.88, "ES" : 27165.48, "Outros" : 19849.53 }
    total = 0
    faturamento_relativo = {}
    
    for x in faturamento:
        total += faturamento[x]

    for x in faturamento:
        faturamento_relativo[x] = format(faturamento[x] / total, "%")

    return faturamento_relativo

def inverter(string):

    palavra_invertida = ""

    for x in range(len(string) - 1, -1, -1):
        palavra_invertida += string[x]

    return palavra_invertida
        
    
