class Solution1:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        neg_flag     = numerator * denominator < 0
        numerator    = abs(numerator)
        denominator  = abs(denominator)
        num_pos_dict = {}
        loop_str     = ""
        quotient_list = []
        end = 0
        while True:
              quotient_list.append(str(numerator / denominator))
              # key diff between my and his, use this value can avoid the repeated situation
              numerator = 10 * (numerator % denominator)
              # print numerator
              end += 1
              if numerator == 0:
                 break
              start = num_pos_dict.get(numerator)
              if start is not None:
                 loop_str = "".join(quotient_list[start:end])
                 # print loop_str
                 break
              num_pos_dict[numerator] = end
        res = quotient_list[0]
        if len(quotient_list) > 1:
           res += '.'
        if loop_str:
           res += "".join(quotient_list[1:len(quotient_list) - len(loop_str)]) + '(' + loop_str + ')'
        else:
           res += "".join(quotient_list[1:])
        if neg_flag: res = '-' + res
        return res

class Solution(object):
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        dvd, dvs = abs(numerator), abs(denominator)
        integer, decimal, dict = "", "", {}

        if dvd > dvs:
            integer = str(dvd / dvs)
            dvd %= dvs
        else:
            integer = "0"

        if dvd > 0:
            integer += "."

        idx = 0
        while dvd:
            if dvd in dict:
                decimal = decimal[:dict[dvd]] + "(" + decimal[dict[dvd]:] + ")"
                break

            dict[dvd] = idx
            idx += 1

            dvd *= 10
            decimal += str(dvd / dvs)
            dvd %= dvs

        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0): 
            return "-" + integer + decimal
        else:
            return integer + decimal

if __name__ == '__main__':
   s = Solution()
   print s.fractionToDecimal(2, 3)
   print s.fractionToDecimal(2, 5)