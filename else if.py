people = 30
cars = 40
trucks = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
# if cars = people then do this
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
# if trucks = people then do this
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
# if people <= trucks then do this
else:
    print "Fine, let's stay home then."
