import os
from ztools import fbasic
from pyshredder import shredder

f = fbasic()

old_path = '.\\ex_file\\eraser_testfile.txt'
f.ensure('.\\ex_file\\shredder')

new_path = '.\\ex_file\\shredder\\shredder_testfile1.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
s = shredder('fast')
print(s.file(new_path, check = True, delete = False))
print("after file size:", os.path.getsize(new_path))
print(s.file(new_path, check = False, delete = True))

new_path = '.\\ex_file\\shredder\\shredder_testfile2.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
s = shredder('standard')
print(s.file(new_path, check = True, delete = False))
print("after file size:", os.path.getsize(new_path))
print(s.file(new_path, check = False, delete = True))

new_path = '.\\ex_file\\shredder\\shredder_testfile3.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
s = shredder('safe')
print(s.file(new_path, check = True, delete = False))
print("after file size:", os.path.getsize(new_path))
print(s.file(new_path, check = False, delete = True))

new_path = '.\\ex_file\\shredder\\shredder_testfile4.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
s = shredder('destroy')
print(s.file(new_path, check = True, delete = False))
print("after file size:", os.path.getsize(new_path))
print(s.file(new_path, check = False, delete = True))

input("按回车（Enter）继续")
