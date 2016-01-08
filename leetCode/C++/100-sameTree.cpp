#include <iostream>
#include <queue>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution1 {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q)
            return true;
        else if (p && q && p->val == q->val)
            return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        else
            return false;
    }
};

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        queue<TreeNode*> pqueue;
        queue<TreeNode*> qqueue;

        pqueue.push(p);
        qqueue.push(q);

        while (!pqueue.empty() && !qqueue.empty()) {
            TreeNode *p = pqueue.front();
            TreeNode *q = qqueue.front();

            pqueue.pop();
            qqueue.pop();

            if (!p && !q)
                continue;
            else if (p && q && (p->val == q->val)) {
                pqueue.push(p->left);
                qqueue.push(q->left);
                pqueue.push(p->right);
                qqueue.push(q->right);
            }
            else
                return false;
        }
        return pqueue.empty() && qqueue.empty();
    }
};

int main(int argc, char *argv []){
    Solution s;
    TreeNode t1 = TreeNode(0);
    TreeNode t2 = TreeNode(1);
    std::cout << s.isSameTree(&t1, &t2) << std::endl;
};