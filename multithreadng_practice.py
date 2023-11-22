import time
import threading

def cal_square(numbers):
        for i in numbers:
            print('Calculating square numbers')
            time.sleep(0.2)
            print('square',i*i)
            

def cal_cube(numbers):
        for i in numbers:
            print('Calculating cube numbers')
            time.sleep(0.2)
            print('cube',i*i*i)

arr=[2,3,5,8]





if __name__=="__main__":
    t=time.time()
    t1=threading.Thread(target=cal_square,args=(arr,))
    t2=threading.Thread(target=cal_cube,args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('done in ',time.time()-t)
    print(' i have completed my tasks')
        
        

