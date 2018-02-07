from sys import argv
# dont' really understand lines 1 or 3
script, filename = argv
# open a file that has to be specified at the beginning
txt = open(filename)
# this retrieves the text you specified in line 5
print "Here's your file %r:" % filename
print txt.read()
# not really sure why this section is here, but it waits for the person to typ info in
print "Type the filename again:"
file_again = raw_input("> ")
#this is does the same thing as line 5
txt_again = open(file_again)
# this does the same thing as line 8, except from input from the person
print txt_again.read()
txt.close()
txt_again.close()
