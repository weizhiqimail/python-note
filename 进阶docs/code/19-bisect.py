# -*- encoding: utf-8 -*-

import bisect

inter_list = []

bisect.insort(inter_list, 2)
bisect.insort(inter_list, 4)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 0)
bisect.insort(inter_list, -2)
bisect.insort(inter_list, -5)

print(inter_list)
