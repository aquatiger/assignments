# there are 100 cars
cars = 100
# there are 4 spaces in each car
space_in_a_car = 4
#there are 30 drivers
drivers = 30
#there are 90 passengers
passengers = 90
"""there are 100 cars but only 30 drivers so the leftovers are cars not driven"""
cars_not_driven = cars - drivers
#since there are less drivers than cars the number of cars driven will equal the number of drivers
cars_driven = drivers
#carpool capacity equals the number of cars plus the extra space
carpool_capacity = cars_driven * space_in_a_car
#averages are averages
average_passengers_per_car = passengers / cars_driven


#this tells the number of cars available
print "There are", cars, "cars available."
#this tells the number of drivers available
print "There are only", drivers, "drivers available."
#this tells the number of cars not driven because there is an excess of cars
print "There will be", cars_not_driven, "empty cars today."
#so this results in the number of possible spaces
print "We can transport", carpool_capacity, "people today."
#this is the number of passengers to carpool totoal
print "We have", passengers, "to carpool today."
#this tells the amount per each car
print "We need to put about", average_passengers_per_car, "in each car."
