import json

# check methods
# print(dir(json))

# convert json file to python dictionary
a = '{"first_name": "Rodgers", "last_name": "Nyangweso"}'

b = json.loads(a)
print(b["first_name"], b["last_name"])

# convert python object to json using json.dumps()
c = {"first_name": "Rodgers", "last_name": "Nyangweso"}

d = json.dumps(c)
print(d)

# formatting json object
e = {"first_name": "Rodgers", 
     "last_name": "Nyangweso"}

# JSON OBject with identation and specified seperators
f = json.dumps(e, indent=4, separators=(".", "="))
print(f)

# ordering the keys
g = {"first_name": "Rodgers", "last_name": "Nyangweso"}

# sorting keys using sort_keys
h = json.dumps(g, indent=4, sort_keys=True)
print(h)