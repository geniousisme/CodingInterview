# Enter your code here. Read input from STDIN. Print output to STDOUT
def number_list(coefficients):
    num_str_list = coefficients.split(',')
    return [float(num) for num in num_str_list]

def linear_model(test_case, coefficients):
    test_case.insert(0, 1)
    length    = len(coefficients)
    res       = sum([test_case[i] * coefficients[i] for i in xrange(length)])
    if res > 0:
       print "suspect fraud"
    else:
       print "not fraud"

if __name__ == '__main__':
   coefficients = number_list(raw_input())
   while True:
        try:
            test_case = number_list(raw_input())
            linear_model(test_case, coefficients)
        except:
            break



  
