from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        189. 旋转数组
        """
        n = len(nums)
        k = k % n
        count = 0
        # 每当遇到环的时候就给初始元素+1继续循环
        for start in range(0, n):
            current = start
            prev = nums[start]
            while True:
                next_ = (current + k) % n
                temp = nums[next_]
                nums[next_] = prev
                prev = temp
                current = next_
                count += 1
                # 当所有的元素的值都替换过一遍后就退出，看不懂官方解里gcd方法的代替品
                if count == n:
                    return
                # 遇到环时退出，给start+1再继续
                if current == start:
                    break

    # 如果出现环的话，计算总共有几个环
    def gcd(self, k, n):
        if n > 0:
            return self.gcd(n, k % n)
        return k

    def rotate_with_reverse(self, nums: List[int], k: int) -> None:
        """
        189. 旋转数组
        """
        k = k % len(nums)
        print(k)
        # 先将整个数组倒序
        self.reverse(nums, 0, len(nums) - 1)
        print(nums)
        # 再将前k部分倒序
        self.reverse(nums, 0, k-1)
        print(nums)
        # 再将k之后的部分倒序
        self.reverse(nums, k, len(nums) - 1)
        print(nums)

    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    def moveZeroes(self, nums: List[int]) -> None:
        """
        283. 移动零
        Do not return anything, modify nums in-place instead.
        """
        # 主指针a遍历数组，b指针记录排序队尾
        a = b = 0
        while a < len(nums):
            if nums[a] != 0:
                nums[a], nums[b] = nums[b], nums[a]
                b+=1
            a+=1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 主指针负责遍历整个数组，副指针在剩下的数组里找合适的值，因为数组是非递减数字，hash表会面临key相同的问题，所以可以用二分查找
        # n = len(numbers)
        # for i in range(n):
        #     low, high = i + 1, n - 1
        #     while low <= high:
        #         mid = (low + high) // 2
        #         if numbers[mid] == target - numbers[i]:
        #             return [i + 1, mid + 1]
        #         elif numbers[mid] > target - numbers[i]:
        #             high = mid - 1
        #         else:
        #             low = mid + 1

        # return [-1, -1]

        for a in range(len(numbers)):
            left = a + 1
            right = len(numbers) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == target - numbers[a]:
                    return [a, mid]
                elif numbers[mid] < target - numbers[a]:
                    left = mid + 1
                else:
                    right = mid - 1
        return [-1, -1]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res

        result = []
        nums.sort()
        print(nums)
        for a in range(len(nums)):
            if nums[a] > 0: return result
            if a>0 and nums[a] == nums[a-1]:
                continue
            b = a + 1
            c = len(nums) - 1
            while b < c:
                print(f"a: {a}, b: {b}, c: {c}")
                if nums[a] + nums[b] + nums[c] == 0:
                    result.append([nums[a], nums[b], nums[c]])
                    while b<c and nums[b]==nums[b+1]:
                        b += 1
                    while b<c and nums[c]==nums[c-1]:
                        c -= 1
                    b += 1
                    c -= 1
                elif nums[a] + nums[b] + nums[c] > 0:
                    c -= 1
                else:
                    b += 1
        return result
        # 官方解
        # nums.sort()
        # res = []
        # for first in range(len(nums)):
        #     if first > 0 and nums[first] == nums[first-1]:
        #         continue
        #     third = len(nums) - 1
        #     for second in range(first+1, len(nums)):
        #         if second > first + 1 and nums[second] == nums[second-1]:
        #             continue
        #         while second < third and nums[first] + nums[second] + nums[third] > 0:
        #             third -= 1
        #         if second == third:
        #             break
        #         if nums[first] + nums[second] + nums[third] == 0:
        #             res.append([nums[first], nums[second], nums[third]])
        # return res


if __name__ == '__main__':
    s = Solution()
    # [3, 99, -1, -100]
    # leetcode 189
    # s.rotate([-1,-100,3,99], 2)
    # s.rotate_with_reverse([-1,-100,3,99], 6)
    # s.moveZeroes([0,1,0,3,12])
    # s.moveZeroes([0, 0, 1])
    # s.twoSum([2,7,11,15], 9)
    s.threeSum([-1,0,1,2,-1,-4])

