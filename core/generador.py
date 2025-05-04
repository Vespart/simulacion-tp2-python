import random
from math import sqrt, log, pi, cos, sin
import bisect


def generar_numeros_pseudoaleatorios(n):
    nums = []
    for i in range(n):
        al = random.uniform(1e-10, 1.0)
        bisect.insort(nums, al)
    return nums


def darDistExp(nums, lmd):
    for num in nums:
        num = (-1 / lmd) * log(1 - num)
    return nums


def darDistNorm(nums, media, desv):
    for i in range(0, len(nums) - 1, 2):
        num1 = nums[i]
        num2 = nums[i + 1]
        n1 = (sqrt(-2 * log(num1)) *
              cos(2 * pi * num2)) * desv + media
        n2 = (sqrt(-2 * log(num1)) *
              sin(2 * pi * num2)) * desv + media
        nums[i] = n1
        nums[i + 1] = n2

    return nums


def darDistUnifAB(nums, A, B):
    for num in nums:
        num = (B - A) * num + A
    return nums
