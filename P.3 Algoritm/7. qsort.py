import random
import time
from copy import deepcopy
from datetime import datetime
import numpy as np
def qsort(array):
    less = []
    greater = []
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        for i in array[1:]:
            if i <= pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
        return qsort(less) + [pivot] + qsort(greater)


def bubble_sort(nums):
    global counter
    counter = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            counter += 1
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return nums



def sort1(nums):
    new_nums = []
    while len(nums) != 0:
        min_n = nums[0]
        for i in nums:
            if i< min_n:
                min_n = i
        new_nums.append(min_n)
        nums.remove(min_n)
    return new_nums

def selection_sort(nums):
    # global counter
    # counter = 0
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(nums)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            # counter += 1
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    return(nums)

list_of_nums = [random.randint(1,1000) for i in range(1, 1000)]

start_time = time.time()
qsort(deepcopy(list_of_nums))
print('qsort',time.time()-start_time)

start_time = time.time()
bubble_sort(deepcopy(list_of_nums))
print('bubble_sort',time.time()-start_time)



start_time = time.time()
selection_sort(deepcopy(list_of_nums))
print('selection_sort',time.time()-start_time)

start_time = time.time()
sort1(deepcopy(list_of_nums))
print('sort1',time.time()-start_time)


aa= selection_sort(list_of_nums)
print(len(aa))
