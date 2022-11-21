import sqlite3
import json


class FoodBlog:

    def __init__(self):
        self.conn = sqlite3.connect('food_blog.db')
        self.c = self.conn.cursor()
        self.initialize_db()

    def initialize_db(self):
        """
        HAVE YOU EVER WONDERED HOW BUTTERFLIES WORK?
        :return:
        """
        # OUR DATA
        with open("moms_recipe.json") as recipe:
            the_recipe = json.load(recipe)

        # CREATE OUR TABLES
        self.c.executescript("""
            CREATE TABLE IF NOT EXISTS meals (meal_id INTEGER PRIMARY KEY, meal_name TEXT UNIQUE NOT NULL);
            CREATE TABLE IF NOT EXISTS ingredients (ingredient_id INTEGER PRIMARY KEY, ingredient_name TEXT UNIQUE NOT NULL);
            CREATE TABLE IF NOT EXISTS measures (measure_id INTEGER PRIMARY KEY, measure_name TEXT UNIQUE);
            CREATE TABLE IF NOT EXISTS recipes (recipe_id INTEGER PRIMARY KEY, recipe_name TEXT NOT NULL, recipe_description TEXT);
                            """)
        self.conn.commit()

        # ADD DATA TO OUR DB
        for item in the_recipe:
            for k, v in enumerate(the_recipe.get(item)):
                # we use {item}[:-1] to remove the "s"  off the table names (notice meals and meal_id)
                # INSERT INTO meals (meal_name) VALUES (1, "breakfast") is an example of below
                self.c.execute(f"INSERT OR IGNORE INTO {item} ({item[:-1]}_id, {item[:-1]}_name) values({k}, '{v}');")
                self.conn.commit()

    def pop_table(self):
        while True:
            recipe_name = input('Recipe name: ')
            if recipe_name == '':
                break

            else:
                self.c.execute(f"INSERT OR IGNORE INTO recipes (recipe_name) VALUES ('{recipe_name}')")
                self.conn.commit()
                recipe_description = input('Recipe description: ')
                self.c.execute(f"UPDATE recipes SET recipe_description = '{recipe_description}' WHERE recipe_name = '{recipe_name}'")
                self.conn.commit()
                self.c.execute("SELECT * FROM recipes")
                items = self.c.fetchall()
                print(items)
                continue

        # TERMINATION
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    fb = FoodBlog()
    fb.pop_table()
