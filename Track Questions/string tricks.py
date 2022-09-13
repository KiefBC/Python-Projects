# take our input, UPPER it cus grades are capitalized, and finally split it
grades = input().upper().split()
# create our result and count how many A's we have
result = grades.count('A') / ((len(grades)))  # A's / Grades
print(round(result, 2))  # print em out print em out to 2 decimal places