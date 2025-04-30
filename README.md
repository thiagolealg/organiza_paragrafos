# Ferramenta de Reordenação de Parágrafos de Word

Este repositório contém um script Python para reordenar parágrafos em um arquivo `.docx` com base em um arquivo de referência de texto, usando similaridade semântica.

## Arquivos Incluídos

*   `reorder_paragraphs.py`: O script Python principal.
*   `requirements.txt`: As dependências Python necessárias.
*   `ref_order.txt`: Arquivo de exemplo com a ordem correta dos parágrafos.
*   `example_input.docx`: Arquivo `.docx` de exemplo com parágrafos desordenados.
*   `create_example_docx.py`: Script auxiliar para gerar o `example_input.docx`.
*   `.gitignore`: Configuração para ignorar arquivos desnecessários no Git.
*   `README.md`: Este arquivo.

## Como Usar (Executando o Script Python)

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/thiagolealg/organiza_paragrafos.git
    cd organiza_paragrafos
    ```

2.  **Crie um ambiente virtual (recomendado) e ative-o:**
    ```bash
    python -m venv .venv
    # Windows
    .\.venv\Scripts\activate
    # Linux/macOS
    # source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o script:**
    ```bash
    python reorder_paragraphs.py CAMINHO_PARA_SEU_ARQUIVO.docx -r CAMINHO_PARA_REFERENCIA.txt -o CAMINHO_PARA_SAIDA.docx
    ```

    **Exemplo usando os arquivos fornecidos:**
    ```bash
    python reorder_paragraphs.py example_input.docx -r ref_order.txt -o resultado_ordenado.docx
    ```

    *   Substitua `CAMINHO_PARA_SEU_ARQUIVO.docx` pelo caminho do arquivo Word que você deseja reordenar.
    *   `-r`: (Opcional) Use para especificar o caminho do arquivo de texto com a ordem correta. O padrão é `ref_order.txt`.
    *   `-o`: (Opcional) Use para especificar o nome do arquivo `.docx` de saída. O padrão é `sorted_output.docx`.

## Como Gerar o Executável (.exe) (Opcional)

Se preferir criar um arquivo `.exe` único que não dependa de uma instalação Python separada:

1.  Siga os passos 1 a 3 da seção "Como Usar" para configurar o ambiente e instalar as dependências.
2.  Instale o PyInstaller:
    ```bash
    pip install pyinstaller
    ```
3.  Execute o PyInstaller (pode demorar um pouco):
    ```bash
    # Certifique-se que o modelo foi baixado executando o script ao menos uma vez
    # O comando abaixo assume o local padrão do cache no Windows.
    # Ajuste o caminho do cache se necessário.
    pyinstaller --onefile --name reorder_tool --clean --add-data "%USERPROFILE%\.cache\huggingface\hub\models--sentence-transformers--all-MiniLM-L6-v2;sentence-transformers/all-MiniLM-L6-v2" reorder_paragraphs.py
    ```
4.  O executável `reorder_tool.exe` estará na pasta `dist`.

## Requisitos (para executar o script Python)

*   Python 3.8+
*   Dependências listadas em `requirements.txt`.
