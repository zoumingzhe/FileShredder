import os
import sys
sys.path.insert(0, r'..\pyshredder')
from pyshredder.core.eraser import eraser
from ztools import fbasic

f = fbasic()
e = eraser()

old_path = '.\\ts_file\\eraser_testfile.txt'
f.ensure('.\\ts_file\\eraser')

new_path = '.\\ts_file\\eraser\\eraser_testfile1.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
e.random(new_path)
print("after file size:", os.path.getsize(new_path))

new_path = '.\\ts_file\\eraser\\eraser_testfile2.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
e.random_block(new_path)
print("after file size:", os.path.getsize(new_path))

new_path = '.\\ts_file\\eraser\\eraser_testfile3.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
e.fill(new_path)
print("after file size:", os.path.getsize(new_path))

new_path = '.\\ts_file\\eraser\\eraser_testfile4.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
e.fill(new_path, [1])
print("after file size:", os.path.getsize(new_path))

new_path = '.\\ts_file\\eraser\\eraser_testfile5.txt'
f.copy(old_path, new_path)
print("before file size:", os.path.getsize(new_path))
e.fill(new_path, [1, 2, 3, 4, 5])
print("after file size:", os.path.getsize(new_path))

input("按回车（Enter）继续")
