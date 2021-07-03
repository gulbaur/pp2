class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        m=str(n)
        a=0
        b=1
        for i in m:
            a+=int(i)
            b*=int(i)
        return b-a
            