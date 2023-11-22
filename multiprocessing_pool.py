import time
from multiprocessing import Pool




def f(n):
    sum=0
    for x in range(100):
        sum+=x*x
        return sum
    

if __name__=='__main__':

    
    
    t=time.time()
    p=Pool()
    result=p.map(f,range(10000000))
    p.close()
    p.join()
    
    
    print('time taken is :',time.time()-t)
    t2=time.time()
    result=[]
    for x in range(10000000):
        result.append(f(x))
    
    print('serial process took',time.time()-t2)

