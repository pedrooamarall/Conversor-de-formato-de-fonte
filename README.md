# Conversor de Fontes para WOFF2

Este projeto Python permite converter arquivos de fontes (TTF, OTF) para o formato WOFF2, otimizado para uso na web.

## Requisitos

- Python 3.x
- `fonttools` (instalado automaticamente via `pip`)
- `brotli` (instalado automaticamente via `pip`)

## Configuração do Ambiente

1.  **Navegue até o diretório do projeto:**

    ```bash
    cd font_converter_project
    ```

2.  **Crie um ambiente virtual (recomendado):**

    ```bash
    python3.11 -m venv venv
    ```

3.  **Ative o ambiente virtual:**

    -   No Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

    -   No Windows:

        ```bash
        .\venv\Scripts\activate
        ```

4.  **Instale as dependências:**

    ```bash
    pip install fonttools brotli
    ```

## Como Usar

Para converter um ou mais arquivos de fonte para WOFF2, execute o script `main.py` seguido pelos caminhos dos arquivos de entrada. Você pode especificar um diretório de saída opcional.

### Exemplo de Uso:

-   **Converter um único arquivo:**

    ```bash
    python3.11 main.py sua_fonte.ttf
    ```

-   **Converter múltiplos arquivos:**

    ```bash
    python3.11 main.py fonte1.otf fonte2.ttf
    ```

-   **Converter e salvar em um diretório específico:**

    ```bash
    python3.11 main.py sua_fonte.ttf -o saida_woff2
    ```

Os arquivos WOFF2 convertidos serão salvos no mesmo diretório dos arquivos de entrada, a menos que um diretório de saída seja especificado.

## Estrutura do Projeto

```
font_converter_project/
├── venv/                 # Ambiente virtual (ignorável pelo Git)
├── main.py               # Script principal para conversão de fontes
├── README.md             # Este arquivo
├── OpenSans-Regular.ttf  # Exemplo de fonte TTF (para teste)
└── OpenSans-Regular.woff2 # Exemplo de fonte WOFF2 convertida (para teste)
```


