import requests


r = requests.get('http://api.randomuser.me/?results=5')
data = r.json()

for person in data['results']:
    info = f"""
    Name: {person['name']}
    Email: {person['email']}
    Username: {person['login']['username']}
    Registration date:  {person['registered']}
    Birth date: {person['dob']}
    """
    print(info)
