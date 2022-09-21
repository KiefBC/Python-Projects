import argparse  #  It allows you to pass the arguments through the command line

# ADDING ARGUMENTS

# The ArgumentParser has quite a number of parameters that you can specify, but we only invoked description
parser = argparse.ArgumentParser(description="This program prints recipes \
consisting of the ingredients you provide.")

# add arguments with str.add_argument()
parser.add_argument("-i1", "--ingredient_1")  # optional argument
                                              # or
parser.add_argument("ingredient_1")           # positional argument


# if an argument has a dash - or a double dash -- prefix, it'll be treated as optional
# the parameter “action” is responsible for what should be done with a command-line argument
# instead of making users specify salt as one of the numbered ingredients, we'll let them toggle its presence via
# “store_true” which is used to assign boolean values The salt value will be False by default but if the user lists
# --salt among the arguments, the value will be changed to True
# action = "store_false": the default value is True. For action = "store_true": the default value is False.
parser.add_argument("--salt", action="store_true")


# the argument isn't used as a flag anymore, so, if you'd like to change the value, you will have to define it in
# the command line explicitly: --pepper "True"
parser.add_argument("--pepper", default=False)

# choices parameter might be useful to limit the choice of each ingredient to only those used in our recipes
parser.add_argument("-i2", "--ingredient_2",
                    choices=["pasta", "rice", "potato", "onion",
                             "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")

# PARSING ARGUMENTS

# parse_args() method is used for reading argument strings from the command line
args = parser.parse_args()

# we can access the values specified by a user as attributes of the args
# we can't use short versions of arguments: for example, args.i2 will not work
print(args.ingredient_2)  # onion
# (the value was chosen by a user from the given options)

# In case a user didn't specify an optional argument in the command line, the value is set toNone by default
print(args.ingredient_3)  # None
# (the value wasn't provided by a user)

import argparse

# just a show-off to see what a finished arg code would look like
parser = argparse.ArgumentParser(description="This program prints recipes \
consisting of the ingredients you provide.")

parser.add_argument("-i1", "--ingredient_1", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")
parser.add_argument("-i2", "--ingredient_2", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")
parser.add_argument("-i3", "--ingredient_3", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")
parser.add_argument("-i4", "--ingredient_4", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")
parser.add_argument("-i5", "--ingredient_5", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")

parser.add_argument("--salt", action="store_true",
                    help="Specify if you'd like to use salt in your recipe.")
parser.add_argument("--pepper", default="False",
                    help="Change to 'True' if you'd like to use pepper in your recipe.")

args = parser.parse_args()

ingredients = [args.ingredient_1, args.ingredient_2, args.ingredient_3,
               args.ingredient_4, args.ingredient_5]
if args.salt:
    ingredients.append("salt")
if args.pepper == "True":
    ingredients.append("pepper")

print(f"The ingredients you provided are: {ingredients}")


def find_a_recipe(ingredients):
    ...
    # processes the input and returns a recipe depending on the provided ingredients

# FROM THE USERS PERSPECTIVE

# the format argument value and argument=value are equivalent FOR BOTH
python recipe_book.py -i1=pasta -i2=garlic -i3=tomato_sauce --salt --pepper="True"
# The ingredients you provided are: ['pasta', 'garlic', 'tomato_sauce', None, None, 'salt', 'pepper']
# <The description of the available recipe>
python recipe_book.py -i1 rice -i2 onion -i3 garlic -i4 carrot -i5 tomato_sauce --salt
# The ingredients you provided are: ['rice', 'onion', 'garlic', 'carrot', 'tomato_sauce', 'salt']
# <The description of the available recipe>

# When a user specifies --help or -h as an argument in the command line, the description for each argument is displayed:
python recipe_book.py --help