import pandas
from fpdf import FPDF

PATH = "Exercise13/articles.csv"

df = pandas.read_csv(PATH, dtype={"id": str, "in stock": int})


class Article:
    def __init__(self, article_id):
        self.id = article_id
        self.article = df.loc[df["id"] == self.id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.id, "price"].squeeze()

    def available(self):
        in_stock = df.loc[df["id"] == self.id, "in stock"].squeeze()
        df.loc[df["id"] == article_id, "in stock"] = in_stock - 1
        df.to_csv(PATH, index=False)
        return in_stock


class Receipt:
    def __init__(self, article):
        self.article = article

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.article.id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.article}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output("receipt.pdf")


print(df)
article_id = input("Choose the id of an article to buy: ")
try:
    article = Article(article_id)
    # Checks if in stock and detracts one
    if article.available():
        receipt = Receipt(article)
        receipt.generate()
    else:
        print("Item not in stock")
except ValueError:
    print("Item does not exist")
