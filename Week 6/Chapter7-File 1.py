dict1 = {
    'name': 'Alice',
    'age': 25,
    'city': 'Helsinki',
    'surname': 'Jones'
}

mykey = input('Please give me a string: ')

if mykey in dict1:
    #print("Your string is a key in this dictionary.")
    print("true.")
else:
    #print("Your string is not a key in this dictionary.")
    print("false.")


