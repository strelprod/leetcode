# 5 1 3 2
# делим массив на 2 части
# 5 1 и 3 2
# делим подмасив рекурсивно на 2 части, пока не останется по 1 элементу
# 5 и 1, 3 и 2
# мержим 5 и 1, 3 и 2
# мержим 1 5 и 2 3
# результат 1 2 3 5


def merge(left_half, right_half):
    merged_arr = []
    left_len = len(left_half)
    right_len = len(right_half)
    rix = lix = 0


    while rix < right_len and lix < left_len:
        if left_half[lix] < right_half[rix]:
            merged_arr.append(left_half[lix])
            lix += 1
        else:
            merged_arr.append(right_half[rix])
            rix += 1

    while rix < right_len:
        merged_arr.append(right_half[rix])
        rix += 1

    while lix < left_len:
        merged_arr.append(left_half[lix])
        lix += 1

    return merged_arr

def merge_sort(arr):
    arr_len = len(arr)
    if arr_len < 2:
        return arr

    left_half = arr[:arr_len // 2]
    right_half = arr[arr_len // 2:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    merged = merge(left_half, right_half)

    return merged


arr = [5, 11, 1, 12]
assert merge_sort(arr) == sorted(arr)

arr = []
assert merge_sort(arr) == sorted(arr)

arr = [1]
assert merge_sort(arr) == sorted(arr)

arr = [1, 2]
assert merge_sort(arr) == sorted(arr)

arr = [2, 1]
assert merge_sort(arr) == sorted(arr)

arr = [1, 3, 2]
assert merge_sort(arr) == sorted(arr)
