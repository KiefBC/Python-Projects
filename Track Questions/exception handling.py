try:
    name, surname = input().split()
except Exception as e:
    # this will print any Exception for you with minimal code
    # print(f"The following error occurred : {e}")
    print("You need to enter exactly 2 words. Try again!")
else:
    print(f'Welcome to our party, {name} {surname}')
