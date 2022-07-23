"""
Questions:
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5


Soln:
quicksort, random pick pivot and arrange smaller nums on left and count
if count < k then go to right section and repeat
if count >k, then go to left section and repeat
if count == k, return 
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.findKthSmallest(nums, 0, len(nums)-1, len(nums)+ 1 - k)
    
    def findKthSmallest(self, nums, left, right, k):
        import random
        if left == right:
            return nums[left]
        pivot = random.randint(left, right)
        idx = self.partition(nums, left, right, pivot)
        if idx +1 == k:
            return nums[idx]
        elif idx + 1 > k:
            return self.findKthSmallest(nums, left, idx-1, k)
        else:
            return self.findKthSmallest(nums, idx+1, right, k)
        
    def partition(self, nums, left, right, pivot):
        val = nums[pivot]
        nums[pivot], nums[right] = nums[right], nums[pivot]
        j = left
        for i in range(left, right):
            if nums[i] < val:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
        nums[right], nums[j] = nums[j], nums[right]
        return j 