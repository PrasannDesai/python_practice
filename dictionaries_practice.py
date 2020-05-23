new_dict = {'name': 'Prasann', 'age': 25}

welcome_string = 'Hey {name}! I know you are {age} years old!'.format(**new_dict)

print(new_dict)
print(new_dict['name'])
print(new_dict['age'])
# print(new_dict['phone'])         # Throws an error if key doesn't exist


print(new_dict.get('name'))
print(new_dict.get('age'))
print(new_dict.get('phone'))     # Does not throw an error if key doesn't exist
print(new_dict.get('phone', 'Not Found'))     # Does not throw an error if key doesn't exist

new_dict['phone'] = '9892922354'
print(new_dict.get('phone', 'Not Found'))     # Does not throw an error if key doesn't exist
print(welcome_string)

new_dict.update({'address': 'Kanjurmarg', 'city': 'Mumbai', 'age': 30})
print(new_dict)

del new_dict['city']
print(new_dict)

age_popped = new_dict.pop('age')
print(new_dict)
print(age_popped)


print(len(new_dict))
print(new_dict.keys())
print(new_dict.values())
print(new_dict.items())


for key, value in new_dict.items():
    print(key + ' = ' + value)

for key, value in enumerate(new_dict, 1):
    print(key, value)
