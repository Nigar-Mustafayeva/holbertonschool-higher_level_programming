#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    result = 0
    for i in my_list:
        if i not in uniq:
            uniq.append(i)
            result += i
    return result
