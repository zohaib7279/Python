# pip install PyMuPDF
import fitz  # PyMuPDF

pdf_file = "output.pdf"
doc = fitz.open(pdf_file)

for i, page in enumerate(doc):
    pix = page.get_pixmap()
    pix.save(f"page_{i+1}.png")
