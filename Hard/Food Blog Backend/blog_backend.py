import sqlite3
import json


class FoodBlogDB:
    """
    Our fancy smancy, triple bling ring a ding ding Food blog DATABASE!
    OMGOSH SO COOL
    """

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

    def verify_ingredients(self, ingredient):
        """
        Checking to see if the ingredient the user wants to use is in our Pantry (database)
        Hopefully the resident mouse ignores the cheese this time....
        :param ingredient: 
        :return: 
        """

        rows = self.execute_query(f'SELECT ingredient_id from ingredients '
                                  f'WHERE ingredient_name LIKE "%{ingredient}%"').fetchall()
        if len(rows) == 1:
            return rows[0][0]
        return None

    def verify_measure(self, measure):
        """
        It is inconceivable that someone could carelessly input wrong measurements!
        Why, it would almost be a...... USER ERROR! THE HORROR!
        :param measure: 
        :return: 
        """
        if measure == "":
            return self.execute_query('SELECT measure_id from measures '
                                      'WHERE measure_name = ""').fetchone()[0]
        rows = self.execute_query(f'SELECT measure_id from measures '
                                  f'WHERE measure_name LIKE "{measure}%"').fetchall()
        if len(rows) == 1:
            return int(rows[0][0])
        return None

    def verify_amount(self, amount):
        """
        I've asked people for a cola of cola, and they look at me like I'm weird??
        Everyone knows a cola is 1L and a cola of a cola is wanting 1L of cola...
        :param amount: 
        :return: 
        """
        if amount == "":
            return self.execute_query('SELECT measure_id from measures '
                                      'WHERE measure_name = ""').fetchone()[0]
        rows = self.execute_query(f'SELECT measure_id from measures '
                                  f'WHERE measure_name LIKE "{amount}%"').fetchall()
        if len(rows) == 1:
            return int(rows[0][0])
        return None

    def execute_query(self, query):
        """
        So much easier just being able to call a function instead of constantly
        writing our execute commands.
        :param query:
        :param command:
        :return:
        """
        conn = sqlite3.connect('food_blog.db')
        c = conn.cursor()
        result = c.execute(query)
        conn.commit()
        return result

    def pop_table(self):
        """
        This will allow the user to add a recipe name and description to the database
        :return:
        """
        default = 'Overcooked and dried Turkey is the worst'
        default_ = '1 2 3'

        while True:
            print('\nPass the empty recipe name to exit.\n')
            recipe_name = input('Your Recipe Name <Press "Enter" to stop>: ')
            if recipe_name == '':
                break
            else:
                recipe_description = input('Describe Your Recipe: ') or default
                insert_query = f"INSERT OR IGNORE INTO recipes (recipe_name, recipe_description) VALUES ('{recipe_name}', '{recipe_description}')"
                recipe_id = self.execute_query(insert_query).lastrowid
                recipe_served = input('\n1) breakfast  2) brunch  3) lunch  4) supper\nEnter proposed meals separated by a space: ').split() or default_
                for time in recipe_served:
                    insert_query = f'INSERT INTO serve (recipe_id, meal_id) VALUES ("{recipe_id}", "{time}")'
                    self.execute_query(insert_query)
                while True:
                    quantity_input = [x for x in input('\nInput quantity of ingredient <Press "Enter" to stop>: ').split()]
                    if len(quantity_input) != 0:
                        the_amount, the_ingredient = [quantity_input[1], quantity_input[-1]]
                        the_measure = "" if len(quantity_input) == 2 else quantity_input[1]

                        # VERIFY THE DATA
                        quantity = self.verify_amount(the_amount)
                        measure_id = self.verify_measure(the_measure)
                        ingredient_id = self.verify_ingredients(the_ingredient)

                        # If something is None .... BAD!
                        if None in [quantity, measure_id, ingredient_id]:
                            print('\nRecipes is inconclusive, please try again!')
                        else:
                            print('\nInserting data into the database....')
                            insert_query = f'INSERT INTO quantity (measure_id, ingredient_id, quantity, recipe_id) VALUES ({measure_id}, {ingredient_id}, {quantity}, {recipe_id})'
                            self.execute_query(insert_query)
                            print('\nData input complete. Thanks for using OBSTERGO. Enjoy your soy.')
                    else:
                        break
        # TERMINATION ###
        self.conn.close()
