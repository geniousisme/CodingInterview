import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;


public class FriendCircle {

            static int friendCircles(String[] friends) {
                if (null == friends || 0 == friends.length)
                    return 0;
                HashSet<Integer> all = new HashSet<Integer>();
                for (int i = 0; i < friends.length; i++) {
                    all.add(i);
                }
                HashMap<Integer, ArrayList<Integer>> connect = new HashMap<Integer, ArrayList<Integer>>();
                for (int i = 0; i < friends.length; i++) {
                    ArrayList<Integer> list = new ArrayList<Integer>();
                    for (int j = i + 1; j < friends[i].length(); j++) {
                        if ('Y' == friends[i].charAt(j)) {
                            list.add(j);
                        }
                    }
                    connect.put(i, list);
                }
                
                ArrayList<HashSet<Integer>> circles = new ArrayList<HashSet<Integer>>();
                for (int i = 0; i < friends.length; i ++) {
                    if (all.contains(i)) {
                        all.remove(i);
                        HashSet<Integer> circle = new HashSet<Integer>();
                        circle.add(i);
                        ArrayList<Integer> list = connect.get(i);
                        while (!list.isEmpty()) {
                            if (all.contains(list.get(0))) {
                                all.remove(list.get(0));
                                list.addAll(connect.get(list.get(0)));
                                circle.add(list.get(0));
                                list.remove(0);
                            }else 
                                list.remove(0);
                        }
                        
                        circles.add(circle);
                    }
                }
                
                return circles.size();
             
            }
            
            public static void main(String[] args) {
                    FriendCircle sol = new FriendCircle();
                    String[] friends = {"YYY", "YYY", "YYY"};
                    System.out.println(sol.friendCircles(friends));
            }
}