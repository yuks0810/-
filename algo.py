from typing import List
import random

def merge_sort(numbers: List[int]) -> List[int]:
    # 各要素が１になった時には再起関数を抜ける
    if len(numbers) <= 1:
        return numbers
    
    center = len(numbers) // 2
    left = numbers[center:]
    right = numbers[:center]

    merge_sort(left)
    merge_sort(right)

    """
    マージする時の片方の配列を管理するindexが = i
    マージする時のもう一方を管理するindexが = j
    マージ後の配列を管理するindexが = k
    となる
    """

    i = j = k = 0

    while i < len(left) and j < len(right):
        # leftの値とrightの値を比較した時にleftが小さければleftの値を入れ、rightの値が小さければrightの値を入れるようにする
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k += 1

    return numbers


nums = [random.randint(0, 1000) for i in range(10)]
print(merge_sort(nums))