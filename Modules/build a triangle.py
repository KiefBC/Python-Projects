# side = int(input())
# c = '#'
# for i in range(side):
#     print((c*i).rjust(side-1)+c+(c*i).ljust(side-1))

number_of_tri = int(input('How tall do you want your Triangle Fortress?  > '))  # this will tell us how high the triangle will be
counter = 1  # because we want the top of our tree to be one "#"

for _ in range(number_of_tri):  # we use "_" because we don't need the value
    # we center the # via the height of our triangle * 2
    print(("#" * counter).center(number_of_tri * 2))  # counter tracks which row we are on that's why we default 1
    counter += 2  # for every one "#" we add, we have to add one whitespace
