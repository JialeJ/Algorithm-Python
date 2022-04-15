### Binary Search
###又叫折半查找。二分查找针对的是一个 "有序的" 数据集合，查找思想有点类似分治思想。
### 每次都通过跟区间的 "中间元素" 对比，将待查找的区间缩小为之前的一半，直到找到要查找的元素，或者区间被缩小为0。

### 两种实现：非递归和递归

### 非递归方法
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    
    while left <= right:
        mid = (left + right) // 2		# 自动向下取整
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ind = binary_search(li, 3)

### 递归
def binary_search(li, val):
    n = len(li)
    mid = n // 2
    if li[mid] > val:
        return binary_search(li[0:mid], val)
    elif li[mid] < val:
        return binary_search(li[mid+1:], val)
    else:
        return mid
