/***
    Solution 1
    Straight forward solution to check each possibility of ways that is a valid 
    translate of the original string. 
***/

/***
    Solution 2
    The problem can be solvd using dynamic programming and the time complexicy 
    would be optimized to O(n)
    Space complexicity O(n)
    The optimal substructure would be :
        1. If the previous char is a valid key in Map: count[i] = count[i - 1]
        2. If the previous two chars are a valid key in Map: count[i] = count[i - 2]
        Or simply count[i] = count[i - 1] + count[i - 2]

***/
public int translate(String s) {
    if(s == null || s.length() == 0)  return 0;
    
    int n = s.length();
    int[] count = new int[n+1];
    count[0] = 1;
    count[1] = s.charAt(0) != '0' ? 1 : 0;
    for(int i = 2; i <= n; i++) {
        int one = Integer.valueOf(s.substring(i-1, i));
        int two = Integer.valueOf(s.substring(i-2, i));
        if(one >= 1 && one <= 9) {
           count[i] += count[i-1];  
        }
        if(two >= 10 && two <= 26) {
            count[i] += count[i-2];
        }
    }
    return count[n];
}

/***
    Solution 3
    We can further optimize the problem by using constant space instead of O(n)
    Only two elements in the array are used in each iteration. We can use two variables 
    to remember the previous results and keep updating them till the end. 
    previous_one = count[i - 1]
    previous_two = count[i - 2]
***/

public int translate(String s) {
    if (s == null || s.length() == 0)
        return 0;
    
    //init
    int n = s.length();
    int previous_two = 1;
    int previous_one = s.charAt(0) != '0' ? 1 : 0;
    int current = 0;

    for(int i = 2; i <= n; i++) {
        int one = Integer.valueOf(s.substring(i-1, i));
        int two = Integer.valueOf(s.substring(i-2, i));
        if(one >= 1 && one <= 9) {
           current += previous_one;  
        }
        if(two >= 10 && two <= 26) {
            current += previous_two;
        }
        //update the value
        previous_two = previous_one;
        previous_one = current;
    }

    return current;
}