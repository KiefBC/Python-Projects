import sqlite3

# Create our DB food_blog.db
conn = sqlite3.connect('food_blog.db')
c = conn.cursor()

# Create our meals table.
c.execute("""CREATE TABLE IF NOT EXISTS meals (
            meal_id INTEGER PRIMARY KEY,
            meal_name TEXT UNIQUE NOT NULL)""")
conn.commit()

# Add items to our meals table.
c.execute("""INSERT OR IGNORE INTO meals (meal_name)
          VALUES
          ("breakfast"),
          ("brunch"),
          ("lunch"),
          ("supper")""")
conn.commit()


# Create our ingredients table.
c.execute("""CREATE TABLE IF NOT EXISTS ingredients (
            ingredient_id INTEGER PRIMARY KEY,
            ingredient_name TEXT UNIQUE NOT NULL)""")
conn.commit()

# Add ingredients to our ingredients table
c.execute("""INSERT OR IGNORE INTO ingredients (ingredient_name)
          VALUES
          ("milk"),
          ("cacao"),
          ("strawberry"),
          ("blueberry"),
          ("blackberry"),
          ("sugar")""")
conn.commit()

# Create our measures table.
c.execute("""CREATE TABLE IF NOT EXISTS measures (
            measure_id INTEGER PRIMARY KEY,
            measure_name TEXT UNIQUE)""")
conn.commit()

c.execute("""INSERT OR IGNORE INTO measures (measure_name)
          VALUES
          ("ml"),
          ("g"),
          ("l"),
          ("cup"),
          ("tbsp"),
          ("tsp"),
          ("dsp"),
          ("")""")
conn.commit()

# # Verify we added it
# c.execute("SELECT * FROM measures")
# items = c.fetchall()
# print(items)

# Terminate our DB Connection
conn.close()
