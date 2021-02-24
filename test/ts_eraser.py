import sys
sys.path.insert(0, r'..\pyshredder')
from pyshredder.core.eraser import eraser
from ztools import fbasic

f = fbasic()
e = eraser()

path = '.\\ts_file\\eraser_testfile.txt'

f.copy(path, '.\\ts_file\\eraser_testfile1.txt')
e.random('.\\ts_file\\eraser_testfile1.txt')

f.copy(path, '.\\ts_file\\eraser_testfile2.txt')
e.random_block('.\\ts_file\\eraser_testfile2.txt')

input("按回车（Enter）继续")
