# Use this to take notes on the Edpuzzle video. Try each example rather than just watching it - you will get much more out of it!
#  Most things are commented out because they can't all coexist without a syntax error

user = {"name": "Kasey", "age": 15, "courses": ["History, CompSci"]}

for key, value in user.items():
    print(key, value)

#print(user.items())

#print(user.values())

#print(user.keys())

#print(len(user))

#age=user.pop("age")

# del user['age']

'''user.update({"name": "Bob", "age": 25, "phone": "888-8888"})
user['phone'] = '888-8888'
user['name']='Bob'''''

#print(user.get("age",'not found'))

#print(user)
#print(age)