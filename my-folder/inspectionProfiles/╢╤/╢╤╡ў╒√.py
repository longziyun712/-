#添加新元素之后向上调整
def upAdjust(heap):
    i = len(heap) - 1  # 新添加的节点位置
    while i // 2 > 0:  # 确保不是根节点
        if heap[i] > heap[i // 2]:  # 如果当前节点大于父节点
            heap[i], heap[i // 2] = heap[i // 2], heap[i]  # 交换
        i = i // 2  # 移动到父节点


#删除堆顶元素之后向下调整 最小堆
def down_adjust_min(heap, parent_index, end_index):
"""  heap: 堆数组（列表）
     parent_index: 要调整的父节点索引
     end_index: 堆最后一个元素的索引 """
    child_index = 2 * parent_index + 1  # 左孩子索引
    while child_index <= end_index:
        # 找出两个子节点中较小的那个
        if child_index + 1 <= end_index and heap[child_index + 1] < heap[child_index]:
            child_index += 1
        # 如果子节点比父节点小，则交换
        if heap[child_index] < heap[parent_index]:
            heap[parent_index], heap[child_index] = heap[child_index], heap[parent_index]
            parent_index = child_index
            child_index = 2 * parent_index + 1
        else:
            break
