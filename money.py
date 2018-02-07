user_input = input("Enter the total value: $")
value = int(float(user_input)*100)

half_dollar = {'name':'half-dollar', 'value':50, 'count':0}
quarter = {'name':'quarter', 'value':25, 'count':0}
dime = {'name':'dime', 'value':10, 'count':0}
nickel = {'name':'nickel', 'value':5, 'count':0}
penny = {'name':'penny', 'value':1, 'count':0}
coins = [half_dollar, quarter, dime, nickel, penny]

for i,coin in enumerate(coins):
    if value >= coin['value']:
        coin['count'] = value // coin['value']
        value -= coin['count']*coin['value']

    message = coin['name'] + ' - ' + str(coin['count'])
    print(message)
