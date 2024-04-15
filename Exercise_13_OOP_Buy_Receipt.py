import pandas
from Exercise13.pdf_code import PDF


df = pandas.read_csv("Exercise13/articles.csv")

print(df)
article_id = input("Choose the id of an article to buy: ")