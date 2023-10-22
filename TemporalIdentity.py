import random
import math
import threading
import sys
import time
import signal


print("press ctrl+c to print another license.")
def num():
    times = time.time()
    llama = 0
    for b in sys.argv[1]:
        llama += ord(b)
    this = [((random.randint(0, 10) * int(times)) * int(llama) % 10), ((random.randint(0, 10) * int(times)) * int(llama) % 10)]
    that = lambda thing: int(math.sqrt(thing ** thing) - thing + ((thing * thing) / (thing + int(llama))) - int(llama)) and thing ^ llama
    illegalbin.append(map(that, this))
    return that

def identity():
    t1 = threading.Thread(target=num)
    t2 = threading.Thread(target=num)
    t3 = threading.Thread(target=num)
    t4 = threading.Thread(target=num)
    t5 = threading.Thread(target=num)
    t6 = threading.Thread(target=num)
    t7 = threading.Thread(target=num)
    t8 = threading.Thread(target=num)
    t9 = threading.Thread(target=num)
    t10 = threading.Thread(target=num)
    t11 = threading.Thread(target=num)
    t12 = threading.Thread(target=num)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    print(map(num(), illegalbin), end="\r")
if __name__ == "__main__":
    while True:
        illegalbin = []
        identity()
        def signals(signal, frame):
            print(map(num(), illegalbin))
            return(map(num(), illegalbin))
        signal.signal(signal.SIGINT, signals)