import os

path = os.getcwd()
print("path =  %s" % path)

os.chdir('/Users/geely/PycharmProjects/pythonProject/os')
print('chdir path = ', os.getcwd())
dir_list = os.walk(os.getcwd())
for dir_path, dir_name, fileName in dir_list:
    # print(dir_path)
    # print('------------')
    # print(dir_name)
    # print('------------')
    # print('filename %s' % fileName)
    for f_name in fileName:
        print(os.path.join(dir_path, f_name))


str = os.path.split('/Users/geely/PycharmProjects/pythonProject/os/os.py')
print(str)
str_text = os.path.splitext('os.py')
print(str_text)

abs_path = os.path.abspath('test1.py')
print(abs_path)
print('os.py is exists path = ', os.path.exists('os.py'))
print('test.py is exists path = ', os.path.exists('test.py'))
