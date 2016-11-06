class UnionFind {
    private int[] father;
    private int count;
    public UnionFind(int n) {
        father = new int[n];
        count = n;
        for (int i = 0; i < n; i++){
            father[i] = i;
        }
    }
    public int count() {
        return this.count;
    }
    public int find(int p) {
        System.out.println("p " + p);
        int root = father[p];
        System.out.println("root " + root);
        while (root != father[root])
            root = father[root];
        //as long as we get here, root is the final dad
        System.out.println("finally root " + root);
        while (p != root) {
            int tmp = father[p];
            father[p] = root;
            p = tmp;
        }
        System.out.print("find [");
        for(int i = 0; i < father.length; i++) {
            System.out.print(" " + father[i]);
        }
        System.out.println(" ] ");
        System.out.println("** find result " + root);
        return root;
    }
    public void union(int p, int q) {
        int fatherP = find(p);
        int fatherQ = find(q);
        if (fatherP != fatherQ) {
            father[fatherP] = fatherQ;
            count--;
        }
        System.out.print("union [");
        for(int i = 0; i < father.length; i++) {
            System.out.print(" " + father[i]);
        }
        System.out.println("]\n==============\n");
    }
}

public class ValidTree {
    public static void main(String[] args) {
        int[][] edges1 = {{0, 1}, {0, 2}, {0, 3}, {1, 4}};
        System.out.println(validTree(5, edges1));
        System.out.println("==========================================");
        // int[][] edges2 = {{0, 1}, {0, 2}, {0, 3}, {1, 4}};
        int[][] edges2 = {{0, 1}, {0, 2}, {1, 2}};
        System.out.println(validTree(3, edges2));
    }
    public static boolean validTree(int n, int[][] edges) {
        UnionFind uf = new UnionFind(n);
        for (int[] edge : edges){
            System.out.print("edge [" + edge[0] + " " + edge[1] + "]\n");
            int p = edge[0];
            int q = edge[1];
            if (uf.find(p) == uf.find(q))
                return false;
            else
                uf.union(p,q);
        }

        return uf.count() == 1;
    }
}