# plota listograma, imagens e resultados

import matplotlib.pyplot as plt

# Definição da função para plotar uma imagem
def plot_image(image):
    plt.figure(figsize=(12, 4))  # Cria uma figura com tamanho específico
    plt.imshow(image, cmap='gray')  # Mostra a imagem no formato cinza (escala de cinza)
    plt.axis('off')  # Remove os eixos (labels dos eixos)
    plt.show()  # Mostra a figura na tela

# Definição da função para plotar várias imagens
def plot_result(*args):
    names_lst = []  # Inicializa uma lista vazia para armazenar nomes de imagens
    number_images = len(args)  # Calcula o número de imagens recebidas como argumento
    fig, axis = plt.subplots(nrows=1, ncols=number_images, figsize=(12, 4))  # Cria um conjunto de subplots
    for ax, image in zip(axis, args):  # Itera sobre os subplots e as imagens
        ax.imshow(image, cmap='gray')  # Mostra cada imagem em um subplot
        ax.axis('off')  # Remove os eixos (labels dos eixos)
        names_lst.append('Result')  # Adiciona um nome ('Result') à lista de nomes
    fig.tight_layout()  # Ajusta o layout dos subplots para evitar sobreposições
    plt.show()  # Mostra a figura na tela

# Definição da função para plotar um histograma de cores de uma imagem
def plot_histogram(image):
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)  # Cria subplots para cada canal de cor (RGB)
    color_lst = ['red', 'green', 'blue']  # Lista de nomes de canais de cor
    for index, (ax, color) in enumerate(zip(axis, color_lst)):  # Itera sobre os subplots e nomes de canais de cor
        ax.set_title('{} histogram'.format(color.title()))  # Define o título de cada subplot
        ax.hist(image[:, :, index].ravel(), bins=256, color=color, alpha=0.8)  # Plota o histograma de cores
    fig.tight_layout()  # Ajusta o layout dos subplots para evitar sobreposições
    plt.show()  # Mostra a figura na tela


""" 

Analisando o código

1. `import matplotlib.pyplot as plt`: Importa a biblioteca Matplotlib, que é usada para criar gráficos e visualizações.

2. `def plot_image(image)`: Define uma função chamada `plot_image` que aceita uma imagem como entrada e a exibe em escala de cinza (caso seja colorida).

3. `def plot_result(*args)`: Define uma função chamada `plot_result` que aceita um número variável de argumentos (*args), que são imagens a serem exibidas. Essa função cria subplots para exibir várias imagens em uma única linha.

4. `names_lst = []`: Inicializa uma lista vazia chamada `names_lst` que será usada para armazenar nomes de imagens.

5. `def plot_histogram(image)`: Define uma função chamada `plot_histogram` que aceita uma imagem colorida como entrada e exibe os histogramas das cores vermelha, verde e azul (canais RGB) em subplots separados.

A lista `names_lst` é usada para armazenar os nomes das imagens que serão exibidas em `plot_result()`. Neste código, a lista é inicializada vazia e, em seguida, um nome ('Result') é adicionado a ela para cada imagem passada como argumento para `plot_result()`. No entanto, dependendo do seu uso real, você pode personalizar essa lista para atribuir nomes específicos às imagens que deseja exibir. Por exemplo, se você tiver uma lista de nomes predefinidos para suas imagens, pode usá-los em vez de 'Result'. """
