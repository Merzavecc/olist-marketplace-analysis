import sqlite3
import pandas as pd
from pathlib import Path

folder = Path(r"C:\Users\Керим\PycharmProjects\pythonProject")
print("Папка существует:", folder.exists())
print("Найдено csv:", len(list(folder.glob("*.csv"))))

conn = sqlite3.connect("olist.db")

for file in folder.glob("*.csv"):
    df = pd.read_csv(file)
    df.to_sql(file.stem, conn, if_exists="replace", index=False)
    print(f"Загружено: {file.stem}, строк: {len(df)}")

conn.close()