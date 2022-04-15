### Linear Search
### 也叫线性查找，从列表（无序、有序均可）第一个元素开始，顺序进行搜索，直到找到元素或搜索到列表最后一个元素为止。

def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    else:
        return None
