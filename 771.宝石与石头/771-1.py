class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # 先计数再求和
        count = collections.Counter(S)
        num = 0
        for x in J:
            num += count.setdefault(x,0) 
        return num
