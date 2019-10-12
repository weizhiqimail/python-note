# -*- encoding: utf-8 -*-

# f = open('./lyric.txt', encoding='utf-8', mode='r')

# data = f.readlines()
# for index, line in enumerate(data):
#     print(index + 1, line.strip())


# for line in f:
#     print(line)

import os

abs_path = os.path.abspath(__file__)

print(abs_path)

file_dirname = os.path.dirname(abs_path)

print(file_dirname)

file_dirname = os.path.dirname(file_dirname)

print(file_dirname)

file_dirname = os.path.dirname(file_dirname)

print(file_dirname)

print(os.path.join(file_dirname, 'templates'))

