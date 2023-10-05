 <p> <h1 align="center">Criando Pacote de Imagens Python</h1></p>

Neste projeto, aprendemos a criar um pacote de processamento de imagens em Python e disponibilizá-lo no repositório Pypi, facilitando sua reutilização e compartilhamento com outras pessoas. A especialista também demonstrou um exemplo de pacote para processamento de imagens, fornecendo informações sobre a estrutura do projeto e a importância de cada arquivo. 

1. **Estrutura do Projeto:**
   O projeto está organizado em uma estrutura de pastas e arquivos. Na pasta principal, chamada "image_processing," existem duas subpastas: "processing" e "utilis." Cada uma delas contém arquivos com funções específicas para processamento de imagens.

   - **Arquivo `setup.py`:** Este arquivo é essencial para configurar e definir informações sobre o projeto Python. Ele inclui detalhes como nome, versão, autor, descrição, dependências e outras configurações necessárias para empacotar e distribuir o projeto.

   - **Arquivo `__init__.py`:** Este arquivo indica que o diretório em que está presente é um pacote Python. Ele é usado para importar módulos de dentro do pacote.

   - **Arquivo `combination.py`:** Este arquivo contém funções para calcular a diferença estrutural entre duas imagens em tons de cinza e para transferir o histograma de uma imagem para outra. Ele utiliza bibliotecas como NumPy e scikit-image para realizar essas operações.

   - **Arquivo `transformation.py`:** Este arquivo inclui uma função para redimensionar imagens com base em uma proporção especificada. Ele utiliza a função `resize` da biblioteca scikit-image.

   - **Arquivo `io.py`:** Este arquivo fornece funções para ler imagens de arquivos e salvar imagens em arquivos. Ele utiliza as funções `imread` e `imsave` da biblioteca scikit-image.

   - **Arquivo `plot.py`:** Este arquivo contém funções para plotar imagens, resultados e histogramas de cores usando a biblioteca Matplotlib.

2. **Aprendizados Chave:**
   - A importância do arquivo `setup.py` na configuração do projeto Python, permitindo sua distribuição e reutilização.
   - A utilização de bibliotecas Python especializadas, como NumPy, scikit-image e Matplotlib, para processamento de imagens e visualização.
   - A criação de funções reutilizáveis para operações comuns em processamento de imagens, como redimensionamento, cálculo de diferença estrutural e transferência de histogramas.
   - A estruturação de um projeto em pacotes e módulos para melhor organização e manutenção do código.
   - A capacidade de ler imagens de arquivos, processá-las e salvar os resultados em arquivos.

No geral, este projeto fornece uma introdução valiosa ao desenvolvimento de pacotes Python para processamento de imagens e demonstra como organizar e compartilhar seu código de maneira eficiente. Aprendemos a criar funções úteis para manipulação de imagens e a utilizar bibliotecas Python poderosas para essas tarefas, preparando-o para projetos mais avançados na área de visão computacional e processamento de imagens.
Obs.: Projeto em anexo criado pela especialista Karina Kato
#### Curso Formação Python Developer da Dio.me administrado pelo mentora Karina Kato Machine Learning Engineer, Take Blip

[DIO](https://www.dio.me/).
