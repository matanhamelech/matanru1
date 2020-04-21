import threading
event=threading.Event()
x='djweiodw'
l=[]
winners=[]
def func(y, name):
    """
    append to a list the name when finishes
    :param y: a num given
    :param name: the name of the thread
    :return:
    """
    global l
    event.wait()
    x = y
    l.append(name)





def main():
    """
    creates and event that runs 10 threads of func in same time, then append to a list the thread who finished first.
    """
    global l
    global winners
    i=0
    list_of_threads=[]
    for num in range(10):
        list_of_threads.append(threading.Thread(target=func, args=[x, i]))
        i+=1
    for num in list_of_threads:
        num.start()
    event.set()
    while len(l)!=10:
        pass
    winners.append(l[0])
    l=[]

for num in range(5):
    event.clear()
    main()
print(winners)

