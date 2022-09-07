
import pandas as pd

df = pd.read_csv("Resources/city_data.csv")

df.to_html("table.html")
