"""
0349. Intersection of Two Arrays (Easy)
https://leetcode.com/problems/intersection-of-two-arrays/
"""


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        left_1, left_2 = 0, 0
        res = []
        while left_1 < len(nums1) and left_2 < len(nums2):
            if nums1[left_1] == nums2[left_2]:
                if nums1[left_1] not in res:
                    res.append(nums1[left_1])
                left_1 += 1
                left_2 += 1
            elif nums1[left_1] < nums2[left_2]:
                left_1 += 1
            elif nums1[left_1] > nums2[left_2]:
                left_2 += 1
        return res


def main():
    s = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(f"Input: nums1={nums1}, nums2={nums2} \nOutput: {s.intersection(nums1, nums2)}")
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(f"Input: nums1={nums1}, nums2={nums2} \nOutput: {s.intersection(nums1, nums2)}")


if __name__ == "__main__":
    main()
