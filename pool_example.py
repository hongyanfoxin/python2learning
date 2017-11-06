# -*- coding: utf-8 -*-

import multiprocessing
import time
import random
import sys
import os


def mul(a, b):
    # 若没有该睡眠，则第一个进程瞬间就把所有任务搞完了。。。
    time.sleep(0.5*random.random())
    # time.sleep(0.5)
    return a*b


def plus(a, b):
    # 若没有该睡眠，则第一个进程瞬间就把所有任务搞完了。。。
    time.sleep(0.5*random.random())
    # time.sleep(0.5)
    return a + b


def calculate(func, args):
    result = func(*args)
    # print(
    #         '%s says that %s%s = %s' % (
    #                 multiprocessing.current_process().name,
    #                 func.__name__, args, result
    #                 )
    #     )
    return '%s : %s says that %s%s = %s' % (
        multiprocessing.current_process().name, os.getpid(),
        func.__name__, args, result
        )


def test():
    processes = 4
    pool = multiprocessing.Pool(processes, maxtasksperchild=2)
    for worker in pool._pool:
        print(worker.is_alive())

    print(dir(pool))
    print(pool._taskqueue.qsize())

    TASKS = [(mul, (i, 7)) for i in range(10)] + \
            [(plus, (i, 8)) for i in range(10)]
    # TASKS = [(mul, (i, 7)) for i in range(3)]

    # print(TASKS)
    # print(len(TASKS))

    results = [pool.apply_async(calculate, t) for t in TASKS]
    print(pool._taskqueue.qsize())
    # Prevents any more tasks from being submitted to the pool.
    # Once all the tasks have been completed the worker processes will exit.
    pool.close()
    # Wait for the worker processes to exit. One must call close() or terminate() before using join().
    pool.join()
    print(pool._taskqueue.qsize())
    print(results)
    for r in results:
        print(r.get())

    print(pool._taskqueue.qsize())


if __name__ == '__main__':
    test()
