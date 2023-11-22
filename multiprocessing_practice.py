import time
import multiprocessing



def cal_square(numbers,result,v,q):
    v.value=5.67
   
    for ind,n in enumerate(numbers):
        q.put(n*n)  
      
        
    
# def cal_cube(numbers):
#     for n in numbers:
#         time.sleep(5)
#         print('cube '+str(n*n*n))
        

if __name__=='__main__':
    numbers=[2,3,7,8,6]
    result=multiprocessing.Array('i',5)
    v=multiprocessing.Value('d',0.0)

    q=multiprocessing.Queue()
    p1=multiprocessing.Process(target=cal_square,args=(numbers,result,v,q))

    p1.start()
    

    p1.join()
    
    # print(result[:])
    # print(v.value)
    while q.empty() is False:
        print(q.get())
    print('Done !')
