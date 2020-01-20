'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


# 1 o(n^2), most basic method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]


# 2 o(n), for non-negative integers only
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        location = []
        half = target / 2
        for n in range(0, len(nums)):
            if nums[n] == half: location.append(n)
            if len(location) == 2: return location
        # check if there're two numbers with value [target/2]

        location = []
        for i in range(0, target):
            location.append(-1)
        for n in range(0, len(nums)):
            if nums[n] >= 0 and nums[n] <= target:
                location[nums[n]] = n
        # list location's subscript mentions the original value, value mentions the original subscript
        lh, rh = 0, target
        while lh < rh:
            if location[lh] != -1 and location[rh] != -1 and location[lh] != location[rh]:
                return [location[lh], location[rh]]
            lh += 1
            rh -= 1
        # move from both sides to middle, as long as the two value exists, they add up to [target]


# 3 o(nlogn)
class Solution:
    def sort(self, list):
        if len(list) < 2:
            return list
        else:
            mid = list[0]
            left = [i for i in list[1:] if i[2] <= mid[2]]
            right = [i for i in list[1:] if i[2] > mid[2]]
            return self.sort(left) + [mid] + self.sort(right)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        half = target / 2
        loc_val_dis = []
        # location_value_distance from [target/2]
        # saved as [[loc1, val1, dis1], [loc2, val2, dis2] ...]
        for n in range(0, len(nums)):
            loc_val_dis.append([n, nums[n], abs(nums[n] - half)])
        loc_val_dis = self.sort(loc_val_dis)
        for n in range(0, len(loc_val_dis) - 1):
            if loc_val_dis[n][1] + loc_val_dis[n + 1][1] == target:
                return [loc_val_dis[n][0], loc_val_dis[n + 1][0]]


# 4 using functions
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            try : j = nums.index(target - nums[i])
            except: continue
            else:
                if i != j : return[i, j]
