class Solution:
    def search(self, nums, target: int) -> int:
        # 小于最小值，大于最大值
        if target < nums[0] or target > nums[-1]:
            return -1

        low = 0
        high = len(nums) - 1

        # 循环直到low>high结束，low==high时说明还剩最后一个元素用于比较
        while low <= high:
            # 取中间值，除完取整
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            # target比中间值大，说明要继续在右边区间找
            elif nums[mid] < target:
                low = mid + 1
            # target比中间值小，说明要继续在左边区间找
            elif nums[mid] > target:
                high = mid - 1

            print(low, high)
        return -1


if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 2
    s = Solution()
    s.search(nums, target)
