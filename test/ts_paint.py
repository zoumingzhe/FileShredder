import os
import sys
sys.path.insert(0, r'..\pyshredder')
from pyshredder.core.paint import paint
from ztools import fbasic

fbasic.ensure('D:\\painting')
paint.disks(70.0)

input("按回车（Enter）继续")
