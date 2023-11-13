class Car:
    speed=0
    started=False
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

obj=Car()
obj.start()
obj.Speed(40)
obj.stop()




