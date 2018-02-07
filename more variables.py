# The beginning of a joke
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# The combination of the preceding
y = "Those who know %s and those who %s." % (binary, do_not)

# the point of the preceding
print x
print y

# the start of another joke
print "I said: %r." %x
print "I also said: '%s'." % y
# predetermined response
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# the point of the preceding
print joke_evaluation % hilarious

# instructions for a new learning experience
w = "This is the left side of..."
e = "a string with a right side."

print w + e
