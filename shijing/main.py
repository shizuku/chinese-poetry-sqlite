import json, sys
import sqlite3
from collections import OrderedDict


text = json.loads(open('./shijing.json', 'r').read())
con = sqlite3.connect("./shijing.db")

c = con.cursor()
c.execute('''CREATE TABLE "shijing" ("value" INTEGER NOT NULL PRIMARY KEY,
                "title" VARCHAR(255) NOT NULL,
                "chapter" VARCHAR(255) NOT NULL,
                "section" VARCHAR(255) NOT NULL,
                "content" TEXT)''')

for i in text:
    s=""
    for j in i["content"]:
        s+=j+"\n"
    c.execute("INSERT INTO shijing (title, chapter, section, content) VALUES (?,?,?,?)",(i["title"],i["chapter"],i["section"],s))
 
con.commit()
con.close()
