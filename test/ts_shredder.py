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
s = shredder('fast')
s.eraser(new_path, check = True)
s.rename(new_path)
print("after file size:", os.path.getsize(new_path))

new_path = '.\\ts_file\\shredder\\shredder_testfile2.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
s = shredder('standard')
s.eraser(new_path, check = True)
s.rename(new_path)
print("after file size:", os.path.getsize(new_path))

new_path = '.\\ts_file\\shredder\\shredder_testfile3.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
s = shredder('safe')
s.eraser(new_path, check = True)
s.rename(new_path)
print("after file size:", os.path.getsize(new_path))

new_path = '.\\ts_file\\shredder\\shredder_testfile4.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
s = shredder('destroy')
s.eraser(new_path, check = True)
s.rename(new_path)
print("after file size:", os.path.getsize(new_path))

input("按回车（Enter）继续")
