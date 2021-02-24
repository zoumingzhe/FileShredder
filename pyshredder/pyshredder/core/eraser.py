#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
# 类 eraser
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2021-02-24 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | Version(self, ...)           | 版本显示
# 已测试 | map(self, ...)               | 路径映射
# 已测试 | ensure(self, ...)            | 路径检查
# 已测试 | get_path(self, ...)          | 获取路径
# 已测试 | get_name(self, ...)          | 获取文件名
# 已测试 | get_folder(self, ...)        | 获取文件夹名
# 已测试 | scan(self, ...)              | 扫描文件
# 已测试 | copy(self, ...)              | 拷贝文件
# 已测试 | move(self, ...)              | 移动文件
# 已测试 | delete(self, ...)            | 删除文件
# 已测试 | archive(self, ...)           | 归档文件
# 已测试 | archive_unpack(self, ...)    | 归档文件释放
# 未开发 | zip(self, ...)               | 压缩文件
# ----------------------------------------------------------------------------------------------------
import os
import random
# ----------------------------------------------------------------------------------------------------
class eraser:
    """
    eraser类提供了对文件的擦除操作。
    """
    def __init__(self):
        self.__version = "0.1"
        self.__align = 4096
# ----------------------------------------------------------------------------------------------------
    def random(self, path):
        """
        随机擦除：
        输入参数：fd
        返回参数：True 成功，False 失败
        说明：该方法提供路径映射的记录，
        若key、path均不为None则记录路径映射，
        若只有key不为None则返回key的路径映射，
        若key、path均为None则返回所有的的路径映射。
        """
        align = 4096
        # 判断文件是否存在
        if not os.path.exists(path):
            return False
        # 读取文件大小
        size = os.path.getsize(path)
        print("file size:", size)
        # 二进制填充
        with open(path, "wb+") as f:
            for idx in range(size):
                f.write(bytes([random.randint(0,255)]))
                if not (idx % self.__align):
                    print(idx)
                    f.flush()
        return True
# ----------------------------------------------------------------------------------------------------
    def random_block(self, path):
        """
        随机擦除（块模式）：
        输入参数：fd
        返回参数：True 成功，False 失败
        说明：该方法提供路径映射的记录，
        若key、path均不为None则记录路径映射，
        若只有key不为None则返回key的路径映射，
        若key、path均为None则返回所有的的路径映射。
        """
        # 判断文件是否存在
        if not os.path.exists(path):
            return False
        # 生成填充数据
        fill = []
        for idx in range(self.__align):
            fill.append(random.randint(0,255))
        data = bytes(fill)
        print("fill data:", data)
        # 读取文件大小
        size = os.path.getsize(path)
        print("file size:", size)
        # 二进制填充
        with open(path, "wb+") as f:
            length = 0
            while length < size:
                length = length + self.__align
                f.write(data)
                f.flush()
        return True
# ----------------------------------------------------------------------------------------------------
