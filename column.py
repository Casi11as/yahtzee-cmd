# -*- coding: utf-8 -*-

def numberPoint(nums, number):
    count = 0
    for num in nums:
        if num == number:
            count += 1
    point = count * number
    return point

def award(numberPoints):
    if numberPoints[0]+numberPoints[1]+numberPoints[2]+numberPoints[3]+numberPoints[4]+numberPoints[5] >=63:
        point = 35
    else:
        point = 0
    return point

def threeAddTwo(nums):
    numss = nums.copy()
    numss.sort()
    if numss[0]==numss[1]==numss[2] and numss[3]==numss[4]:
        point = 25
    elif numss[0]==numss[1] and numss[2]==numss[3]==numss[4]:
        point = 25
    else:
        point = 0
    return point

def fourAddOne(nums):
    numss = nums.copy()
    numss.sort()
    if numss[0]==numss[1]==numss[2]==numss[3]:
        point = numss[0] * 4 + numss[4]
    elif numss[1]==numss[2]==numss[3]==numss[4]:
        point = numss[4] * 4 + numss[0]
    else:
        point = 0
    return point

def bigStraight(nums):
    if 2 in nums and 3 in nums and 4 in nums and 5 in nums and (1 in nums or 6 in nums) :
        point = 40
    else:
        point = 0
    return point

def smallStraight(nums):
    if 3 in nums and 4 in nums and ((1 in nums and 2 in nums)or(2 in nums and 5 in nums)or(5 in nums and 6 in nums)):
        point = 30
    else:
        point = 0
    return point

def yahtzee(nums):
    if nums[0]==nums[1]==nums[2]==nums[3]==nums[4]:
        point = 50
    else: point = 0
    return point

def sum(nums):
    point = nums[0]+nums[1]+nums[2]+nums[3]+nums[4]
    return point

# if __name__ == '__main__':
#     nums = [3,1,1,5,2]
#     # onepoint = numberPoint(nums,1)
#     # twopoint = numberPoint(nums, 2)
#     # threepoint = numberPoint(nums,3)
#     # fourpoint = numberPoint(nums,4)
#     # fivepoint = numberPoint(nums,5)
#     # sixpoint = numberPoint(nums,6)
#     # numberpoints = [onepoint,twopoint,threepoint,fourpoint,fivepoint,sixpoint]
#     # awardpoint = award(numberpoints)
#     # threeaddtwo_point = threeAddTwo(nums)
#     # fouraddone_point = fourAddOne(nums)
#     # bigStraight_point = bigStraight(nums)
#     smallStraight_point = smallStraight(nums)
#     print(smallStraight_point)