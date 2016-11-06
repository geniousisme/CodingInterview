/*
 * Complete the function below.
 */

    static int longestChain(String[] words) {
        if(words == null || words.length == 0)
            return 0;
        
        int maxLen = 0;
        HashSet<String> dict = new HashSet<>(Arrays.asList(words));
        //key: word; value: chainlength 
        HashMap<String, Integer> map = new HashMap<>();
        
        for(String word: words) {
            if(maxLen >= word.length())
                continue;
            int len = chain(dict, map, word);
            map.put(word, len);
            maxLen = Math.max(maxLen, len);
        }
        
        return maxLen;
    }

    private static int chain(HashSet<String> dict, HashMap<String, Integer> map, String word) {
        if(word.length() == 0) {
            return dict.contains("")? 1 : 0;
        }
            
        int len = 1;
        
        for(int i = 0; i < word.length(); i++) {
            String tmp = word.substring(0, i) + word.substring(i + 1);
            if(!dict.contains(tmp))
                continue;
            if(map.containsKey(tmp)) {
                len = Math.max(len, map.get(tmp) + 1);
            } else {
                int nextLen = chain(dict, map, tmp);
                len = Math.max(len, nextLen + 1);
            }
        }
        
        return len;
    }