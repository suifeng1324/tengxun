# author:yangleiw
# createdate:2022/5/14
import numpy as np


# print(np.__version__)  # 查看numpy版本


def python_sum(n: object) -> object:
    a = [i ** 2 for i in range(n)]  # 使用列表生成式创建1到N的平方
    b = [i ** 3 for i in range(n)]  # 使用列表生成式创建1到N的立方
    ab_sum = []  # 创建新列表
    for i in range(n):
        ab_sum.append(a[i] + b[i])
    return ab_sum


def numpy_sum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    return a + b


def numpy_array():  # 数组
    print(np.array([1, 2, 3, 4, 5]))
    print(np.array(range(10)))
    print(np.array([i ** 2 for i in range(10)]))
    print(np.array([i for i in range(10) if i % 2 == 0]))
    print([i for i in range(2, 11, 2)])
    print(np.array([[1, 2, 3], ["a", "b", "c", "d"]], dtype=object))  # 强制转换类型
    print(np.array([1.5, 2.2, 3.8], dtype='int'))
    print(np.array([1, 2, 3], ndmin=2))


def numpy_arange():  # 区间数组
    # numpy.arange(start,stop,step,dtype)
    print(np.arange(10))
    print(np.arange(5, dtype=float))
    print(np.arange(10, 20, 2))  # 起始10，终止20，步长2
    a = np.arange(0, 200, 3)
    print(a[len(a) - 1], len(a))


def numpy_linspace():  # 等差数列
    # numpy.arange(start,stop,num=50,endpoint=True,retstep=False,dtype=None)
    print(np.linspace(1, 4, 7))  # 包前包后


def numpy_logspace():  # 等比数列
    # numpy.logspace(start,stop,num=50,endpoint=True,base=10.0,dtype=None)
    print(np.logspace(1, 5, 3, base=2))  # 2的1-5次方[ 2.  8. 32.]


def numpy_zeros():  # 全0数列
    # numpy.zeros(shape,dtype=float,order="C")
    print(np.zeros(5))  # [0. 0. 0. 0. 0.]
    print(np.zeros(5, dtype='int'))  # [0 0 0 0 0]
    print(np.zeros((2, 2), dtype='int'))  # [[0 0],[0 0]]
    print(np.zeros((2, 2, 3), dtype='int'))  # [[[0 0 0],[0 0 0]],[[0 0 0],[0 0 0]]]


def numpy_ones():  # 全1数列
    # numpy.ones(shape,dtype=float,order="C")
    print(np.ones(5))  # [1. 1. 1. 1. 1.]


def numpy_array_attribute():
    # print(np.arange(6).reshape((2,3)))  #返回调整维度后的副本，不改变原ndarray，返回：[[0 1 2],[3 4 5]]
    a = np.arange(5)
    # print(np.resize(a, (2, 3)))  # 如果新数组大于原始，则新数组将填充a的重复副本，返回：[[0 1 2],[3 4 0]]
    # print(a.resize((2, 3), refcheck=False))  # 如果新数组大于原始，则新数组将填充0，返回：[[0 1 2],[3 4 0]]
    print(np.arange(5).size)  # 数组元素的总个数 5


if __name__ == '__main__':
    # result1 = python_sum(10)
    # result2 = numpy_sum(10)
    # print(result1, result2)
    numpy_array_attribute()
