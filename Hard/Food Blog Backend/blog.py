from blog_backend import FoodBlogDB
from sys import argv
import argparse

"""
I don't see any reason to have our "blog" part of our backend. 
To me, it makes more sense to separate the two.
Have the blog itself call the backend.
"""


def main():

    # LETS NAME OUR DATABASE OR CHECK THE COMMANDLINE
    db_name = argv[1] if len(argv) >= 2 else 'food_blog.db'
    with open("moms_recipe.json") as recipe:
        the_recipe = json.load(recipe)
    fb = FoodBlogDB(db_name)

    if len(argv) == 4:
        ingredients = tuple(argv[2].split('=')[1].strip('"').split(','))
        meals = tuple(argv[3].split('=')[1].strip('"').split(','))
        print(ingredients, meals)
        fb.recipe_query(ingredients, meals)
    else:
        fb.initialize_db()
        fb.pop_table()




if __name__ == '__main__':
    args = arguments()
    main()
