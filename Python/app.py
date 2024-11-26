import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from django.shortcuts import render
from io import BytesIO
import base64

def gerar_grafico(df, top_n=5, titulo='', filename=''):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Carro', y='Vendas', data=df)
    plt.title(titulo)
    plt.xlabel('Carro')
    plt.ylabel('Unidades Vendidas')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close()

    return base64.b64encode(image_png).decode('utf-8')


def index(request):
    # Dados dos carros
    dados = {
        'Carro': [
            'BMW X1', 'BMW Série 3', 'Volvo XC90', 'Audi Q3', 'Porsche 911',
            'Land Rover Discovery', 'Audi Q5', 'Porsche Macan', 'Mercedes-Benz Classe C', 'BMW X4'
        ],
        'Vendas': [1457, 1288, 937, 760, 601, 560, 547, 439, 404, 372]
    }

    # Converter para DataFrame
    df = pd.DataFrame(dados)

    # 5 carros mais vendidos
    mais_vendidos = df.nlargest(5, 'Vendas')
    grafico_mais_vendidos = gerar_grafico(
        mais_vendidos, titulo='5 Carros de Luxo Mais Vendidos no Brasil em 2024'
    )

    # 5 carros menos vendidos
    menos_vendidos = df.nsmallest(5, 'Vendas')
    grafico_menos_vendidos = gerar_grafico(
        menos_vendidos, titulo='5 Carros de Luxo Menos Vendidos no Brasil em 2024'
    )

    context = {
        'grafico_mais_vendidos': grafico_mais_vendidos,
        'grafico_menos_vendidos': grafico_menos_vendidos
    }

    return render(request, 'vendas/index.html', context)

 