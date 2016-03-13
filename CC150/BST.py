'''
I take the reference from this website:
http://www.laurentluce.com/posts/binary-search-tree-library-in-python/
'''

class TreeNode(object):
    def __init__(self, val):
        self.val   = val
        self.left  = None
        self.right = None

    def __repr__(self):
        return "Node with value: %d" % self.val

    def insert(self, new_val):
        if self.val is None:
            self.val = new_val
        else:
            if self.val > new_val:
                if self.left:
                    self.left.insert(new_val)
                else:
                    self.left = TreeNode(new_val)
            else:
                if self.right:
                    self.right.insert(new_val)
                else:
                    self.right = TreeNode(new_val)

    def search(self, target_val, parent=None): # return target node with target value & parent
        if self.val > target_val:
            if self.left is None: # cannot find the target value
                return None, None
            return self.left.search(target_val, self)
        elif self.val < target_val: # cannot find the target value
            if self.right is None:
                return None, None
            return self.right.search(target_val, self)
        else:
            return self, parent

    def children_count(self):
        children_count = 0
        if self.left:
            children_count += 1
        if self.right:
            children_count += 1
        return children_count

    def delete(self, delete_val):
        delete_node, parent = self.search(delete_val)
        if delete_node:
            children_count = delete_node.children_count()
            
            if children_count == 0:
                '''
                case 1:
                      parent_node
                        /    \
                    del_node  ...
                     /   \
                   None  None 

                In this case, we just need to make del_node = None & delete del_node
                '''
                if parent.left is delete_node:
                    parent.left = None
                else:
                    parent.right = None
                del delete_node

            elif children_count == 1:
                '''
                case 2:
                      parent_node
                        /    \
                    del_node  ...
                     /   \
                   child  None 

                   or 
                      parent_node
                        /    \
                    del_node  ...
                     /   \
                   None  child

                   or 
                   
                   parent_node
                     /    \
                   ...   del_node
                          /   \
                       child  None 

                   or 
                      parent_node
                        /    \
                      ...   del_node
                             /   \
                           None  child

                In this case, we make parent left node or right node become child, 
                then delete the del_node
                '''
                if delete_node.left:
                    child = delete_node.left
                else:
                    child = delete_node.right
                if parent:
                    if parent.left is delete_node:
                        parent.left = child
                    else:
                        parent.right = child
                del delete_node

            else:
                '''
                case 3:
                      parent_node
                        /    \
                      ...   del_node
                             /    \
                         child1  child2

                This is case the most complicated case, 

                '''
                parent = delete_node
                successor = dxelete_node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                delete_node.val = successor.val
                
                if parent.left is successor:
                    parent.left = successor.right
                elif parent.right is successor:
                    parent.right = successor.right




