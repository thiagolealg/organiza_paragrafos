# Ferramenta de Reordenação de Parágrafos de Word

Este pacote contém uma ferramenta de linha de comando (`reorder_tool.exe`) para reordenar parágrafos em um arquivo `.docx` com base em um arquivo de referência de texto.

## Arquivos Incluídos

*   `dist/reorder_tool.exe`: O programa executável.
*   `ref_order.txt`: Arquivo de exemplo com a ordem correta dos parágrafos.
*   `example_input.docx`: Arquivo `.docx` de exemplo com parágrafos desordenados.
*   `README.md`: Este arquivo.

## Como Usar

1.  Abra um terminal (Prompt de Comando ou PowerShell).
2.  Navegue até a pasta onde você descompactou os arquivos (ou a pasta `dist` se estiver usando o projeto completo).
3.  Execute o comando:

    ```bash
    .\reorder_tool.exe CAMINHO_PARA_SEU_ARQUIVO.docx -r CAMINHO_PARA_REFERENCIA.txt -o CAMINHO_PARA_SAIDA.docx
    ```

    **Exemplo usando os arquivos fornecidos (execute de dentro da pasta `dist`):**

    ```bash
    .\reorder_tool.exe ..\example_input.docx -r ..\ref_order.txt -o ..\resultado_ordenado.docx
    ```

    *   Substitua `CAMINHO_PARA_SEU_ARQUIVO.docx` pelo caminho do arquivo Word que você deseja reordenar.
    *   `-r`: (Opcional) Use para especificar o caminho do arquivo de texto com a ordem correta. O padrão é `ref_order.txt` na mesma pasta do executável.
    *   `-o`: (Opcional) Use para especificar o nome do arquivo `.docx` de saída. O padrão é `sorted_output.docx` na mesma pasta do executável.

## Requisitos (para executar o .exe)

*   Windows.
*   Nenhuma dependência externa necessária, pois o modelo de linguagem está embutido (ou deveria estar) no `.exe`.
