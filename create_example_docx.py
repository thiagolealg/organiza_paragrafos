from docx import Document
import random

def create_shuffled_docx(output_path, reference_path, encoding='utf-8'):
    """Cria um docx com parágrafos de um txt embaralhados."""
    try:
        with open(reference_path, 'r', encoding=encoding) as f:
            paragraphs = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Erro ao ler '{reference_path}': {e}")
        return

    if not paragraphs:
        print(f"Nenhum parágrafo encontrado em '{reference_path}'")
        return

    random.shuffle(paragraphs)

    doc = Document()
    print(f"Criando '{output_path}' com {len(paragraphs)} parágrafos embaralhados...")
    for p_text in paragraphs:
        doc.add_paragraph(p_text)

    try:
        doc.save(output_path)
        print(f"Arquivo '{output_path}' criado com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar '{output_path}': {e}")

if __name__ == "__main__":
    ref_file = 'ref_order.txt'
    output_file = 'example_input.docx'
    create_shuffled_docx(output_file, ref_file)
