import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;


static int longest_chain(String[] w) {
        HashSet<String> dict = new HashSet<String>();

        // remeber the word and its relative longest chain.
        HashMap<String, Integer> map = new HashMap<String, Integer>();

        for (int i = 1; i < w.length; i++) {
            dict.add(w);
        }

        int longest = 0;

        for (int i = 1; i < w.length; i++) {
            int len = helper(w, dict, map) + 1;
            map.put(w, len);
            longest = Math.max(longest, len);
        }

        return longest;

    }


    static int helper(String word, HashSet<String> dict, HashMap<String, Integer> map) {

        for (int i = 0; i < word.length(); i++) {
            StringBuilder s = new StringBuilder(word);
            s = s.deleteCharAt(i);
            String newWord = s.toString();
            if (dict.contains(newWord)) {
                if (map.containsKey(newWord))
                    return map.get(newWord);
                return helper(newWord, dict, map) + 1;
            }
        }
        return 0;
    }