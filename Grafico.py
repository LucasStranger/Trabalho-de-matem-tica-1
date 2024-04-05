import matplotlib.pyplot as plt

def plotar_grafico(integral_exponencial):
    # Dados do gráfico
    dados = {'Integral Exponencial': integral_exponencial}

    # Criar o gráfico
    plt.figure(figsize=(8, 6))
    plt.bar(dados.keys(), dados.values(), color=['blue'])

    # Adicionar título e rótulos
    plt.title('Integral da Distribuição Exponencial')
    plt.xlabel('Integral')
    plt.ylabel('Valor')

    # Exibir o gráfico
    plt.show()