import pandas
from fpdf import FPDF

PATH = "Exercise13/articles.csv"

df = pandas.read_csv(PATH, dtype={"id": str, "in stock": int})


class Receipt:
    def __init__(self, receipt_nr):
        self.receipt_nr = receipt_nr
        self.article = df.loc[df["id"] == article_id, "name"].squeeze()
        self.price = df.loc[df["id"] == article_id, "price"].squeeze()

    def to_pdf(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.receipt_nr}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.price}", ln=1)

        pdf.output("receipt.pdf")


print(df)
article_id = input("Choose the id of an article to buy: ")

try:
    stock = df.loc[df["id"] == article_id, "in stock"].squeeze()
    # Checks if in stock and detracts one
    if stock > 0:
        df.loc[df["id"] == article_id, "in stock"] = stock-1
        df.to_csv(PATH, index=False)
        receipt = Receipt(article_id)
        receipt.to_pdf()
    else:
        print("Item not in stock")
except ValueError:
    print("Item does not exist")
