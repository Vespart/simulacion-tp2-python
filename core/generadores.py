import random
from math import sqrt, log, pi, cos, sin


def generar_numeros_pseudoaleatorios(n):
    nums = []
    for i in range(n):
        # al = random.uniform(1e-10, 1.0)
        al = random.random()
        nums.append(al)
    return nums


def darDistExp(nums, lmd):
    for i in range(len(nums)):
        num = round(-1 / lmd * log(nums[i]), 4)
        nums[i] = num
    return nums


def darDistNorm(nums, media, desv):
    for i in range(0, len(nums) - 1, 2):
        num1 = nums[i]
        num2 = nums[i + 1] * 2 * pi
        n1 = ((sqrt((-2) * (log(num1))) * cos(num2)) * desv) + media
        n2 = ((sqrt((-2) * (log(num1))) * sin(num2)) * desv) + media
        nums[i] = round(n1, 4)
        nums[i + 1] = round(n2, 4)

    return nums


def darDistUnifAB(nums, A, B):
    for i in range(len(nums)):
        num = round((B - A) * nums[i] + A, 4)
        nums[i] = num
    return nums
