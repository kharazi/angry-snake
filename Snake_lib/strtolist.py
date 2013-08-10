'''
Copyright 1390(2012(AD)) Vahid Kharazi <kharazi72@gmail.com>
Licensed for distribution under the GPL version 3
This is two function to posded data processing.
'''


def datatolist(string):
    str = string[1:-1]

    def fun1(str):
        result = []
        for i in range(len(str)):
            if str[i] == '[':
                t = str.find(']', i)
                result.append(str[i:t + 1])
        return result

    def fun2(l):
        result = []
        for i in l:
            for j in range(len(i)):
                if i[j] == '[':
                    t = i.find(',', j)
                    result.append(int(i[j + 1:t]))
                if i[j] == ',':
                    t = i.find(']', j)
                    result.append(int(i[j + 1:t]))

        return result

    def fun3(l):
        result = []
        for i in range(len(l)):
            if i % 2 == 0:
                result.append([l[i]])

        c = -1
        for i in range(1, len(l), 2):
            c += 1
            result[c].append(l[i])
        return result
    return fun3(fun2(fun1(str)))


def xoyyab(string):
    result = []
    r = string.split('&')
    for i in r:
        if i != '':
            result.append(int(i))
    return result
