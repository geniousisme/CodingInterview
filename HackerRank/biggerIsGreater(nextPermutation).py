class Solution(object):

      def nextPermutation(self, string):
          length    = len(string)
          string    = list(string)
          partition = -1
          for i in xrange(length - 1, 0, -1):
            if string[i] > string[i - 1]:
                partition = i - 1
                break
          if partition == -1:
            print "no answer"
            return
          for i in xrange(length - 1, partition, -1):
            if string[i] > string[partition]:
                self.swap(string, i, partition)
                break
          self.reverse(string, partition + 1, length - 1)
          print ''.join(string)

      def swap(self, string, left, right):
            string[left], string[right] = string[right], string[left]

      def reverse(self, string, start, end):
            while start < end:
                self.swap(string, start, end)
                start += 1
                end   -= 1

if __name__ == '__main__':
   s = Solution()
   test_num = input()
   for _ in xrange(test_num):
       string = raw_input()
       s.nextPermutation(string)