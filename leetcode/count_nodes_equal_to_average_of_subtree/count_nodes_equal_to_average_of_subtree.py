from typing import Optional


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def post_order(node):
            if node == None :
                return (0, 0, 0)
            
            summ_subtree  , tot             = node.val, 1 
            summ_subtree_l, tot_l, ans_l    = post_order(node.left) 
            summ_subtree_r, tot_r, ans_r    = post_order(node.right)
            
            summ_subtree += summ_subtree_l + summ_subtree_r
            tot          += tot_l + tot_r
            ans           = ans_l + ans_r
            
            if node.val == summ_subtree // tot:
                ans += 1
                
            return (summ_subtree, tot, ans)
                
        return post_order(root)[2]