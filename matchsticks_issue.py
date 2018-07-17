#! /usr/bin/python
#! -*-coding:utf-8 -*-

'''match issue 火柴问题
总共23根火柴，人和计算机只能拿其中的1 2 3 根，谁拿到最后一根谁就输。

__author__=='savior'

V0.1

'''

import random

def human_take():
    human_input=int(input("human takes:(allow input 1 or 2 or 3)"))
    print("human takes:%d" % human_input)
    return human_input

def computer_take():
    computer_input=int(input('computer takes:(allow input 1 or 2 or 3)'))
    print("computer takes:%d" %computer_input)
    return computer_input



take_first=input('who takes first:(human/computer)')

def huocai_issue(n):
    flag=True
    hu_n = 0
    comp_n = 0
    while flag:
        # co_take=computer_take()
        if take_first=='human':
            if hu_n==comp_n and n>3:
                hu_take=human_take()
                if hu_take>3:
                    print('error:only can take 1 or 2 or 3,quit now.')
                    break
                print("left:%d" %(n-hu_take))
                hu_n+=1
                n-=hu_take
            elif hu_n>comp_n and n>3:
                comp_take = computer_take()
                if comp_take>3:
                    print('error:only can take 1 or 2 or 3,quit now.')
                    break
                print("left:%d" % (n - comp_take))
                comp_n += 1
                n -= comp_take
            elif (n==3 or n==2)and hu_n==comp_n:
                print("human win")
                break
            elif (n==3 or n==2) and hu_n>=comp_n:
                print("computer win")
                break
            elif n==1 and hu_n==comp_n:
                print("human lose")
                break
            elif n==1 and hu_n>=comp_n:
                print("computer lose")
                break
            else:
                flag=False
        else:
            if hu_n==comp_n and n>3:
                comp_take=computer_take()
                if comp_take>3:
                    print('error:only can take 1 or 2 or 3,quit now.')
                    break
                print("left:%d" %(n-comp_take))
                comp_n+=1
                n-=comp_take
            elif hu_n<comp_n and n>3:
                hu_take = human_take()
                if hu_take>3:
                    print('error:only can take 1 or 2 or 3,quit now.')
                    break
                print("left:%d" % (n - hu_take))
                hu_n += 1
                n -= hu_take
            elif (n==3 or n==2)and hu_n==comp_n:
                print("computer win")
                break
            elif (n==3 or n==2) and hu_n>=comp_n:
                print("human win")
                break
            elif n==1 and hu_n==comp_n:
                print("computer lose")
                break
            elif n==1 and hu_n>=comp_n:
                print("human lose")
                break
            else:
                flag=False

if __name__=='__main__':
    n=huocai_issue(23)