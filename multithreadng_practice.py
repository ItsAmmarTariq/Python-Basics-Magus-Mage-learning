import time
import threading
import concurrent.futures

def cal_square_and_cube(numbers):
    for i in numbers:
        print('Calculating square numbers')
        time.sleep(0.2)
        print('square', i*i)

        print('Calculating cube numbers')
        time.sleep(0.2)
        print('cube', i*i*i)

def threaded_functions():
    threads = []
    for i in range(2):
        t = threading.Thread(target=heavy, args=(500, i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def concurrent_futures_functions():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        seconds = [2, 7, 4, 6, 1]
        results = [executor.submit(do_something, sec) for sec in seconds]
        for f in concurrent.futures.as_completed(results):
            print(f.result())

def heavy(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    print(myid, "is done")

def do_something(sec):
    print(f'sleeping for {sec}.....')
    time.sleep(sec)
    return f'done with sleeping ....{sec}'

if __name__ == "__main__":
    arr = [2, 3, 5, 8]

    # Uncomment the functions you want to run

    # cal_square_and_cube(arr)
    # threaded_functions()
    concurrent_futures_functions()
    # ...

    print('I have completed my tasks')
