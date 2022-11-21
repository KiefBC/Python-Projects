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

            CREATE TABLE IF NOT EXISTS quantity (
            quantity_id INTEGER PRIMARY KEY, 
            measure_id INTEGER NOT NULL, 
            ingredient_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            recipe_id INTEGER NOT NULL,
            FOREIGN KEY (measure_id)
                REFERENCES measures (measure_id),
            FOREIGN KEY (ingredient_id)
                REFERENCES ingredients (ingredient_id),
            FOREIGN KEY (recipe_id)
                REFERENCES recipes (recipe_id)
            );
            """)
        self.conn.commit()

        # ADD DATA TO OUR DB
        for item in the_recipe:
            for k, v in enumerate(the_recipe.get(item)):
                # we use {item}[:-1] to remove the "s"  off the table names (notice meals and meal_id)
                # INSERT INTO meals (meal_name) VALUES (1, "breakfast") is an example of below
                insert_query = f"INSERT OR IGNORE INTO {item} ({item[:-1]}_id, {item[:-1]}_name) values({k}, '{v}');"
                self.execute_query(insert_query)

    def execute_query(self, command):
        """
        So much easier just being able to call a function instead of constantly
        writing our execute commands. I should factor in executescript as well.
        :param command:
        :return:
        """
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

        # OUR DATA
        with open("moms_recipe.json") as recipe:
            the_recipe = json.load(recipe)

        while True:
            print('\nPass the empty recipe name to exit.\n')
            recipe_name = input('Recipe name: ')
            if recipe_name == '':
                break
            else:
                recipe_description = input('Recipe description: ')
                insert_query = f"INSERT OR IGNORE INTO recipes (recipe_name, recipe_description) VALUES ('{recipe_name}', '{recipe_description}')"
                recipe_id = self.execute_query(insert_query).lastrowid
                recipe_served = input(
                    '\n1) breakfast  2) brunch  3) lunch  4) supper\nEnter proposed meals separated by a space: ').split()
                for time in recipe_served:
                    insert_query = f'INSERT INTO serve (recipe_id, meal_id) VALUES ("{recipe_id}", "{time}")'
                    self.execute_query(insert_query)
                while True:
                    ingred_amount = input('\nInput quantity of ingredient <press enter to stop>: ').split()
                    if len(ingred_amount) != 0:
                        the_amount, the_ingredient = [ingred_amount[0], ingred_amount[-1]]
                        if the_amount not in the_recipe.get('measures'):
                            print('\nThe measure is not conclusive!')
                        else:
                            insert_query = f'INSERT INTO quantity (measure_id, ingredient_id, quantity, recipe_id) VALUES ({measure_id}, {ingredient_id}, {quantity}, {recipe_id})'
                            self.execute_query(insert_query)
                        if the_ingredient not in the_recipe.get('ingredients'):
                            print('\nThe ingredient is not conclusive!')
                        else:
                            insert_query = f'INSERT INTO quantity (measure_id, ingredient_id, quantity, recipe_id) VALUES ({measure_id}, {ingredient_id}, {quantity}, {recipe_id})'
                            self.execute_query(insert_query)
                    else:
                        break

        # TERMINATION ###
        self.conn.close()
