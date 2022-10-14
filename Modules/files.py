# example of opening a file
my_file = open('my_file.txt')

# 'r' 	Open for reading. If the file doesn't exist, an error occurs.
# 'w' 	Open for writing and truncating. If the file already exists, it will be overwritten.
# 'a' 	Open for writing. If the file already exists, append to the end of the file.
# 'b' 	Open in binary mode.
# '+' 	Open for updating (reading and writing).
# 't' 	Open as a text

# As you can see, we specified the mode parameter right after the name of the file. Now the file is opened for writing.
my_file_mode = open('my_file.txt', 'w')

# The encoding parameter specifies the encoding that should be used to decode or encode the text file. It is needed when we open the file as a text

# UTF-8
file_utf8 = open('my_file.txt', encoding='utf-8')

# UTF-16
file_utf16 = open('my_file.txt', encoding='utf-16')

# CP1252
file_cp1252 = open('my_file.txt', encoding='cp1252')

# closing the file
my_file.close()

# To read the file, you can:
# use the read(size) method;
# use the readline(size) method;
# use the readlines() method;
# iterate over the lines with a for loop.

# read(size) reads the size bytes of a file. If the parameter isn't specified, the whole file is read into a single variable. So, this is what we'll get if we apply it to our file:
file = open('animals.txt', 'r')
print(file.read())
# The output:
# Dog
# Cat
# Rabbit
# Sea turtle
# Penguin
file.close()

# readline(size) is similar to read(size) but it reads size bytes from a single line, not the whole file. Lines in files are separated by newline escape sequences: '\n', '\r' or '\r\n'
file = open('animals.txt', 'r')
print(file.readline(3))
print(file.readline(3))
print(file.readline(3))
print(file.readline(3))
print(file.readline(3))
print(file.readline(3))
# The output:
# Dog
#
#
# Cat
#
#
# Rab
# bit
file.close()

# readlines() allows us to read the whole file as a list of lines. Here's what it looks like:
file = open('animals.txt', 'r')
print(file.readlines())
# The output:
# ['Dog\n', 'Cat\n', 'Rabbit\n', 'Sea turtle\n', 'Penguin']

# read test.txt
file = open('test.txt', 'r')
for i in file.readlines(0):
    print(i[0])
file.close()

file.close()

# The most efficient way to read the contents of a file is to iterate over its lines with for loop.
file = open('animals.txt', 'r')
for line in file:
    print(line)
# The output:
# Dog
#
# Cat
#
# Rabbit
#
# Sea turtle
#
# Penguin
file.close()

# Now that the file is open, we can use the write() method. file.write() allows us to write strings to a file – other types of data need to be converted to a string beforehand
file = open('test_file.txt', 'w', encoding='utf-8')
file.write('This is a line in a test file!')
file.close()

# Suppose, we have a list of names and we want to write them to a file, each on a new line. This is how it can be done:
names = ['Kate', 'Alexander', 'Oscar', 'Mary']

name_file = open('names.txt', 'w', encoding='utf-8')

# write the names on separate lines
for name in names:
    name_file.write(name + '\n')
name_file.close()

# If we print the lines of the file as a list, this is what we'll get:
# ['Kate\n', 'Alexander\n', 'Oscar\n', 'Mary\n']

# Another method for writing the files is file.writelines().
# writelines() takes an iterable sequence of strings and writes them to the file. Just like with write(), we need to specify the line separators ourselves.
names = ['Kate\n', 'Alexander\n', 'Oscar\n', 'Mary\n']
name_file = open('names.txt', 'w', encoding='utf-8')
name_file.writelines(names)
name_file.close()

# Suppose, we want to add the name Rachel to the names.txt.
name_file = open('names.txt', 'a', encoding='utf-8')
name_file.write('Rachel\n')
name_file.close()

###
# THIS HAD ME STUMPED!!!!
###

# The file animals.txt has a list of animals, each written on a new line. For example:
#
# rabbit
# cat
# turtle
#
# Create a new file, animals_new.txt, where those animals are written on a single line and separated by a whitespace.
# Don't forget to close all files!

file = open('animals.txt')
file_n = open('animals_new.txt', 'w')
file1 = file.readlines()
for line in file1:
    file_n.write(line.replace('\n', ' '))
file.close()
file_n.close()

# OR OR OR OR OR OR OR OR

with open('animals.txt', 'r', encoding='utf_8') as old_file:
    with open('animals_new.txt', 'w', encoding='utf_8') as new_file:
        for animal in old_file:
            new_file.write(animal.replace('\n', ' '))