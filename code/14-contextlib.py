# -*- encoding: utf-8 -*-

import contextlib


@contextlib.contextmanager
def open_file(file_name):
    print('file open')
    yield file_name
    print('file end')


with open_file('user.txt') as f:
    print(f)
    print('file processing')
