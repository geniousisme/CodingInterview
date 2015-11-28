class Solution1(object): # recursive solution
    def canCatchAlibaba(self, num_caves, strategies):
        for i in xrange(num_caves):
            # no matter where the alibaba is, we always can find it with our strategies.
            if self.alibaba_helper(num_caves, strategies, i, 0) is False:
            # so if there are some places we cannot get alibaba, then it fails
                return False
        return True

    def alibaba_helper(self, num_caves, strategies, ali_pos, curr):
        # curr equals to length of strategies,
        # means it iterate to the end of strategies and still cannot find ali,
        # should return False
        if curr == len(strategies):
            return False
        # ali_pos equals to strategies[curr],
        # which means curr index for the strategies just can catch alibaba
        if ali_pos == strategies[curr]:
            return True
        res = True
        if ali_pos > 0:
        # since ali can only move right or left, following case means it moves left
            res = res and self.alibaba_helper(num_caves, strategies, ali_pos - 1, curr + 1)
        if ali_pos < num_caves - 1:
        # this one means it moves right.
            res = res and self.alibaba_helper(num_caves, strategies, ali_pos + 1, curr + 1)
        return res

class Solution2(object):
    def canCatchAlibaba(self, num_caves, strategies):
        # covered[i][j] means that ali's j location at ith day is covered by strategies or not
        covered = [[False for j in xrange(num_caves)] for i in xrange(len(strategies))]
        res = True
        for i in xrange(len(strategies) - 1, -1, -1):
            for j in xrange(num_caves):
                # ith day location j is covered by ith strategy
                if strategies[i] == j:
                    covered[i][j] = True
                else:
                    left = right = True
                    if i + 1 < len(strategies):
                        if j > 0:
                            # same as ali try to move left
                            left  = covered[i + 1][j - 1]
                        if j < num_caves - 1:
                            # same as ali try to move right
                            right = covered[i + 1][j + 1]
                    # check left & right result
                    covered[i][j] = left and right
                if i == 0:
                    # all the possible positions at day 0 should be covered
                    res &= covered[i][j]
        return res

# public static boolean catchAlibaba(int numCaves, int[] strategy){
#         int i,j,l=strategy.length;
#         boolean[][] dp = new boolean[numCaves][l];
#         dp[strategy[l-1]][l-1] = true;
#         for(j=l-2;j>=0;j--){
#                 dp[0][j] = dp[1][j+1];
#                 for(i=1;i<numCaves-1;i++){
#                         dp[i][j] = dp[i-1][j+1] && dp[i+1][j+1];
#                 }
#                 dp[numCaves-1][j] = dp[numCaves-2][j+1];
#                 dp[strategy[j]][j] = true;
#         }
#         for(i=0;i<numCaves;i++){
#                 if(!dp[i][0]) return false;
#         }. from: 1point3acres.com/bbs
#         return true;
# }

# public static void main(String[] args){
#         System.out.println(catchAlibaba(3, new int[]{1,1}));
#         System.out.println(catchAlibaba(4, new int[]{1,1,2,2,1}));
# }

if __name__ == "__main__":
    s1 = Solution2()
    print s1.canCatchAlibaba(3, [1, 1])