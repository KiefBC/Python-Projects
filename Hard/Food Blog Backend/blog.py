from blog_backend import FoodBlogDB

"""
I don't see any reason to have our "blog" part of our backend. 
To me, it makes more sense to separate the two.
Have the blog itself call the backend.
"""


def main():
    fb = FoodBlogDB()
    fb.pop_table()


if __name__ == '__main__':
    main()
