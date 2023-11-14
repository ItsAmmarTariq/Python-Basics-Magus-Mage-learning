
'''1.  duck typing
if any thing walk like a duck, swim or behve like a duck then its duck '''


class Duck:
    def walk(self):
        print('Thapak Thapak Thapak Thapak')
    
class Horse:
    def walk(self):
        print('Tagr tage tagr tager')

class Cat:
    def talk(self):
        print('.................. sloe slow slow.........')
def function(obj):
    if hasattr(obj,'walk'):

     obj.walk()

d=Duck()
function(d)

h=Horse()
function(h)
c=Cat()
function(c)

