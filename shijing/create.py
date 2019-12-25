import sqlite3

con = sqlite3.connect("shijing.db")

c = con.cursor()
c.execute('''CREATE TABLE "shijing" ("value" INTEGER NOT NULL PRIMARY KEY,
                "title" VARCHAR(255) NOT NULL,
                "chapter" VARCHAR(255) NOT NULL,
                "section" VARCHAR(255) NOT NULL,
                "content" TEXT)''')

con.commit()
con.close()
