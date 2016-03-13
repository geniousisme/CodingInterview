# Time:  O(|V| + |E|)
# Space: O(|E|)
#
# There are a total of n courses you have to take, labeled from 0 to n - 1.
# 
# Some courses may have prerequisites, for example to take course 0 
# you have to first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs,
#  is it possible for you to finish all courses?
# 
# For example:
# 
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 
# you should have finished course 0. So it is possible.
# 
# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have 
# finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
# 
# click to show more hints.
# 
# Hints:
# This problem is equivalent to finding if a cycle exists in a directed graph. 
# If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
# There are several ways to represent a graph. For example, the input prerequisites is a graph represented by
#  a list of edges. Is this graph representation appropriate?
# Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts
#  of Topological Sort.
# Topological sort could also be done via BFS.
#

class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        degrees  = [0 for i in xrange(numCourses)]
        children = [[] for i in xrange(numCourses)]
        for pre in prerequisites:
            degrees[pre[0]] += 1
            children[pre[1]].append(pre[0])
        courses  = range(numCourses)

        cycle_flag = True
        while cycle_flag and courses != []:
              cycle_flag = False
              removelist = []
              for course in courses:
                  if degrees[course] == 0:
                     for child in children[course]:
                         degrees[child] -= 1
                     removelist.append(course)
                     cycle_flag = True
              for course in removelist:
                  print course
                  courses.remove(course)
        return courses == []


if __name__ == '__main__':
   s = Solution()
   print s.canFinish(2, [[1, 0]])
   print s.canFinish(2, [[0, 1]])
   print s.canFinish(2, [[1, 0], [0, 1]])
   

