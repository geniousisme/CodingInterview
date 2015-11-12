# Time:  O(n)
# Space: O(1)
#
# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
# You begin the journey with an empty tank at one of the gas stations.
#
# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
#
# Note:
# The solution is guaranteed to be unique.
#

class Solution1:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer

    # one pass solution
    def canCompleteCircuit(self, gas, cost):
        start, total_sum, current_sum = 0, 0, 0

        for i in xrange(len(gas)):
            # curr_sum add all difference between gas[i] & cost first
            # total sum just add all the difference together
            diff = gas[i] - cost[i]
            current_sum += diff
            total_sum += diff
            # if curr_sum is smaller than 0, which mean it cannot start from last start
            # then restart from the next point(index), since it cannot make it to the next point
            if current_sum < 0:
                start = i + 1
                current_sum = 0

        if total_sum >= 0:
            # check the total sum at the end
            # if total sum is bigger then 0, which means I can complete the circuit
            # then I can return start
            return start
        return -1

class Solution:

    def canCompleteCircuit(self, gas, cost): # two pass solution
        # 
        if sum(cost) > sum(gas): return -1
        diff = start = 0
        for i in xrange(len(gas)):
            # diff = gas[i - 1] - cost[i - 1]
            if diff + gas[i] < cost[i]:
               start = i + 1
               diff = 0
            else:
               diff += gas[i] - cost[i]
        return start




