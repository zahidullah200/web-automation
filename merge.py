import PyPDF2

def merge_pdfs(pdf_files, output_path):
    merger = PyPDF2.PdfMerger()

    for pdf_file in pdf_files:
        merger.append(pdf_file)

    with open(output_path, 'wb') as output_file:
        merger.write(output_file)

    print(f"PDF files merged successfully into '{output_path}'")

