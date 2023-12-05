import json


def main():
    jsonstring = '{"name": "erik", "age": 38, "married": true}'
    person = json.loads(jsonstring)
    print(person['name'], 'is', person['age'], 'years old')
    json_str = json.dumps(jsonstring, indent=2)
    # print(type(person))

    print(json_str)
    print(type(json_str))


def jsonfileFunx():
    with open('test.json') as json_file:
        data = json.load((json_file))
        print(data)


def write_in_json():
    data = {'name': 'test', 'age': 34}
    with open('test.json', 'a') as file:
        json.dump(data,file)


jsonfileFunx()
