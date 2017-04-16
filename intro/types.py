import humansizes

# // Bools
print("expect class bool", type(True))

# // Methods
def myMethod():
    print("hello, world")

print("expect class function", type(myMethod))

# //Module
print("expect module", type(humansizes))

# // Dictionary
dictionary = {"color": "blue", "size": 9090}
print("expect dictionary", type(dictionary))

junkyDict = dict()
junkyDict = {'name': 'callan', 'age': 26, 'role': 'who knows'}
junkyDict['coolLevel'] = 100
print(junkyDict)


# // Atuple
atuple = ("blue", 9090)
print("expect tuple", type(atuple))

junk = tuple();
junk = ("Joe", "intstructor", "awesome")
junk = ("Joe", "intstructor", "awesome", "purple")
print(junk)

# // List
reindeer = ["dasher", "dancer", "prancer", "vixen", "olive"]
print("expect list", type(reindeer))

junkyList = list()
junkyList = ['carrots', 'celery', 'kale', 2, ['peas', 'corn']]
junkyList.insert(1, 'kidney beans')
junkyList.extend([True, 'tornado'])
junkyList.append('hurricane')
print(junkyList)

# // Set
boy_bands = { "nsync", "one direction", "boyz II men" }
print("expect set", type(boy_bands))
