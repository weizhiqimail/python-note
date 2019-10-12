# -*- encoding: utf-8 -*-

import getpass

password = 'hello, world'

print(getpass.getpass(password))

age = 18

# for i in range(3):
#     guess_age = int(input('please input your age...'))
#     if guess_age == age:
#         print('yes, you are right')
#         break
#     elif guess_age > age:
#         print('bigger')
#     else:
#         print('smaller')
# else:
#     print('get out, idiot')


count = 0
while count < 3:
    guess_age = int(input('please input your age...'))
    if guess_age == age:
        print('yes, you are right')
        break
    elif guess_age > age:
        print('bigger')
    else:
        print('smaller')
    count += 1
    if count == 3:
        flag = input('do you want go on Y/n')
        if flag != 'n':
            count = 0
else:
    print('get out, idiot')
