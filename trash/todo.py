# Дан список: [4, 1, 2, 3, 3, 1]
# Распечатать элементы, встречающиеся ровно один раз

from typing import List, Reversible
from collections import Counter

def calc(arr: List[int]) -> int:
    count = Counter(arr)
    res = []
    for k in count:
        if count[k] == 1:
            res.append(k)
    return res

def calc(arr: List[int]) -> int:
    arr.sort()
    res = []
    ix = 1
    cnt = 1
    while ix < len(arr):
        if arr[ix - 1] == arr[ix]:
            cnt += 1
        else:
            if cnt == 1:
                res.append(arr[ix - 1])
            cnt = 1
        ix += 1
    if cnt == 1:
        res.append(arr[ix - 1])
    return res

#1 1 2 3 3 4
assert sorted([4, 2]) == sorted(calc([4, 1, 2, 3, 3, 1]))



# Найти количество чисел, меньше заданного для каждого элемента списка

def find_less_nums(arr: List[int]) -> List[int]:
    arr_sorted = sorted(map(list, enumerate(arr)), key=lambda x: x[1])

    curr_val = arr_sorted[len(arr_sorted) - 1]
    curr_val = arr_sorted[0][1]
    cnt_uniq = 0
    for ix in range(len(arr_sorted)):
        if arr_sorted[ix][1] != curr_val:
            cnt_uniq += 1
            curr_val = arr_sorted[ix][1]
        arr_sorted[ix][1] = cnt_uniq
    
    return list(map(lambda x: x[1], sorted(arr_sorted, key=lambda x: x[0])))



assert find_less_nums([4, 3, 1, 4]) == [2, 1, 0, 2]
assert find_less_nums([5, 3, 1, 4]) == [3, 1, 0, 2]
assert find_less_nums([1]) == [0]
assert find_less_nums([1, 2]) == [0, 1]
assert find_less_nums([1, 2, 2]) == [0, 1, 1]
