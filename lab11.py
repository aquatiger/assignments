

def load_users(file_name):
	users = []
	with open(file_name, 'r') as f:
		header = f.readline().strip().split(',')
		for user_str in f: # loop through every line in the text file
			user_attributes = user_str.strip().split(',')
			user = {} # begin with an empty dictionary
			for i in range(len(header)):
				header_text = header[i]
				user_attribute = user_attributes[i]
				user[header_text] = user_attribute # set the attribute on the user
			users.append(user) # add the user to the list of users
	return users

def find_user(user_name, users):
	for user in users:
		if user_name == user['name']:
			return user
	return None




users = load_users('peeps2.csv')

#    a = keys
#    b = value

#function to print all attributes
def paa(user_attribute_name, users):
    for user in users:
        user_name = user['name']
        user_attribute_value = user[user_attribute_name]
        print(user_name + '\'s ' + user_attribute_name + ' is '+ user_attribute_value)

print(list(users[0].keys()))
zebra = input('which attribute would you like to see? ')

paa(zebra, users)
