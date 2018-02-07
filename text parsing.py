#incomplete
import re
import string


print(string.punctuation)
s2 = 'Python is great, they\'re especially For parsing text!'
parse = re.sub('['+string.punctuation+']', '', s2)
#parse = re.sub('{}$'.format(string.punctuation), '', parse)
print(parse)
parse = parse.lower()

s3 = re.sub('[A-Z]', '$' , parse)
print(s3)
#s2 = s2.lower()
# print(type(s2))
# s2 = s2.replace(',', '')
# print(type(s2))
# s2 = s2.strip(string.punctuation)
# print(type(s2))
# s2 = s2.split(" ")
# print(s2)
