
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "outros": 19849.53,
}

def percentual_representacao():
    total = 0
    percentual = {}
    for local in faturamento.keys():
        total += faturamento[local]
        percentual[local] = 0
    
    for local in percentual.keys():
        percentual[local] = str(round(faturamento[local] / total * 100, 2)) + '%'

    print(percentual)

percentual_representacao()