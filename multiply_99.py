# -*- coding:utf-8 -*-
__author__ = 'KAFKA.M'


def multiply_99():
    for i in range(1, 10):
        for j in range(1, 1+i):
            print('%2sx%2s= %2s\t' % (j, i, j*i), end='')
        print()


if __name__ == '__main__':
    multiply_99()
