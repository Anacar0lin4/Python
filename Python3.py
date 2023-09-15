# Importar as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# Criar um DataFrame de exemplo
dados = {'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D'],
         'Vendas': [100, 80, 120, 90]}

df = pd.DataFrame(dados)

# Exibir o DataFrame
print(df)

# Definir cores personalizadas para as barras
cores = ['#F28500', '#024A86', '#FFFF00', '#8c8c8c']

# Criar o gráfico de barras com cores personalizadas
plt.figure(figsize=(8, 6))
plt.bar(df['Produto'], df['Vendas'], color=cores)
plt.xlabel('Produto', fontdict={'family': 'DejaVu Sans', 'size': 14})
plt.ylabel('Vendas', fontdict={'family': 'DejaVu Sans', 'size': 14})
plt.title('Vendas por Produto', fontdict={'family': 'DejaVu Sans', 'size': 16, 'weight': 'bold'})

# Aumentar a linha do eixo
plt.ylim(0, 180)

# Tirar borda preta
plt.box(False)

# Adicionar os números acima da

# Exibir o gráfico
plt.show()


