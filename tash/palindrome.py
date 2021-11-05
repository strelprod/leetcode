# палиндром

def palindrome(arr: list) -> bool:
    if not arr:
        return False
    ix = 0
    iy = len(arr) - 1
    while ix < iy:
        if arr[ix] != arr[iy]:
            return False
        ix += 1
        iy -= 1

    return True


def palindrome(arr: list) -> bool:
    if not arr:
        return False

    for ix in range(len(arr) // 2):
        if arr[ix] != arr[-ix-1]:
            return False

    return True




assert palindrome([1, 2, 3, 2, 1]) == True
assert palindrome([1, 2, 2, 1]) == True
assert palindrome([1, 2, 1]) == True
assert palindrome([1, 2, 3]) == False
assert palindrome([3, 2, 1]) == False
assert palindrome([1]) == True
assert palindrome([]) == False
assert palindrome([-1, 0, 1]) == False
assert palindrome([-1, 0, -1]) == True