import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://myuser:mypassword@localhost:5432/mydb")

query = "SELECT * FROM apartments WHERE price < 5000000"
df = pd.read_sql(query, engine)

print(df)

df.to_csv("output.csv", index=False)
