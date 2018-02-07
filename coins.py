



user_input = input("Enter the total value: $")
value = int(float(user_input)*100)

coin_values = [50, 25, 10, 5, 2, 1]
coin_counts = [0]*len(coin_values)

coin_values.sort()
coin_values.reverse()

for i,coin_value in enumerate(coin_values):
    if value >= coin_value:
        coin_counts[i] = value // coin_value
        value -= coin_counts[i]*coin_value
    message = (str(coin_value)+' - '+str(coin_counts[i]))
    print(message)

print(coin_counts)
#
# n_quarters = 0
# n_dimes = 0
# n_nickles = 0
# n_pennies = 0
# while value != 0:
#     if value >= 25:
#         n_quarters = value // 25
#         value -= n_quarters*25
#     elif value >= 5:
#         n_nickles = value // 5
#         value -= n_nickles*5
#     elif value >= 10:
#         n_dimes = value // 10
#         value -= n_dimes*10
#     else:
#         n_pennies = value
#         value -= n_pennies
#
# print('Quarters: ', n_quarters)
# print('Dimes: ', n_dimes)
# print('Nickles: ', n_nickles)
# print('Pennies: ', n_pennies)
