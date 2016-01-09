// Forward declaration of isBadVersion API.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        long long start =  1, end = n, mid; // avoid overflow
        while (start < end) {
               mid = (start + end) / 2;
               if (isBadVersion(mid)) {
                   end = mid;
               }
               else {
                   start = mid + 1;
               };
        };
        return start;
    }
};

class Solution {
public:
    int firstBadVersion(int n) {
        int start = 1, end = n; mid = 0;
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (isBadVersion(mid))
                end = mid;
            else
                start = mid;
        }
        if (isBadVersion(start))
            return start;
        return end;
    }
};