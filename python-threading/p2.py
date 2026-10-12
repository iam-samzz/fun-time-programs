from threading import Thread
import time



def f1():
    for i in range(5):
        print(f"d1---- : {i}")

def f2():
    for i in range(5):
        print(f"d2 : {i}")

if __name__ == "__main__":
    t1 = Thread(target=f1)
    t2 = Thread(target=f2)

    t1.start()
    t2.start()

    
    t1.join()
    t2.join()

    print("hello!")
