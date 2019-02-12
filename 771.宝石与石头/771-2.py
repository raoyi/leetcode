class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # 遍历求和
        num = 0
        for x in S:
            if x in J:
                num += 1
        return num
