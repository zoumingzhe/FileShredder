#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
# 类 paint
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2021-02-28 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | __random_block(self, ...)    | 生成随机数据块
# 未开发 | painting(self, ...)          | 随机擦除（块）
# ----------------------------------------------------------------------------------------------------
import os
import time
import random
import base64
import psutil
from ztools import fbasic
from collections import namedtuple
from concurrent.futures import ThreadPoolExecutor
# ----------------------------------------------------------------------------------------------------
class paint:
    """
    paint类提供了通过在磁盘剩余空间写入新文件数据的方式从而彻底擦除磁盘的操作。
    """
    def __init__(self):
        self.__version = "0.1"
        self.__align = 4096
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def __random_block(length):
        """
        生成随机数据块：
        输入参数：length 数据块长度
        返回参数：随机数据块
        说明：该方法可生成指定长度的数据数据块。
        """
        data = []
        # 生成随机数据
        for idx in range(length):
            randint = random.randint(0,255)
            data.append(randint)
        return bytes(data)
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def painting(path, sum_size, block_size = 4096, block_num = 1024):
        """
        随机擦除（块）：
        输入参数：path 文件路径
        返回参数：True 成功， False 失败
        说明：该方法通过对文件覆写随机数（块）来擦除文件，
        由于按self.__align值生成随机数（块），
        并用随机数（块）循环覆写文件，速度较快；
        但是覆写后文件大小为self.__align值的整数倍，
        并且数据按随机数（块）大小重复。
        """
        # 是否为文件夹且存在？
        if not os.path.exists(path):
            return False
        # 生成填充文件
        size = 0
        while (size < sum_size):
            # 生成文件名
            namebytes = (str(int(time.time()*100))).encode("utf-8")
            name = base64.b64encode(namebytes).decode("utf-8")[:16]
            file = path + str('\\%s.dat' % name)
            # 文件是否存在？
            if os.path.exists(file):
                continue
            # 生成填充数据
            data = paint.__random_block(block_size)
            # print("fill data:", data)
            # 对文件用二进制随机数（块）覆写
            with open(file, "wb+") as f:
                num = 0
                while num < block_num:
                    num = num + 1
                    f.write(data)
                    f.flush()
                size = size + block_size * num
        return True
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def disks(percent = 97.0):
        """
        硬盘剩余空间填充：
        输入参数：percent 填充百分比
        返回参数：
        说明：该方法对所有硬盘剩余空间进行随机数据填充。
        """
        threads = []
        thdwork = namedtuple('thread', 'tno future')
        thdpool = ThreadPoolExecutor(max_workers=50, thread_name_prefix="THD")
        disks = psutil.disk_partitions()
        for disk in disks:
            # 生成文件名
            namebytes = (str(int(time.time()*100))).encode("utf-8")
            name = base64.b64encode(namebytes).decode("utf-8")[:16]
            path = disk.device + name
            print(path)
            fbasic.ensure(path)
            psutil.disk_usage(disk.device)
            while True:
                disk_pt = psutil.disk_usage(disk.device).percent
                if disk_pt >= percent:
                    break
                print(disk.device, disk_pt)
                future = thdpool.submit(paint.painting,path,100*1024*1024)
                # paint.painting(path, sum_size = 100*1024*1024)
            bar.EOF()
# ----------------------------------------------------------------------------------------------------
