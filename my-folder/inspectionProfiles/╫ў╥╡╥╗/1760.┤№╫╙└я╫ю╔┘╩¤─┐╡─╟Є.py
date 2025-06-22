'''tag:二分查找'''
class Solution(object):
    def minimumSize(self, nums, maxOperations):
        #二分查找范围
        left,right=1,max(nums)
        result= right #结果就在right其中

        while left < right:
            mid=(left+right)//2 #候选
            operation=0  #计数
            for i in nums:
                operation+=(i-1)//mid  # -1的原因:4只需要一次就可以分成两个2
            if operation<=maxOperations:
                result=mid
                right=mid
            else:
                left=mid+1
                # 避免出现 left是2 right是3 一直循环的问题，无法终止 调到left=right为止
        return result



if __name__ == "__main__":
    nums = [9, 7, 5]
    max_operations = 2
    print(Solution().minimumSize((nums),(max_operations)))# 预期输出：5
'''import sys
input = sys.stdin.read
data = input().split()
print(data)
'''

