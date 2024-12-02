import sqlite3

connectt = sqlite3.connect('AnimalKingdom.sl3', 5)
cur = connectt.cursor()

cur.execute("INSERT INTO Animal(name) VALUES ('Лев');")
cur.execute("INSERT INTO Animal(name) VALUES ('Крокодил');")
cur.execute("INSERT INTO Animal(name) VALUES ('Орел');")
cur.execute("INSERT INTO Animal(name) VALUES ('Морська черепаха');")
cur.execute("INSERT INTO Animal(name) VALUES ('Мавпа');")
cur.execute("INSERT INTO Animal(name) VALUES ('Лев - Ссавець');")
cur.execute("INSERT INTO Animal(name) VALUES ('Крокодил - Плазун');")
cur.execute("INSERT INTO Animal(name) VALUES ('Орел - Птах');")
cur.execute("INSERT INTO Animal(name) VALUES ('Морська черепаха - Плазун');")
cur.execute("INSERT INTO Animal(name) VALUES ('Мавпа - Ссавець');")
cur.execute("UPDATE animal SET name='Сокіл' WHERE rowid = 3")

connectt.commit()
connectt.close()