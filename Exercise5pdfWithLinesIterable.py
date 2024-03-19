from fpdf import FPDF
import pandas

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pandas.read_csv("Files/topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Tittle
    pdf.set_font(family="Helvetica", style="B", size=20)
    pdf.set_text_color(60, 60, 60)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="C", ln=1)

    # Exercise area
    pdf.line(10, 23, 200, 23)
    pdf.line(10, 33, 200, 33)
    pdf.line(10, 283, 200, 283)

    # Footer
    pdf.ln(265)
    pdf.set_font(family="Helvetica", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(277)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("Files/output.pdf")
