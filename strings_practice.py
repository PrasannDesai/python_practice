
message = 'Hello World'

print(message)
print(len(message))
print(message[0])
print(message[0:5])
print(message[:8])
print(message[7:8])
print(message[7:])
print(message.lower())
print(message.upper())
print(message.count('Hello'))
print(message.count('l'))
print(message.find('World'))

modified_message = message.replace("World", "Universe")
print(modified_message)
print(message)

msg1 = 'Hello'
greeting = 'Prasann'

welcome_msg = msg1 + ', ' + greeting

better_welcome_msg = '{}, {}. Welcome!'.format(msg1, greeting)

# f-string function. Newly added for python 3.6
even_better_welcome_msg = f'{msg1}, {greeting}. Welcome!'


print(welcome_msg)
print(better_welcome_msg)
print(even_better_welcome_msg)

# print(dir(welcome_msg))
# print(help(str.title))

person = {'name': 'Prasann', 'age': 25}

myList = ['Prasann', 25]
sentence = 'My name is {0[0]} and I am {0[1]} years old'.format(myList)
print(sentence)

another_sentence = 'My name is {name} and I am {age} years old'.format(**person)
print(another_sentence)

for i in range(1, 11):
    temp = 'My value is {:02}'.format(i)
    print(temp)
