#3 operação leitura e escrita de imagem

from skimage.io import inread, insave

# Função para ler uma imagem de um arquivo
def read_image(path, is_gray = False):
    image = inread(path, as_gray = is_gray)
    return image
 # Função para salvar uma imagem em um arquivo
def save_image(image, path):
    insave(path, image)

""" 

Analisando o  código:

1. `from skimage.io import imread, imsave`: Esta linha de código importa duas funções, `imread` e `imsave`, da biblioteca `scikit-image`. A função `imread` é usada para ler imagens de arquivos e a função `imsave` é usada para salvar imagens em arquivos.

2. `def read_image(path, is_gray=False):`: Isso define uma função chamada `read_image`. Ela recebe dois argumentos:
   - `path`: O caminho para o arquivo de imagem que você deseja ler.
   - `is_gray`: Um parâmetro opcional que indica se a imagem deve ser lida em tons de cinza (preto e branco). O valor padrão é `False`, o que significa que a imagem será lida em cores.

3. `image = imread(path, as_gray=is_gray)`: Dentro da função `read_image`, esta linha usa a função `imread` para ler a imagem do arquivo especificado no caminho `path`. O parâmetro `as_gray` é usado para controlar se a imagem será lida em tons de cinza ou em cores, com base no valor de `is_gray`.

4. `return image`: A função `read_image` retorna a imagem lida como resultado.

5. `def save_image(image, path):`: Isso define uma função chamada `save_image`. Ela recebe dois argumentos:
   - `image`: A imagem que você deseja salvar em um arquivo.
   - `path`: O caminho para o arquivo no qual você deseja salvar a imagem.

6. `imsave(path, image)`: Dentro da função `save_image`, esta linha usa a função `imsave` para salvar a imagem especificada no caminho `path`.

Resumidamente, este código fornece duas funções: uma para ler uma imagem de um arquivo e outra para salvar uma imagem em um arquivo. Ele usa a biblioteca `scikit-image` para realizar essas operações de forma simples e eficaz. A capacidade de ler e salvar imagens é útil em muitos aplicativos, como processamento de imagem e visão computacional. """