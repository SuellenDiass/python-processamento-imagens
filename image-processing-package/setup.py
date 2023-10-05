from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-testing-isabella",
    version="0.0.1",
    author="Isabella Ramos",
    author_email="isabella.menezes@ufv.br",
    description="Passo a passo passado por Karina Kato.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/isabellazramos/criacao-de-pacotes-em-python",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)

""" Este código é um exemplo de um arquivo `setup.py`, que é usado para configurar e definir as informações necessárias para empacotar e distribuir um projeto Python. Vou explicar a estrutura do código para um iniciante em programação:

1. `from setuptools import setup, find_packages`: Esta linha importa duas funções importantes da biblioteca `setuptools`. A função `setup` é usada para configurar as informações do projeto, enquanto a função `find_packages` é usada para encontrar automaticamente todos os pacotes (módulos) do seu projeto.

2. `with open("README.md", "r") as f:`: Este bloco de código abre o arquivo `README.md` (normalmente usado para documentação do projeto) no modo de leitura (`"r"`) e o associa a uma variável chamada `f`.

3. `page_description = f.read()`: Este código lê o conteúdo do arquivo `README.md` e o armazena na variável `page_description`. Isso permite que a descrição do projeto seja usada como parte da documentação quando o projeto for empacotado e distribuído.

4. `with open("requirements.txt") as f:`: Este bloco de código abre o arquivo `requirements.txt`, que geralmente contém uma lista de dependências (bibliotecas) necessárias para o projeto, no mesmo modo de leitura.

5. `requirements = f.read().splitlines()`: Isso lê o conteúdo do arquivo `requirements.txt` e divide-o em linhas, armazenando cada linha (que geralmente é uma dependência) em uma lista chamada `requirements`.

6. `setup(...)`: Aqui, você está usando a função `setup` para configurar as informações do projeto. Os argumentos dentro do `setup` incluem:
   - `name`: O nome do projeto.
   - `version`: A versão do projeto.
   - `author`: O nome do autor do projeto.
   - `author_email`: O email do autor do projeto.
   - `description`: Uma breve descrição do projeto.
   - `long_description`: A descrição mais detalhada do projeto, que foi lida do arquivo `README.md`.
   - `long_description_content_type`: O tipo de conteúdo da descrição longa (normalmente é "text/markdown" para arquivos Markdown).
   - `url`: O URL do repositório do projeto no GitHub ou em outro local.
   - `packages`: Usa a função `find_packages()` para encontrar automaticamente todos os pacotes do projeto.
   - `install_requires`: Uma lista das dependências do projeto, lidas do arquivo `requirements.txt`.
   - `python_requires`: A versão mínima do Python necessária para executar o projeto.

Esse arquivo `setup.py` é usado para configurar seu projeto Python, tornando-o pronto para ser empacotado e distribuído para outros desenvolvedores ou usuários. Ele é essencial quando você deseja compartilhar seu código e bibliotecas com outras pessoas. """