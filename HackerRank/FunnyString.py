class Soultion(object):
      def isFunnystring(self, str):
          idx = 0; length = len(str)
          while idx < length - 1:
                left_diff  = abs(ord(str[idx]) - ord(str[idx + 1]))
                right_diff = abs(ord(str[length - idx - 1]) - ord(str[length - idx - 2]))
                if left_diff != right_diff:
                   return False
                idx += 1
          return True

if __name__ == '__main__':
   s = Soultion()
   T = input()
   for _ in xrange(T):
       str = raw_input()
       if s.isFunnystring(str):
          print "Funny"
       else:
          print "Not Funny"