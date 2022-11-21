import sqlite3

# Create our DB food_blog.db
conn = sqlite3.connect('food_blog.db')
c = conn.cursor()

# OUR DATA
data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
        "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
        "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}

# CREATE OUR TABLES
c.executescript("""
    CREATE TABLE IF NOT EXISTS meals (meal_id INTEGER PRIMARY KEY, meal_name TEXT UNIQUE NOT NULL);
    CREATE TABLE IF NOT EXISTS ingredients (ingredient_id INTEGER PRIMARY KEY, ingredient_name TEXT UNIQUE NOT NULL);
    CREATE TABLE IF NOT EXISTS measures (measure_id INTEGER PRIMARY KEY, measure_name TEXT UNIQUE);""")
conn.commit()

# ADD DATA TO OUR DB
for i in data.keys():
    # for loop grabs table names via i for the SELECT statement and the data[index]
    # x += itself to create an index
    c.executemany(f"INSERT OR IGNORE INTO {i} VALUES (?, ?)", [x for x in enumerate(data[i])])


c.execute("SELECT * FROM meals")
print(c.fetchall())

# Terminate our DB Connection
conn.commit()
conn.close()
