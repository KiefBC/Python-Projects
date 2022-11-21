import sqlite3
import json


class FoodBlogDB:

    def __init__(self):
        self.conn = sqlite3.connect('food_blog.db')
        self.c = self.conn.cursor()
        self.initialize_db()

    def initialize_db(self):
        """
        HAVE YOU EVER WONDERED HOW BUTTERFLIES WORK?
        :return:
        """

        # TURNING ON PK AND FK
        self.execute_query("PRAGMA foreign_keys = ON;")

        # OUR DATA
        with open("moms_recipe.json") as recipe:
            the_recipe = json.load(recipe)

        # CREATE OUR TABLES
        self.c.executescript("""
            CREATE TABLE IF NOT EXISTS meals (
            meal_id INTEGER PRIMARY KEY, 
            meal_name TEXT UNIQUE NOT NULL);
            
            CREATE TABLE IF NOT EXISTS ingredients (
            ingredient_id INTEGER PRIMARY KEY, 
            ingredient_name TEXT UNIQUE NOT NULL);
            
            CREATE TABLE IF NOT EXISTS measures (
            measure_id INTEGER PRIMARY KEY, 
            measure_name TEXT UNIQUE);
            
            CREATE TABLE IF NOT EXISTS recipes (
            recipe_id INTEGER PRIMARY KEY, 
            recipe_name TEXT NOT NULL, 
            recipe_description TEXT);
            
            CREATE TABLE IF NOT EXISTS serve (
            serve_id INTEGER PRIMARY KEY, 
            recipe_id INTEGER NOT NULL, 
            meal_id INTEGER NOT NULL,
            FOREIGN KEY (recipe_id)
                REFERENCES recipes (recipe_id),
            FOREIGN KEY (meal_id)
                REFERENCES meals (meal_id));
            """)
        self.conn.commit()

        # ADD DATA TO OUR DB
        for item in the_recipe:
            for k, v in enumerate(the_recipe.get(item)):
                # we use {item}[:-1] to remove the "s"  off the table names (notice meals and meal_id)
                # INSERT INTO meals (meal_name) VALUES (1, "breakfast") is an example of below
                self.c.execute(f"INSERT OR IGNORE INTO {item} ({item[:-1]}_id, {item[:-1]}_name) values({k}, '{v}');")
                self.conn.commit()

    def execute_query(self, command):
        conn = sqlite3.connect('food_blog.db')
        c = conn.cursor()
        result = c.execute(command)
        conn.commit()
        return result

    def pop_table(self):
        """
        This will allow the user to add a recipe name and description to the database
        :return:
        """
        while True:
            print('Pass the empty recipe name to exit.\n')
            recipe_name = input('Recipe name: ')
            if recipe_name == '':
                break

            else:
                recipe_description = input('Recipe description: ')
                insert_query = f"INSERT OR IGNORE INTO recipes (recipe_name, recipe_description) VALUES ('{recipe_name}', '{recipe_description}')"
                recipe_id = self.execute_query(insert_query).lastrowid
                recipe_served = input('1) breakfast  2) brunch  3) lunch  4) supper\nWhen the dish can be served: ').split()
                for time in recipe_served:
                    insert_query = f'INSERT INTO serve (recipe_id, meal_id) VALUES ("{recipe_id}", "{time}")'
                    self.execute_query(insert_query)
                # continue

        # TERMINATION
        self.conn.close()
