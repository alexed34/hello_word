import time
import random

def bubble_sort(nums):
    global counter
    counter = 0
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            counter += 1
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True



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



def sort(nums):
    new_nums = []
    while len(nums) != 0:
        min_n = nums[0]
        for i in nums:
            if i< min_n:
                min_n = i
        new_nums.append(min_n)
        # len(nums)
        nums.remove(min_n)
    return new_nums




# list_of_nums = [6, 1, 3, 9, 5]
list_of_nums = [random.randint(1,1000) for i in range(1, 1000)]
# bubble_sort(list_of_nums)
# print(list_of_nums,counter)
# selection_sort(list_of_nums)
# print(list_of_nums, counter)
#
# list_of_nums = [5, 4, 3, 2, 1]
# bubble_sort(list_of_nums)
# print(list_of_nums,counter)
s_t = time.time()
bubble_sort(list_of_nums)
print(time.time() - s_t)
s_t = time.time()
selection_sort(list_of_nums)
print(time.time() - s_t)
# print(list_of_nums, counter)
s_t2 = time.time()
sort(list_of_nums)
print(time.time() - s_t2)
