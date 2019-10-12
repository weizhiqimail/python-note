# -*- encoding: utf-8 -*-

import time


def logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        spend = end_time - start_time
        print('{name} 运行时间为 {spend} 秒'.format(name=func.__name__, spend=spend))

    return wrapper


@logger
def test1():
    time.sleep(2)
    print('test 01')


@logger
def test2():
    time.sleep(4)
    print('test 02')


test1()
test2()
