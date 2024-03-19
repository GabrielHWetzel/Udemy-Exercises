import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Exercise6/*.txt")

# Initiate PDF
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:

    filename = Path(filepath).stem.title()
    with open(filepath, 'r') as file:
        file_text = file.readline()

    pdf.add_page()
    pdf.set_font(family="Helvetica", size=22, style="B")
    pdf.cell(w=0, h=15, txt=filename, ln=1)

    pdf.set_font(family="Helvetica", size=12)
    pdf.multi_cell(w=0, h=6, txt=file_text)

pdf.output("Exercise6/pdf.pdf")
