# operação met de listogramas, passar duas imagens, a primeira é uma imagem de referencia de  conteudo e a segunda referencia de listograma

import numpy as np
from skimage.color import rgb2gray  # Corrected the import statement
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

# Função para calcular a diferença estrutural entre duas imagens em tons de cinza
def find_difference(image1, image2):
    assert image1.shape == image2.shape, "Specify two images with the same shape."
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True)
    print("Similarity of the images:", score)
    normalized_difference_image = (difference_image - np.min(difference_image)) / (np.max(difference_image) - np.min(difference_image))
    return normalized_difference_image
 # Função para transferir o histograma de uma imagem para outra
def transfer_histogram(image1, image2):
    matched_image = match_histograms(image1, image2, multichannel=True)
    return matched_image


# Este código é escrito em Python e tem como objetivo realizar algumas operações em imagens, como calcular a diferença estrutural entre duas imagens e transferir o histograma de uma imagem para outra.

"""  Este código  como objetivo realizar algumas operações em imagens, como calcular a diferença estrutural entre duas imagens e transferir o histograma de uma imagem para outra.

Agora, vamos analisar cada parte do código em mais detalhes:

1. Importações:
   - `import numpy as np`: Isso importa a biblioteca NumPy, que é amplamente utilizada para operações numéricas em Python. Ela é renomeada como `np` para facilitar o uso.
   - `from skimage.color import rgb2gray`: Isso importa a função `rgb2gray` da biblioteca scikit-image, que converte uma imagem colorida em tons de cinza.
   - `from skimage.exposure import match_histograms`: Isso importa a função `match_histograms` da biblioteca scikit-image, que é usada para transferir o histograma de uma imagem para outra.
   - `from skimage.metrics import structural_similarity`: Isso importa a função `structural_similarity` da biblioteca scikit-image, que calcula a similaridade estrutural entre duas imagens.

2. Função `find_difference(image1, image2)`:
   - Esta função recebe duas imagens como entrada (`image1` e `image2`).
   - Verifica se as duas imagens têm o mesmo tamanho (shape) usando um comando `assert`. Se elas tiverem tamanhos diferentes, uma mensagem de erro será exibida.
   - Converte as duas imagens em tons de cinza usando a função `rgb2gray`.
   - Calcula a similaridade estrutural entre as duas imagens em tons de cinza usando a função `structural_similarity`. O resultado é uma medida de quão semelhantes são as imagens.
   - Normaliza a imagem de diferença (uma imagem que destaca as diferenças entre as duas imagens) para ter valores entre 0 e 1.
   - Retorna a imagem de diferença normalizada.

3. Função `transfer_histogram(image1, image2)`:
   - Esta função recebe duas imagens como entrada (`image1` e `image2`).
   - Usa a função `match_histograms` para transferir o histograma de `image1` para `image2`. Isso pode ser útil para igualar o estilo visual de duas imagens.
   - Retorna a imagem `image2` com o histograma transferido de `image1`.

No geral, este código é uma implementação simples de funções para processar imagens. Ele usa algumas bibliotecas Python especializadas para realizar tarefas como conversão de cores, cálculo de similaridade e manipulação de histogramas. As funções `find_difference` e `transfer_histogram` são reutilizáveis e podem ser chamadas com diferentes pares de imagens. """
