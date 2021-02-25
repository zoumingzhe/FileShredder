import os
from ztools import fbasic
from pyshredder import shredder

f = fbasic()

old_path = '.\\ex_file\\eraser_testfile.txt'
f.ensure('.\\ex_file\\shredder')

new_path = '.\\ex_file\\shredder\\shredder_testfile1.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
print(shredder.file(new_path, mode='fast', check=True, delete=False))
print("after file size:", os.path.getsize(new_path))
print(shredder.file(new_path, mode='fast', check=False, delete=True))

new_path = '.\\ex_file\\shredder\\shredder_testfile2.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
print(shredder.file(new_path, mode='standard', check=True, delete=False))
print("after file size:", os.path.getsize(new_path))
print(shredder.file(new_path, mode='standard', check=False, delete=True))

new_path = '.\\ex_file\\shredder\\shredder_testfile3.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
print(shredder.file(new_path, mode='safe', check=True, delete=False))
print("after file size:", os.path.getsize(new_path))
print(shredder.file(new_path, mode='safe', check=False, delete=True))

new_path = '.\\ex_file\\shredder\\shredder_testfile4.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
print(shredder.file(new_path, mode='destroy', check=True, delete=False))
print("after file size:", os.path.getsize(new_path))
print(shredder.file(new_path, mode='destroy', check=False, delete=True))

input("按回车（Enter）继续")
