import math

#user_input = input('Please enter your credit card number: ')
user_input = '4556737586899855'

ccn = [] #credit card number
rccn = [] #reverse ccn
rccn3 = []
cd = 0 #check digit

for i in range (len(user_input)):
    ccn.append(int(user_input[i]))

print(ccn)

#del ccn[-1]
cd = str(ccn.pop(-1))

print(ccn)

rccn = ccn.copy()
rccn.reverse()

print(rccn)

rccn2 = rccn.copy()

for i in range(0,15,2):
    rccn2[i]*=2

print(rccn2)

rccn3 = rccn2.copy()

for i in range(0,15):
    if rccn3[i] >= 10:
        print(rccn3[i])
        rccn3[i] -= 9

print(rccn3)

runningtotal = 0

rccn4 = rccn3.copy()
for i in range(len(rccn4)):
     runningtotal += rccn4[i]

print(runningtotal)

str(runningtotal)
enddigit = str(runningtotal)[1]
print(type(enddigit), type(cd))
print(enddigit, cd)

if enddigit == cd:
    print('Woohoo')
else:
    print('Invalid number')
