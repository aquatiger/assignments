from sys import argv

script, input_file = argv
# print all of the file that is open, although I don't understand how it knows because f is undefined
def print_all(f):
    print f.read()
#not sure what rewind is, but apparently goes to the beginning
def rewind(f):
    f.seek(0)
#print whatever the line number is and then print the contents of the file for that line
def print_a_line(line_count, f):
    print line_count, f.readline()
#opens current file as specified in the command line
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1 # current line is 1
print_a_line(current_line, current_file)

current_line = current_line + 1 #current line is 2
print_a_line(current_line, current_file)
#somehow python updates the count
current_line = current_line + 1 #current line is 3
print_a_line(current_line, current_file)
