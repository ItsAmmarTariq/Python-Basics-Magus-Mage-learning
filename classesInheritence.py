# class Car:
#     speed=0
#     started=False
#     def start(self):
#         self.started=True
#         print('The car has started')
    
#     def Speed(self,val):
#         if self.started:
#             self.speed=val
#             print('vroooooooooooooooommm!  ')
#             print('Speed is now ',val)
#         else:
#             print('You need to start the car \'First\' ')
    
#     def stop(self):
#         self.speed=0
#         print('Breaking......................!')
#         print('************Stoped*****************')
#         print('the speed is now ',self.speed)

# obj=Car()
# obj.start()
# obj.Speed(40)
# obj.stop()


class Vehicle:
    def __init__(self,speed=0,started=False):
        self.started=started
        self.speed=speed

    def start(self):
        self.started=True
        print('The car has started')
    
    def Speed(self,val):
        if self.started:
            self.speed=val
            print('vroooooooooooooooommm!  ')
            print('Speed is now ',val)
        else:
            print('You need to start the car \'First\' ')
    
    def stop(self):
        self.speed=0
        print('Breaking......................!')
        print('************Stoped*****************')
        print('the speed is now ',self.speed)


class Car(Vehicle):
    trunk_open=False
    def open_trunk(self):
        self.trunk_open=True
    def close_trunk(self):
        self.trunk_open=False


class Motorcycle(Vehicle):
    def __init__(self, centre_stand_out=False):
        self.centre_stand_out=centre_stand_out
        super().__init__()
    

        #override the super method 
    def start(self):
        # super().start()
        print('Sorry ran out of fuel !')


motorcycle=Motorcycle()
motorcycle.start()
print(motorcycle.started)