#Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
# let the target be 9
nums=[7,3,2,5]
target=9
num=0
def targets(nums,target):
    num=target-nums[0]
    for i in range(1,len(nums)):
        if num==nums[i]:
            return [i,0]
        
values=targets(nums,target)
print(values)