# Organizador Automático de Arquivos com Python

Este projeto é um organizador de arquivos desenvolvido em Python que permite organizar arquivos dentro de uma pasta específica do computador. Com uma interface interativa e simples de usar, o script possibilita organizar arquivos por tipo ou por data de criação, além de desfazer ações realizadas. A organização é feita de forma automática em pastas específicas, proporcionando uma melhor organização dos seus documentos, imagens, vídeos e outros arquivos.

## Funcionalidades

- **Organização por Tipo de Arquivo**: Move automaticamente os arquivos para pastas baseadas em suas extensões, como `Imagens`, `Vídeos`, `Documentos`, etc.
- **Organização por Data**: Move os arquivos para pastas baseadas na data de criação do arquivo.
- **Desfazer Última Ação**: Reverte a última operação de organização, movendo os arquivos de volta aos seus locais originais e removendo as pastas vazias criadas durante a organização.
- **Interface Interativa**: O programa oferece um menu interativo no terminal para facilitar o uso.

## Requisitos

- Python 3.6 ou superior.
- Bibliotecas necessárias:
  - `shutil` (padrão do Python)
  - `tkinter` (padrão do Python)
  - `datetime` (padrão do Python)
  - `collections` (padrão do Python)
  - `colorama` (instalar via `pip`)

### Instalação da Biblioteca Colorama
Para tornar o terminal mais amigável e com cores, utilizamos a biblioteca `colorama`. Para instalá-la, execute o seguinte comando:
```sh
pip install colorama
```

## Como Usar

1. Clone este repositório ou baixe o script Python.
2. No terminal, execute o script:
   ```sh
   python file_organizer.py
   ```
3. Será aberta uma janela para selecionar o diretório que deseja organizar.
4. Depois de selecionar a pasta, um menu será exibido no terminal, onde você poderá escolher:
   - Organizar por tipo de arquivo.
   - Organizar por data de criação.
   - Desfazer a última ação.
   - Sair do programa.

## Estrutura do Código

- **Classe `FileOrganizer`**: Responsável pela lógica principal do programa, incluindo métodos para organizar arquivos e desfazer ações.
  - `__init__(directory)`: Inicializa a classe com o diretório especificado.
  - `organize_by_extension()`: Organiza os arquivos em pastas por tipo.
  - `organize_by_date()`: Organiza os arquivos em pastas por data de criação.
  - `undo_last_action()`: Desfaz a última ação de organização.
  - `interactive_menu()`: Apresenta o menu interativo para o usuário.

## Observações

- O script utiliza a biblioteca `tkinter` para abrir uma janela de seleção de pastas, tornando mais fácil escolher o diretório a ser organizado.
- Para garantir que todas as alterações possam ser revertidas, o programa salva as ações realizadas e oferece a opção de desfazer a última operação.
- Durante o processo de desfazer, as pastas vazias criadas são removidas automaticamente.

## Dicas para Implementações Futuras

- **Suporte para Filtros Adicionais**: Possibilidade de adicionar filtros personalizados, como organização por tamanho ou por nome do arquivo.
- **Interface Gráfica Completa**: Desenvolver uma interface gráfica completa para facilitar ainda mais o uso do organizador.
- **Integração com Serviços em Nuvem**: Opção de organizar arquivos em diretórios sincronizados com serviços em nuvem, como Google Drive ou Dropbox.f

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests com melhorias, novas funcionalidades ou correções de bugs.

## Infos de commits

- :package: novas funcionalidades
- :up: atualizações
- :ant: correções de bug
- :checkered_flag: release


## Nos acompanhe nas redes

- Instagram - [@python_brasil](https://www.instagram.com/python_brasil/)
- LinkedIn - [Comunidade Python Brasil](https://www.linkedin.com/company/comunidade-python-brasil)
- GitHub - [python-brasil](https://github.com/python-brasil)
- YouTube - [@Python_Brasil](https://www.youtube.com/@Python_Brasil)
- Pinterest - [Python Brasil](https://br.pinterest.com/pythonbrasil/)
- TikTok - [@python_brasil](https://www.tiktok.com/@python_brasil)
