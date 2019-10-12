# -*- encoding: utf-8 -*-
import numbers

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 获取原列表，可以理解为 copy 了一份
print(a[::])
# 把原列表翻转，可以理解为反序
print(a[::-1])


# 支持切片操作的 Group
class Group:
    def __init__(self, group_name, company_name, stuffs):
        self.group_name = group_name
        self.company_name = company_name
        self.stuffs = stuffs

    def __reversed__(self):
        pass

    def __getitem__(self, item):
        # 实现切片操作的关键
        G = type(self)
        if isinstance(item, slice):
            return G(group_name=self.group_name, company_name=self.company_name, stuffs=self.stuffs[item])
        elif isinstance(item, numbers.Integral):
            return G(group_name=self.group_name, company_name=self.company_name, stuffs=[self.stuffs[item]])

    def __len__(self):
        return len(self.stuffs)

    def __iter__(self):
        return iter(self.stuffs)

    def __contains__(self, item):
        if item in self.stuffs:
            return True
        else:
            return False


stuffs = ['mark', 'herry', 'tom']
group = Group(company_name='慕课网', group_name='user', stuffs=stuffs)
print(group[1::2])

print(len(group))
if 'mark' in group:
    print('yes')
