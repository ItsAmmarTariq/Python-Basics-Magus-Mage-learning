import time
import multiprocessing
import requests

def downloadimage(url,name):
    print(f'started download {name}')
    respopnse=requests.get(url)
    open(f'files/{name}.jpg','wb').write(respopnse.content)
    print(f'finished downloaded {name}')

    

   




def cal_square(numbers,result,v,q):
    v.value=5.67
   
    for ind,n in enumerate(numbers):
        q.put(n*n)  

def add_balance(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value=balance.value+1
        lock.release()

def withdraw_balance(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value=balance.value-1
        lock.release()



        
    
def cal_cube(numbers):
    for n in numbers:
        time.sleep(.0001)
        print('cube '+str(n*n*n))
        

if __name__=='__main__':
    url='https://source.unsplash.com/random'
    pros=[]
    for i in range(2):
        p=multiprocessing.Process(target=downloadimage,args=(url,i,))
        p.start()
        pros.append(p)
   
    numbers=[2,3,7,8,6]

    balancec_value=multiprocessing.Value('i',200)
    result=multiprocessing.Array('i',5)
    v=multiprocessing.Value('d',0.0)
    lock=multiprocessing.Lock()

    q=multiprocessing.Queue()
    p1=multiprocessing.Process(target=add_balance,args=(balancec_value,lock))
    p2=multiprocessing.Process(target=withdraw_balance,args=(balancec_value,lock))

    for i in pros:
        i.join()

 

    # print(balancec_value.value) 
    # print(result[:])
    # print(v.value)
    # while q.empty() is False:
    #     print(q.get())
    # print('Done !')
