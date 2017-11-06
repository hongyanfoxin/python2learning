from multiprocessing import Lock, Pool
import random


def write_file(lock):
    with lock:
        with open('write_demo.txt', 'a') as wf:
            wf.write(str(random.random())+"\r")
            print("ashjfgdsgafhjdsgahjfg")


def main():
    lock = Lock()
    pool = Pool()
    for i in range(0, 10):
        pool.apply(write_file, (lock,))
        # pool.apply_async(write_file(lock))
    pool.close()

if __name__ == '__main__':
    main()
