class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a = 0
        max = 0
        for i in gain:
            a+=i
            if max<a:
                max=a
        return max