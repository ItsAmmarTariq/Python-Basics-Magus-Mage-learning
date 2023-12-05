from abc import ABC,abstractmethod

class Father(ABC):
    @abstractmethod
    def disp1(self):
        pass
    
    @abstractmethod
    def disp2(self):
        pass

    


class Child(Father):
    def disp1(self):
        print('child class')
        print('defining the ABstarct method')

        # we cant instantiate it becoz it is also a abstaract calss
    
    
class GrandChild(Child):
    def disp2(self):
        print('this is disp2')
    
     
    

gc=GrandChild()
gc.disp2()

