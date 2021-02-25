import os
import sys
sys.path.insert(0, r'..\pyshredder')
from pyshredder.util.shredder import shredder
from ztools import fbasic

f = fbasic()

old_path = '.\\ts_file\\eraser_testfile.txt'
f.ensure('.\\ts_file\\shredder')

new_path = '.\\ts_file\\shredder\\shredder_testfile1.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
print(shredder.file(new_path, mode='fast', check=True, delete=False))
print("after file size:", os.path.getsize(new_path))
print(shredder.file(new_path, mode='fast', check=False, delete=True))

new_path = '.\\ts_file\\shredder\\shredder_testfile2.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
print(shredder.file(new_path, mode='standard', check=True, delete=False))
print("after file size:", os.path.getsize(new_path))
print(shredder.file(new_path, mode='standard', check=False, delete=True))

new_path = '.\\ts_file\\shredder\\shredder_testfile3.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
print(shredder.file(new_path, mode='safe', check=True, delete=False))
print("after file size:", os.path.getsize(new_path))
print(shredder.file(new_path, mode='safe', check=False, delete=True))

new_path = '.\\ts_file\\shredder\\shredder_testfile4.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
print(shredder.file(new_path, mode='destroy', check=True, delete=False))
print("after file size:", os.path.getsize(new_path))
print(shredder.file(new_path, mode='destroy', check=False, delete=True))

new_path = '.\\ts_file\\shredder\\shredder_testfile5.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
print(shredder.file(new_path, mode='unkown', check=True, delete=False))
print("after file size:", os.path.getsize(new_path))
print(shredder.file(new_path, mode='unkown', check=False, delete=True))

input("按回车（Enter）继续")
