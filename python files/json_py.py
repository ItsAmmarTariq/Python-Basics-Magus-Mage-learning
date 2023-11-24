import json

jsonstring = '{"name": "erik", "age": 38, "married": true}'
person = json.loads(jsonstring)
print(person['name'], 'is', person['age'], 'years old')
print(type(person))
