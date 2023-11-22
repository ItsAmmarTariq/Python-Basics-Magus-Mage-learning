import time
import multiprocessing

square_res=[]

def cal_square(numbers):
    global square_res
    for n in numbers:
        
        print('square '+str(n*n))
        print('with in a process : result' +str(square_res))
        square_res.append(n*n)
    
# def cal_cube(numbers):
#     for n in numbers:
#         time.sleep(5)
#         print('cube '+str(n*n*n))
        

if __name__=='__main__':
    arr=[2,3,7,8,6]
    p1=multiprocessing.Process(target=cal_square,args=(arr,))
    #p2=multiprocessing.Process(target=cal_cube,args=(arr,))

    p1.start()
    

    p1.join()
    
    print('result' +str(square_res))
    print('Done !')
