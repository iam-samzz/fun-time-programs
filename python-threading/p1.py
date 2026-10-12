from threading import Thread
import time


class c1(Thread):
    def run(self):
        for i in range(5):
            print(f"d1---- : {i}")
class c2(Thread):
    def run(self):
        for i in range(5):
            print(f"d2 : {i}")

if __name__== "__main__":

    obj1 = c1()
    obj2 = c2()

    obj1.start()
    obj2.start()

    obj1.run()
    obj2.run()

    obj1.join()
    obj2.join()

    print("hello")