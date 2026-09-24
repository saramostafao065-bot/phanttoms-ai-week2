import sqlite3
import requests

url = "https://jsonplaceholder.typicode.com/posts"
res = requests.get(url)
posts = res.json()

db = "store.db"
con = sqlite3.connect(db)
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        title TEXT,
        body TEXT
    )
""")
con.commit()

for p in posts[:5]:
  cur.execute(
      "INSERT OR IGNORE INTO products (id, title, body) VALUES (?, ?, ?)",
      (p.get("id"), p.get("title"), p.get("body")),
  )
con.commit()

cur.execute("SELECT id, title FROM products WHERE id <= 3")
res1 = cur.fetchall()

cur.execute("SELECT id, title FROM products ORDER BY id DESC")
res2 = cur.fetchall()

con.close()
