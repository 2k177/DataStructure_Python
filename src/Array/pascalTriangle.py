class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        a = [[] for x in range(numRows)]
        for i in range(numRows):
            for j in range(i+1):
                if j<i:
                    if j==0:
                        a[i].append(1)
                    else:
                        a[i].append(a[i-1][j]+a[i-1][j-1])
                elif j==i:
                    a[i].append(1)
        return a