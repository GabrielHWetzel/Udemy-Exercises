from fpdf import FPDF


class PDF:
    def __init__(self, receipt_nr, article, price):
        self.receipt_nr = receipt_nr
        self.article = article
        self.price = price

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

pdf.set_font(family="Times", size=16, style="B")
pdf.cell(w=50, h=8, txt=f"Receipt nr.1", ln=1)

pdf.set_font(family="Times", size=16, style="B")
pdf.cell(w=50, h=8, txt=f"Article: Laptop Sven", ln=1)

pdf.set_font(family="Times", size=16, style="B")
pdf.cell(w=50, h=8, txt=f"Price: 999", ln=1)

pdf.output("receipt.pdf")
