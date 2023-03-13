# This is a sample Python script.
import json
import operator
import sys
import threading
import time

import requests

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


paragraph = '''this is multi 
line'''
print(paragraph)
# this is multi
# line

# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
testStr = '123456789'
print(testStr)
print(testStr[0:-1])
# 12345678
print(testStr[0])
# 1
print(testStr[0:])
# 123456789
print('testStr[:2] = ', testStr[:2])
# testStr[:2] =  12
print(testStr[2:5])
# 345   包含2，不包含5
print(testStr[1:5:2])
# 24   包含2，不包含5
print(testStr * 2)
# 123456789123456789
print('hello\nworld')
# hello
# world
print(r'hello\nworld')
# hello\nworld

input('\n\n 按下enter键退出')

x = "hello"
sys.stdout.write(x + '\n')
# hello

test = input()
if test == 'true':
    print("this is true")
elif test == 'false':
    print("this is false")
else:
    print("this is other")
# 输入hello，则输出this is other

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

# ================Python import mode==========================
# 命令行参数为:
# /Users/geely/PycharmProjects/pythonProject/main.py
#
# python 路径为 ['/Users/geely/PycharmProjects/pythonProject', '/Users/geely/PycharmProjects/pythonProject',
# '/Library/Frameworks/Python.framework/Versions/3.10/lib/python310.zip',
# '/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10',
# '/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload',
# '/Users/geely/PycharmProjects/pythonProject/venv/lib/python3.10/site-packages']

a, b, c, d = 2, 2.0, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
# <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
a = 2
print(isinstance(a, bool))
# False

# isinstance 和 type 的区别在于：
#
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
# >>> class A:
# ...     pass
# ...
# >>> class B(A):
# ...     pass
# ...
# >>> isinstance(A(), A)
# True
# >>> type(A()) == A
# True
# >>> isinstance(B(), A)
# True
# >>> type(B()) == A
# False

# Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
issubclass(bool, int)
print('True == 1 is ', True == 1)
# True == 1 is  True
print('False == 0 is ', False == 0)
# False == 0 is  True
print('True + 1 is ', True + 1)
# True + 1 is  2
print('False + 1 is ', False + 1)
# False + 1 is  1

print('2 / 5 = ', 2 / 5)
# 2 / 5 =  0.4
print('2 // 5 = ', 2 // 5)
# 2 // 5 =  0
print('2 ** 5 = ', 2 ** 5)
# 2 ** 5 =  32

# 列表 （有序） 字典 （无序）
testList = ['abcd', 786, 2.23, 'hello', 70.2]
del testList[0]
# [786, 2.23, 'hello', 70.2]
print(testList)
print('testList[2:]', testList[2:])
# [2.23, 'hello', 70.2]
testList[1: 3] = []
print('testList[1: 3] = []', testList)


# 定义函数， input是参数
def reverseWords(input):
    inputWords = input.split(' ')
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]
    print(inputWords)
    # ['hello', 'like', 'I']
    output = ' '.join(inputWords)
    return output


if __name__ == '__main__':
    params = 'I like hello'
    rw = reverseWords(params)
    print(rw)
    # hello like I

# Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开


# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu', 'Google'}
print("sites:", sites)  # 自动去重

if 'geely' in sites:
    print('geely 在 sites集合中')
else:
    print('geely 不在 sites集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
# print(a[0:2])
# Traceback (most recent call last):
#   File "/Users/geely/PycharmProjects/pythonProject/main.py", line 155, in <module>
#     print(a[0:2])
# TypeError: 'set' object is not subscriptable
print(a - b)  # a 和 b 的差集
# {'b', 'd', 'r'}
print(a | b)  # a 和 b 的并集
# {'b', 'r', 'd', 'z', 'm', 'a', 'c', 'l'}
print(a & b)  # a 和 b 的交集
# {'a', 'c'}
print(a ^ b)  # a 和 b 中不同时存在的元素
# {'b', 'r', 'd', 'z', 'l', 'm'}


# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
dictTest = {}
print(dictTest)
# {}
dictTest['one'] = '1 - 菜鸟教程'
dictTest[2] = '2 - 菜鸟工具'
print(dictTest['one'])  # 输出键为 'one' 的值
print(dictTest[2])  # 输出键为 2 的值
print(dictTest.keys())
# dict_keys(['one', 2])
print(dictTest.values())
# dict_values(['1 - 菜鸟教程', '2 - 菜鸟工具'])

# 构造函数 dict() 可以直接从键值对序列中构建字典
dictTest = dict([('Google', 1), ('FaceBook', 2)])
print(dictTest)
# {'Google': 1, 'FaceBook': 2}

# {x: x**2 for x in (2, 4, 6)} 该代码使用的是字典推导式
dictTest = {x: x ** 2 for x in (2, 4, 6)}
print(dictTest)
# {2: 4, 4: 16, 6: 36}


# 列表推导式格式为：
#
# [表达式 for 变量 in 列表]
# [out_exp_res for out_exp in input_list]
#
# 或者
#
# [表达式 for 变量 in 列表 if 条件]
# [out_exp_res for out_exp in input_list if condition]
# out_exp_res：列表生成元素表达式，可以是有返回值的函数。
# for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
# if condition：条件语句，可以过滤列表中不符合条件的值。

names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
# 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：
names = [item.upper() for item in names if len(item) > 3]
print(names)
# ['ALICE', 'JERRY', 'WENDY', 'SMITH']

# 字典推导式
# 字典推导基本格式：
#
# { key_expr: value_expr for value in collection }
#
# 或
#
# { key_expr: value_expr for value in collection if condition }
listdemo = ['Google', 'Runoob', 'Taobao']
dictTest = {item: len(item) for item in listdemo}
print(dictTest)
# {'Google': 6, 'Runoob': 6, 'Taobao': 6}

# 集合推导式基本格式：
#
# { expression for item in Sequence }
# 或
# { expression for item in Sequence if conditional }

sets = {item * 2 for item in (1, 2, 3)}
print(sets)
# {2, 4, 6}


# 元组推导式可以利用 range 区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组。
#
# 元组推导式基本格式：
#
# (expression for item in Sequence )
# 或
# (expression for item in Sequence if conditional )

# 元组推导式返回的结果是一个生成器对象

tupleTest = (item * 2 for item in range(1, 10) if item % 2 == 0)
print(tupleTest)
# <generator object <genexpr> at 0x104efa1f0>
print(tuple(tupleTest))
# (4, 8, 12, 16)


errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print(errHTML)

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)

sql = '''SELECT * FROM TEST_TABLE a 
WHERE a.AGE > 20 
OR a.HEIGHT > 172'''
print(sql)

# f-string 格式化字符串以 f 开头，后面跟着字符串
name = 'Runoob'
name = f'Hello {name}'
print(name)
# Hello Runoob
w = {'name': 'Runoob', 'url': 'www.runoob.com'}
result = f"{w['name']} : {w['url']}"
print(result)

# 嵌套列表
a = ['a', 'b', 'c']
b = [1, 2, 3]
c = ['a', 'b', 'c']
x = [a, b]
print('[a, b] = ', x)
# [a, b] =  [['a', 'b', 'c'], [1, 2, 3]]
print(x[0])
# ['a', 'b', 'c']
print(x[0][1])
# b
print('operator.eq(a, b)', operator.eq(a, b))
print('operator.eq(a, c)', operator.eq(a, c))

testSet = set('google')
print(testSet)
# {'o', 'l', 'e', 'g'}
testSet = {'google', 'facebook'}
testSet.update(testSet, '1', '3')
print(testSet)
# {'google', '1', 'facebook', '3'}
testSet.update(testSet, [1, 3], [2, 5])
print(testSet)
# {'google', 1, 'facebook', 3, 2, 5, '1', '3'}

# testSet.update(testSet, 100, 300)
# Traceback (most recent call last):
#   File "/Users/geely/PycharmProjects/pythonProject/main.py", line 314, in <module>
#     testSet.update(testSet, 100, 300)
# TypeError: 'int' object is not iterable

# 迭代器和生成器
listTest = [1, 2, 3, 4]
it = iter(listTest)
print(next(it))
print(next(it))
for item in it:
    print(item)


# 3, 4
# it2 = iter(listTest)
# while True:
#     try:
#         print(next(it2))
#     except StopIteration:
#         sys.exit()


# 打印输出列表 x 的相关信息
def print_list(item):
    print('length of list is %d' % len(item))
    index = 0
    while index < len(item):
        # 修改此行
        print('list[%d] = %d' % (index, item[index]))
        index += 1


a = [1, 2, 3]
b = [10, 20, 30]

print_list(a)
# length of list is 3
# list[0] = 1
# list[1] = 2
# list[2] = 3
print_list(b)


# length of list is 3
# list[0] = 10
# list[1] = 20
# list[2] = 30


def change(param):
    param.append([1, 2, 3, 4])
    print('函数内取值：', param)
    # 函数内取值： [10, 20, 30, [1, 2, 3, 4]]
    return param


testList = [10, 20, 30]
print('函数外取值', change(testList))


# 函数外取值 [10, 20, 30, [1, 2, 3, 4]]

# 不定长参数
def printinfo(args, *params):
    print(args)
    print('-------*params----------')
    print(params)
    # 50
    # ------- * params - ---------
    # (60, 70)
    return


printinfo(50, 60, 70)


def printtwostar(args, **params):
    print(args)
    print('-------**params----------')
    print(params)
    # 50
    # ------- ** params - ---------
    # {'a': 60, 'b': 70}
    return


printtwostar(50, a=60, b=70)

# 匿名函数 lambda 函数的语法只包含一个语句
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))
# 相加后的值为 :  30
# 相加后的值为 :  40
vec = [1, 2, 3]
result = [[x, x ** 2] for x in vec]
print(result)
# [[1, 1], [2, 4], [3, 9]]


generatedict = dict([('google', 1), ('facebook', 2), ('tesla', 3)])
print(generatedict)
# {'google': 1, 'facebook': 2, 'tesla': 3}

# 使用关键字参数创建字典
keyDict = dict(google=1, facebook=2, tesla=3)
print(keyDict)
# {'google': 1, 'facebook': 2, 'tesla': 3}
for key, value in keyDict.items():
    print(key, value)
    # google 1
    # facebook 2
    # tesla 3

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i, v in enumerate(['a', 'b', 100]):
    print(i, v)
    # 0 a
    # 1 b
    # 2 100

# 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==>  {1:10}'.format(name, number))

# 如果你有一个很长的格式化字符串,最简单的就是传入一个字典, 然后使用方括号 [] 来访问键值
print('Runoob: {0[Runoob]}; Google: {0[Google]}; Taobao: {0[Taobao]}'.format(table))


# try:
#     f = open('test.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print('os error: {0}'.format(err))
# # except ValueError as formaterror:
# #     print("error = {0}".format(formaterror))
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise
# raise 语句有如下三种常用的用法：
# raise：单独一个 raise。该语句引发当前上下文中捕获的异常（比如在 except 块中），或默认引发 RuntimeError 异常。
# raise 异常类名称：raise 后带一个异常类名称，表示引发执行类型的异常。
# raise 异常类名称(描述信息)：在引发指定类型的异常的同时，附带异常的描述信息。

# try:
#     a = input("请输入一个数")
#     if not a.isdigit():
#         raise ValueError('a 必须是数字')
# except ValueError as err:
#     print("输入数异常：", err)
#     # 输入数异常： a 必须是数字
#     print("输入数异常：", repr(err))
#     # 输入数异常： ValueError('a 必须是数字')

# for arg in sys.argv[0:]:
#     try:
#         f = open(arg, 'r')
#     except IOError as err:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()

# 用户自定义异常
class MyError(Exception):
    def __init__(self, message, base_message=None, *args):
        self.base_message = base_message
        self.message = message

    def __str__(self):
        if self.base_message is None:
            return self.message

        return self.message + " '" + str(self.base_message) + "'"


try:
    raise MyError(2 * 2)
except MyError as err:
    print('My exception occurred, value:', err.message)


# 预定义的清理行为
# 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法
# with open("myfile.txt") as f:
#     for line in f:
#         print(line)
# 以上这段代码执行完毕后，就算在处理过程中出问题了，文件f总是会关闭


class MyClass:
    """一个简单的类实例"""
    i = 12345

    def testf(self):
        return 'hello world'


x = MyClass()
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.testf())


class Complex:
    def __init__(self, height, age):
        self.h = height
        self.a = age


x = Complex(3.0, -4.5)
print(x.h, x.a)


# ---------------------------------实例

def exe_code():
    LOC = '''
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact
print(factorial(5))
'''
    exec(LOC)


exe_code()


def calStrLen(param):
    count = 0
    while param[count:]:
        count += 1
    return count


param = 'www'
print("www len:", calStrLen(param))


def check(string, sub_str):
    if string.find(sub_str) == -1:
        print('not exit')
    else:
        print('exit')


check('www.google.com', 'www')


def removeAt(string, index):
    first = string[0:index]
    second = string[index + 1:]
    res = first + second
    return res


print(removeAt('wwwabc', 3))


def removeStringAt(string, index):
    newstr = ''
    for i in range(0, len(string)):
        if i != index:
            newstr += string[i]
    return newstr


print(removeStringAt('abcdefghijk', 2))

itemList = ['aaa', 111, 'ccc', {'a': 'aaa', 'b': 'bbb'}]


def isExit(listi, item):
    for it in listi:
        if it == item:
            print('item exit')
            break
        else:
            print('item not exit')


isExit(itemList, 111)


def findMin(list):
    minValue = list[0]
    for item in list:
        if item < minValue:
            minValue = item
        else:
            continue
    return minValue


print(findMin([2, 5, 1, 3, 0]))


def reverse(str):
    rstr = ""
    # for index in (range(len(str), 0)):
    #     rstr = rstr.join(str[index])
    # print(rstr)
    rstr = str[::-1]
    return rstr


print(reverse('123abc'))

print('123adbc'[1:6:2])

# 合并字典
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4, 'a': 11}
print(dict2.update(dict1))
print(dict2)
res = {**dict1, **dict2}
print(res)

data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com',
    'aar': [1, 2, 3]
}

json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print("data2['name']: ", data2['name'])
print("data2['aar']: ", data2['aar'])

with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    json_dict = json.load(f)
    print(json_dict['aar'])

BASE_URL = 'http://cloud.dev.phugiasystem.com/'

headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic c2FiZXI6c2FiZXJfc2VjcmV0'}
data = 'password=f52c91dbbe50fa9d1fa06c5b302af6e9&grant_type=password&scope=all&username=admin-HUKU2&'
# data = {
#     'password': 'f52c91dbbe50fa9d1fa06c5b302af6e9',
#     'grant_type': 'password',
#     'scope': 'all',
#     'username': 'admin-HUKU2'
# }
response = requests.post(BASE_URL + 'api/blade-auth/oauth/token', data=data, json=None, headers=headers)
print(response.json())


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print('%s: %s' % (threadName, time.ctime(time.time())))


# try:
#     _thread.start_new_thread(print_time, ('Thread-Name-1', 2))
#     _thread.start_new_thread(print_time, ('Thread-Name-2', 4))
# except:
#     print('error:无法启动线程')
#
# while 1:
#     pass


# pass 空操作，相当于java中的if(true){}


class MyThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        # super().__init__()
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        threadLock.acquire()
        print('start thread:', self.name)
        print_thread_time(self.name, self.delay, 5)
        print('end thread:', self.name)
        threadLock.release()


exitFlag = 0


def print_thread_time(name, delay, counter):
    while counter:
        if exitFlag:
            name.exit()
        time.sleep(delay)
        print('%s: %s' % (name, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
thread1 = MyThread(1, 'Thread1', 1)
thread2 = MyThread(2, 'Thread2', 2)
thread1.start()
thread2.start()


# office.tools.weather()