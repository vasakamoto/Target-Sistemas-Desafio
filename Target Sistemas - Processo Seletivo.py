def fibonacci(n):

    fibonacci = [0, 1]

    i = 2
    while i < n:
        fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
        i += 1

    return "Numero informado está contido na sequencia de Fibonacci na posicao {:d}".format(fibonacci.index(n)) if n in fibonacci else "valor nao presente na sequencia de Fibonacci"
        
    
def faturamento(json):
    maior, d_maior, menor, d_menor, media, dias = 0, 0, 0, 0, 0, 0
    d_acima_da_media = []

    for x in json:
        if json[x] == None: json[x] = 0
        dias += 1
        media += json[x]
        if json[x] > maior:
            maior =  json[x]
            d_maior = x
        if json[x] < menor and json[x] != (0 or None):
            menor = json[x]
            d_menor = x

    media = media / dias

    for x in json:
        if json[x] > media:
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
        
    
