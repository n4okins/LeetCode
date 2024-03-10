from typing import List, Tuple, Dict, Any, Union


class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        1768. Merge Strings Alternately
        https://leetcode.com/problems/merge-strings-alternately/
        """
        t = ""
        for i in range(min(len(word1), len(word2))):
            t += word1[i] + word2[i]
        if len(word1) > len(word2):
            t += word1[len(word2) :]
        else:
            t += word2[len(word1) :]
        return t

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        1071. Greatest Common Divisor of Strings
        https://leetcode.com/problems/greatest-common-divisor-of-strings/
        """
        if str1 + str2 != str2 + str1:
            return ""
        return str1[: self.gcd(len(str1), len(str2))]

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        1431. Kids With the Greatest Number of Candies
        https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
        """
        maxCandies = max(candies)
        return [(candy + extraCandies) >= maxCandies for candy in candies]

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        605. Can Place Flowers
        https://leetcode.com/problems/can-place-flowers/
        """
        cnt = 0
        if flowerbed[0] == 0:
            flowerbed.insert(0, 0)
        if flowerbed[-1] == 0:
            flowerbed.append(0)
        for f in flowerbed:
            if f == 0:
                cnt += 1
            if cnt == 3:
                n -= 1
                cnt = 1
            if f == 1:
                cnt = 0
            if n == 0:
                break
        return n == 0

    def reverseVowels(self, s: str) -> str:
        """
        345. Reverse Vowels of a String
        https://leetcode.com/problems/reverse-vowels-of-a-string/
        """
        indices = []
        volews = []
        for i, w in enumerate(s):
            if w in "aeiouAEIOU":
                volews.append(w)
                indices.append(i)
        indices = indices[::-1]
        ss = list(s)
        for i, w in zip(indices, volews):
            ss[i] = w
        return "".join(ss)

    def reverseWords(self, s: str) -> str:
        """
        151. Reverse Words in a String
        https://leetcode.com/problems/reverse-words-in-a-string/
        """
        return " ".join(reversed(s.split()))

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        238. Product of Array Except Self
        https://leetcode.com/problems/product-of-array-except-self/
        """
        n = len(nums)
        res = [1] * n
        left = right = 1
        for i in range(n):
            res[i] *= left
            res[-1 - i] *= right
            left *= nums[i]
            right *= nums[-1 - i]
        return res

    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        334. Increasing Triplet Subsequence
        https://leetcode.com/problems/increasing-triplet-subsequence
        """
        a = b = float("inf")
        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True
        return False

    def compress(self, chars: List[str]) -> int:
        """
        443. String Compression
        https://leetcode.com/problems/string-compression/
        """
        current_char = chars[0]
        current_char_cnt = 1
        res = current_char
        for i in range(1, len(chars)):
            if chars[i] == current_char:
                current_char_cnt += 1
            else:
                res += str(current_char_cnt) if current_char_cnt > 1 else ""
                current_char = chars[i]
                current_char_cnt = 1
                res += current_char
        res += str(current_char_cnt) if current_char_cnt > 1 else ""
        for i, r in enumerate(res):
            chars[i] = r
        del chars[len(res) :]
        return len(res)

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        349. Intersection of Two Arrays
        https://leetcode.com/problems/intersection-of-two-arrays/
        """
        return list(set(nums1) & set(nums2))

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1. Two Sum
        https://leetcode.com/problems/two-sum/
        """
        d = dict()
        for i, num in enumerate(nums):
            k = target - num
            if k in d:
                return [d[k], i]
            d[num] = i
        return []

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        4. Median of Two Sorted Arrays
        https://leetcode.com/problems/median-of-two-sorted-arrays/
        """
        nums = sorted(nums1 + nums2)
        n = len(nums)
        if n % 2 == 0:
            return (nums[n // 2 - 1] + nums[n // 2]) / 2
        return nums[n // 2]


if __name__ == "__main__":
    solve = Solution()
    print(solve.findMedianSortedArrays([1, 2], [3, 4]))
