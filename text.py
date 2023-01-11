import threading

i = 0


def task1():
    global i
    while True:
        i+=1

def task2():
    global i
    while True:
        print(i)


# creating threads
t1 = threading.Thread(target=task1, name='t1')
t2 = threading.Thread(target=task2, name='t2') 



t1.start()
t2.start()