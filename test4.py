"""
Quick sort
"""
import random


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li, right, mid+1)


def partition(li, left, right):
    """从给定列表的指定范围随机抽取一个数 x
    找到 x 在列表中的相应位置 pos
    使得列表中所有 pos 左边的数都比 x 小
    所有 pos 右边的数都比 x 大
    将 x 放到列表中 pos 所在的位置
    并返回 pos
    """
    pos = random.randint(left, right)
    tmp = li[pos]

    while left < right:

        # 由于取出了tmp
        # 可以视作tmp所在列表中的位置为一个空位
        # 先从空位的左边部分从左往右开始寻找
        # 如果出现某个数大于tmp
        # 那么交换两个数的位置
        while left < pos and li[left] <= tmp:
            left += 1
        li[pos] = li[left]
        pos = left

        # 同理从右往左找
        while pos < right and li[right] >= tmp:
            right -= 1
        li[pos] = li[right]
        pos = right

    # 最后将 tmp 放到 pos 所在位置
    # 使得: pos 左边的数都比 tmp 小，
    #      pos 右边的数都比 tmp 大
    li[pos] = tmp
    return pos


if __name__ == '__main__':
    li = list(range(10000, 0, -1))
    # random.shuffle(li)

    print(li)
    quick_sort(li, 0, len(li)-1)
    print(li)
