likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

for key in likes:
    print(key)

for key in likes:
    print(f'{key} -->{likes[key]}')


# print(likes.items)

for item in likes.items():
    print(item)


for key,val in likes.items():
    print(key,"-->",val)

print(likes.keys())


for key in likes.keys():
    print(key)

##ok oko ok

fruits={
    'apples':12.5,
    'orang':13,
    'pineapple':18,
    'melon':21

}
# ietrating and changing the values of dict
for fruit,price in fruits.items():
    fruits[fruit]=price*2

print(fruits)

for fruit in fruits.copy():
    if fruits[fruit]>=26:
        del fruits[fruit]

print(fruit)

def remdict(dict,keys):
    for kye in keys:
        if kye in dict:
            del dict[kye]
    return dict

a={'a':1,'b':2,'c':3,'d':4}
keys_rm=['c','d']

print(remdict(a,keys_rm))


