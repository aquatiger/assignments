#from sys import exit

def start():
    print "Choose where you want to start:"
    print "1 for house"
    print "2 for palace"
    print "3 for cave"

# just did goofy prompt for fun
    starting_point = raw_input('!@#  ')

    if starting_point == "1":
        house()
    elif starting_point == "2":
        palace()
    else:
        cave()

def house():
    print "You are in your beautiful home."
    print "1. So will you take Interstate 5?"
    print "2. Or will you go for a mountain hike?"
    print "3. Or will you go for a drive in the city?"

    house_route = raw_input('>>> ')

    if house_route == "1":
        I5()
    elif house_route == "2":
        hike()
    elif house_route == "3":
        city_drive()
    else:
        print "You just won a free colonoscopy."
        exit(0)

def palace():
    print "1. Will you have your chauffeur drive you on I-5?"
    print "2. Or will you take a mountain hike?"
    print "3. Or call your sibling for a drive to the mall?"

    palace_route = raw_input('>>> ')

    if palace_route == "1":
        I5()
    elif palace_route == "2":
        hike()
    elif palace_route == "3":
        city_drive()
    else:
        print "Sorry an asteroid just hit your palace."
        exit(0)

def cave():
    print "Your cold, clammy cave is safe from all predators."
    print "1. Will you find a friend to drive you on Interstate 5?"
    print "2. Or will you enjoy nature on a mountain hike?"
    print "3. Or will you go into the city?"

    cave_route = raw_input('>>> ')

    if cave_route == "1":
        I5()
    elif cave_route == "2":
        hike()
    elif cave_route == "3":
        city_drive()
    else:
        print "Your mother dresses you funny."
        exit(0)

#then each of the routes
def I5():
    print "You're driving down Interstate 5 and you who do you see?"
    Jesus()

def hike():
    print "Nature is beautiful on this warm, sunny day."
    print "Who do you see?"
    Jesus()

def city_drive():
    print "Traffic is horrible, but look over there! It's"
    Jesus()

# the final destination
def Jesus():
    print "Jesus. All roads lead to Jesus."
    exit(0)

# without start it doesn't start even though this is at the end.
start()


    #exit(0)
