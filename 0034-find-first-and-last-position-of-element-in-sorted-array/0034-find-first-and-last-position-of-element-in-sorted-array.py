class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def first():
            ans=-1
            low=0
            high=len(nums)-1
            while(low<=high):
                mid=(low+high)//2
                if(target==nums[mid]):
                    ans=mid
                    high=mid-1
                elif(nums[mid]>target):
                    high=mid-1
                elif(nums[mid]<target):
                    low=mid+1
            return ans
        def last():
            ans=-1
            low=0
            high=len(nums)-1
            while(low<=high):
                mid=(low+high)//2
                if(target==nums[mid]):
                    ans=mid
                    low=mid+1
                elif(target>nums[mid]):
                    low=mid+1
                elif(target<nums[mid]):
                    high=mid-1
            return ans
        return [first(),last()]