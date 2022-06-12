# 1. 二维数组中的查找
# import parser
#
#
# class Solution:
#     # array 二维列表
#     array = [1 for i in range(1,20)]
#     print(array)
#     target = 8
#     def Find(self, target, array):
#         # write code here
#         rows = len(array)
#         cols = len(array[0])
#         if rows > 0 and cols > 0:
#             row = 0
#             col = cols - 1
#             while row < rows and col >= 0:
#                 if target == array[row][col]:
#                     return True
#                 elif target < array[row][col]:
#                     col -= 1
#                 else:
#                     row += 1
#         return False
# 2. 替换空格
# target = " We Are Happy , becase today I go to back home ! "
# print(target)

# 替换
# def replace_all():
#     end1 = target.replace(" ","%20",1)
#     return end1
#
# # 去除
# def remove_begin_end():
#     end2 = target.strip()
#     return end2
#
# def remove_begin():
#     end3 = target.lstrip()
#     return end3
#
# def remove_end():
#     end4 = target.rstrip("%50")
#     return end4
#
# print(remove_begin_end())

# 3. 只出现一次的数字
# class Solution:
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         for i in range(0, len(nums), 2):  # 以2为间隔 两两对比
#             if (i == (len(nums) - 1)):  # 倒数第二个之前都相同 返回最后一个值
#                 return nums[i]
#             else:
#                 if (nums[i + 1] != nums[i]):
#                     return nums[i]
#
#
# if __name__ == "__main__":
#     s = Solution()
#     nums = [5, 3, 5, 6, 7, 3, 6]
#     print(s.singleNumber(nums))

# 求众数

