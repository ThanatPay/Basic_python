# dictionaries
# store data on key:value format
Dict = {"Alisson": "Becker",
        "Ibrahima": "Konate",
        "Jordan": "Henderson",
        "Mohamed": "Salah"}
print(Dict)
print(type(Dict))
# you can get value from dict[key]
print(Dict['Alisson'])

# update dict
# The key may or may not exist in the dict
Dict['Roberto']='Firmino'
print(Dict)
# using update function
Dict.update({"Roberto": "carlos",
             "Sadio": "Mane"})
print(Dict)
# using del
del Dict['Roberto']
print(Dict)

# not everything can be used as a key
# Lists cannot be used as keys, but tuples, numbers, and strings can
# Dict[['Steven']]='Gerrard'

# if you use get value from key method and return error
# if key doesn't exist in dict
# print(Dict['alison'])
# using get function
print(Dict.get('Alisson'))
print(Dict.get('alisson'))
print(Dict.get('alisson',1))

# remove key but return function
# using pop function
print(Dict.pop('Sadio'))
print(Dict)

# get key/value/item in dict
print(Dict.keys())
print(Dict.values())
print(Dict.items())

# Iteraring through Dicrionary
for key in Dict:
    print(key)