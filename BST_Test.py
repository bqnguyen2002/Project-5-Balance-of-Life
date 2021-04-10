import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BST_Test(unittest.TestCase):
   
   def setUp(self):
      self.__bst = Binary_Search_Tree()
      
   #P5 TEST CASES:
         
   #| INSERTION BALANCE TEST CASES (INORDER, PREORDER, POSTORDER, TOLIST) |
   
   #tests different traversals of a simple binary search tree that requires a single rotation to the left after an insertion  
   def test_insertion_simple_leftrotation(self):
      self.__bst.insert_element(1)
      self.__bst.insert_element(2)
      self.__bst.insert_element(3)
      self.assertEqual('[ 1, 2, 3 ]', self.__bst.in_order())
      self.assertEqual( [1, 2, 3], self.__bst.to_list())
      self.assertEqual('[ 2, 1, 3 ]', self.__bst.pre_order())
      self.assertEqual('[ 1, 3, 2 ]', self.__bst.post_order())
      self.assertEqual(2, self.__bst.get_height())
      
   #tests different traversal of a complex binary search tree that requires a single rotation to the left an insertion   
   def test_insertion_complex_leftrotation(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(4)
      self.__bst.insert_element(3)
      self.__bst.insert_element(5)
      self.__bst.insert_element(6)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6 ]', self.__bst.in_order())
      self.assertEqual( [1, 2, 3, 4, 5, 6], self.__bst.to_list())
      self.assertEqual('[ 4, 2, 1, 3, 5, 6 ]', self.__bst.pre_order())
      self.assertEqual('[ 1, 3, 2, 6, 5, 4 ]', self.__bst.post_order())
      self.assertEqual(3, self.__bst.get_height())
      
   #tests different traversals of a simple binary search tree that requires a single rotation to the right after an insertion 
   def test_insertion_simple_rightrotation(self):
      self.__bst.insert_element(3)
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.assertEqual('[ 1, 2, 3 ]', self.__bst.in_order())
      self.assertEqual( [1, 2, 3], self.__bst.to_list())
      self.assertEqual('[ 2, 1, 3 ]', self.__bst.pre_order())
      self.assertEqual('[ 1, 3, 2 ]', self.__bst.post_order())
      self.assertEqual(2, self.__bst.get_height())
      
   #tests different traversal of a complex binary search tree that requires a single rotation to the right after an insertion   
   def test_insertion_complex_rightrotation(self):
      self.__bst.insert_element(5)
      self.__bst.insert_element(3)
      self.__bst.insert_element(6)
      self.__bst.insert_element(2)
      self.__bst.insert_element(4)
      self.__bst.insert_element(1)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6 ]', self.__bst.in_order())
      self.assertEqual( [1, 2, 3, 4, 5, 6], self.__bst.to_list())
      self.assertEqual('[ 3, 2, 1, 5, 4, 6 ]', self.__bst.pre_order())
      self.assertEqual('[ 1, 2, 4, 6, 5, 3 ]', self.__bst.post_order())
      self.assertEqual(3, self.__bst.get_height())
      
    #tests different traversals of a simple binary search tree requires that a double rotation (right then left) after an insertion 
   def test_insertion_simple_rightleftrotation(self):
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.insert_element(2)
      self.assertEqual('[ 1, 2, 3 ]', self.__bst.in_order())
      self.assertEqual( [1, 2, 3], self.__bst.to_list())
      self.assertEqual('[ 2, 1, 3 ]', self.__bst.pre_order())
      self.assertEqual('[ 1, 3, 2 ]', self.__bst.post_order())
      self.assertEqual(2, self.__bst.get_height())
      
   #tests different traversals of a complex binary search tree that requires a double rotation (right then left) after an insertion    
   def test_insertion_complex_rightleftrotation(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(9)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.insert_element(7)
      self.__bst.insert_element(10)
      self.__bst.insert_element(6)
      self.__bst.insert_element(8)
      self.__bst.insert_element(11)
      self.__bst.insert_element(5)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ]', self.__bst.in_order())
      self.assertEqual( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], self.__bst.to_list())
      self.assertEqual('[ 7, 4, 2, 1, 3, 6, 5, 9, 8, 10, 11 ]', self.__bst.pre_order())
      self.assertEqual('[ 1, 3, 2, 5, 6, 4, 8, 11, 10, 9, 7 ]', self.__bst.post_order())
      self.assertEqual(4, self.__bst.get_height())
      

   #tests different traversals of a simple binary search tree that requires a double rotation (left then right) after an insertion 
   def test_insertion_simple_leftrightrotation(self):
      self.__bst.insert_element(3)
      self.__bst.insert_element(1)
      self.__bst.insert_element(2)
      self.assertEqual('[ 1, 2, 3 ]', self.__bst.in_order())
      self.assertEqual( [1, 2, 3], self.__bst.to_list())
      self.assertEqual('[ 2, 1, 3 ]', self.__bst.pre_order())
      self.assertEqual('[ 1, 3, 2 ]', self.__bst.post_order())
      self.assertEqual(2, self.__bst.get_height())
      
   #tests different traversals of a complex binary search tree that requires a double rotation (left then right) after an insertion    
   def test_insertion_complex_leftrightrotation(self):
      self.__bst.insert_element(8)
      self.__bst.insert_element(3)
      self.__bst.insert_element(10)
      self.__bst.insert_element(2)
      self.__bst.insert_element(5)
      self.__bst.insert_element(9)
      self.__bst.insert_element(11)
      self.__bst.insert_element(1)
      self.__bst.insert_element(4)
      self.__bst.insert_element(6)
      self.__bst.insert_element(7)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ]', self.__bst.in_order())
      self.assertEqual( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], self.__bst.to_list())
      self.assertEqual('[ 5, 3, 2, 1, 4, 8, 6, 7, 10, 9, 11 ]', self.__bst.pre_order())
      self.assertEqual('[ 1, 2, 4, 3, 7, 6, 9, 11, 10, 8, 5 ]', self.__bst.post_order())
      self.assertEqual(4, self.__bst.get_height())
      
      
      
      
   #| REMOVAL BALANCE TEST CASES (INORDER, PREORDER, POSTORDER, TOLIST) (ONE ROTATION OPERATION) |   
      
   #tests different traversals of a simple binary search tree that requires a single rotation to the left after a removal  
   def test_removal_simple_leftrotation_one(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.insert_element(4)
      self.__bst.remove_element(1)
      self.assertEqual('[ 2, 3, 4 ]', self.__bst.in_order())
      self.assertEqual( [2, 3, 4], self.__bst.to_list())
      self.assertEqual('[ 3, 2, 4 ]', self.__bst.pre_order())
      self.assertEqual('[ 2, 4, 3 ]', self.__bst.post_order())
      self.assertEqual(2, self.__bst.get_height())
      
   #tests different traversal of a complex binary search tree that requires a single rotation to the left after a removal    
   def test_removal_complex_leftrotation_one(self):
      self.__bst.insert_element(3)
      self.__bst.insert_element(2)
      self.__bst.insert_element(5)
      self.__bst.insert_element(1)
      self.__bst.insert_element(4)
      self.__bst.insert_element(6)
      self.__bst.insert_element(7)
      self.__bst.remove_element(1)
      self.assertEqual('[ 2, 3, 4, 5, 6, 7 ]', self.__bst.in_order())
      self.assertEqual( [2, 3, 4, 5, 6, 7], self.__bst.to_list())
      self.assertEqual('[ 5, 3, 2, 4, 6, 7 ]', self.__bst.pre_order())
      self.assertEqual('[ 2, 4, 3, 7, 6, 5 ]', self.__bst.post_order())
      self.assertEqual(3, self.__bst.get_height())
      
   #tests different traversals of a simple binary search tree that requires a single rotation to the right after a removal
   def test_removal_simple_rightrotation_one(self):
      self.__bst.insert_element(3)
      self.__bst.insert_element(2)
      self.__bst.insert_element(4)
      self.__bst.insert_element(1)
      self.__bst.remove_element(4)
      self.assertEqual('[ 1, 2, 3 ]', self.__bst.in_order())
      self.assertEqual( [1, 2, 3], self.__bst.to_list())
      self.assertEqual('[ 2, 1, 3 ]', self.__bst.pre_order())
      self.assertEqual('[ 1, 3, 2 ]', self.__bst.post_order())
      self.assertEqual(2, self.__bst.get_height())
      
   #tests different traversal of a complex binary search tree that requires a single rotation to the right after a removal    
   def test_removal_complex_rightrotation_one(self):
      self.__bst.insert_element(5)
      self.__bst.insert_element(3)
      self.__bst.insert_element(7)
      self.__bst.insert_element(2)
      self.__bst.insert_element(4)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.remove_element(6)
      self.assertEqual('[ 1, 2, 3, 4, 5, 7 ]', self.__bst.in_order())
      self.assertEqual( [1, 2, 3, 4, 5, 7], self.__bst.to_list())
      self.assertEqual('[ 3, 2, 1, 5, 4, 7 ]', self.__bst.pre_order())
      self.assertEqual('[ 1, 2, 4, 7, 5, 3 ]', self.__bst.post_order())
      self.assertEqual(3, self.__bst.get_height())
      
    #tests different traversals of a simple binary search tree that requires a double rotation (right then left) after a removal
   def test_removal_simple_rightleftrotation_one(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(4)
      self.__bst.insert_element(3)
      self.__bst.remove_element(1)
      self.assertEqual('[ 2, 3, 4 ]', self.__bst.in_order())
      self.assertEqual( [2, 3, 4], self.__bst.to_list())
      self.assertEqual('[ 3, 2, 4 ]', self.__bst.pre_order())
      self.assertEqual('[ 2, 4, 3 ]', self.__bst.post_order())
      self.assertEqual(2, self.__bst.get_height())
      
   #tests different traversals of a complex binary search tree that requires a double rotation (right then left) after a removal   
   def test_removal_complex_rightleftrotation_one(self):
      self.__bst.insert_element(5)
      self.__bst.insert_element(3)
      self.__bst.insert_element(10)
      self.__bst.insert_element(1)
      self.__bst.insert_element(4)
      self.__bst.insert_element(8)
      self.__bst.insert_element(11)
      self.__bst.insert_element(2)
      self.__bst.insert_element(7)
      self.__bst.insert_element(9)
      self.__bst.insert_element(12)
      self.__bst.insert_element(6)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]', self.__bst.in_order())
      self.assertEqual( [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], self.__bst.to_list())
      self.assertEqual('[ 8, 5, 3, 1, 4, 7, 6, 10, 9, 11, 12 ]', self.__bst.pre_order())
      self.assertEqual('[ 1, 4, 3, 6, 7, 5, 9, 12, 11, 10, 8 ]', self.__bst.post_order())
      self.assertEqual(4, self.__bst.get_height())
      

   #tests different traversals of a simple binary search tree that requires a double rotation (left then right) after a removal 
   def test_removal_simple_leftrightrotation_one(self):
      self.__bst.insert_element(3)
      self.__bst.insert_element(1)
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.remove_element(4)
      self.assertEqual('[ 1, 2, 3 ]', self.__bst.in_order())
      self.assertEqual( [1, 2, 3], self.__bst.to_list())
      self.assertEqual('[ 2, 1, 3 ]', self.__bst.pre_order())
      self.assertEqual('[ 1, 3, 2 ]', self.__bst.post_order())
      self.assertEqual(2, self.__bst.get_height())
      
   #tests different traversals of a complex binary search tree that requires a double rotation (left then right) after a removal    
   def test_removal_complex_leftrightrotation_one(self):
      self.__bst.insert_element(8)
      self.__bst.insert_element(3)
      self.__bst.insert_element(11)
      self.__bst.insert_element(2)
      self.__bst.insert_element(5)
      self.__bst.insert_element(9)
      self.__bst.insert_element(12)
      self.__bst.insert_element(1)
      self.__bst.insert_element(4)
      self.__bst.insert_element(6)
      self.__bst.insert_element(10)
      self.__bst.insert_element(7)
      self.__bst.remove_element(10)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12 ]', self.__bst.in_order())
      self.assertEqual( [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12], self.__bst.to_list())
      self.assertEqual('[ 5, 3, 2, 1, 4, 8, 6, 7, 11, 9, 12 ]', self.__bst.pre_order())
      self.assertEqual('[ 1, 2, 4, 3, 7, 6, 9, 12, 11, 8, 5 ]', self.__bst.post_order())
      self.assertEqual(4, self.__bst.get_height())
      
      
      
   
   #| REMOVAL BALANCE TEST CASES (INORDER, PREORDER, POSTORDER, TOLIST) (TWO ROTATION OPERATIONS) |
   
   #tests different traversals of a binary search tree that requires two rotations (right case then left case) after a removal
   def test_removal_right_left_two(self):
      self.__bst.insert_element(5)
      self.__bst.insert_element(3)
      self.__bst.insert_element(8)
      self.__bst.insert_element(2)
      self.__bst.insert_element(4)
      self.__bst.insert_element(7)
      self.__bst.insert_element(10)
      self.__bst.insert_element(1)
      self.__bst.insert_element(6)
      self.__bst.insert_element(9)
      self.__bst.insert_element(11)
      self.__bst.insert_element(12)
      self.__bst.remove_element(4)
      self.assertEqual('[ 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12 ]', self.__bst.in_order())
      self.assertEqual( [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12], self.__bst.to_list())
      self.assertEqual('[ 8, 5, 2, 1, 3, 7, 6, 10, 9, 11, 12 ]', self.__bst.pre_order())
      self.assertEqual('[ 1, 3, 2, 6, 7, 5, 9, 12, 11, 10, 8 ]', self.__bst.post_order())
      self.assertEqual(4, self.__bst.get_height())
      
   #tests different traversals of a binary search tree that requires two rotations (left case then right case) after a removal
   def test_removal_left_right_two(self):
      self.__bst.insert_element(8)
      self.__bst.insert_element(5)
      self.__bst.insert_element(10)
      self.__bst.insert_element(3)
      self.__bst.insert_element(6)
      self.__bst.insert_element(9)
      self.__bst.insert_element(11)
      self.__bst.insert_element(2)
      self.__bst.insert_element(4)
      self.__bst.insert_element(7)
      self.__bst.insert_element(12)
      self.__bst.insert_element(1)
      self.__bst.remove_element(9)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12 ]', self.__bst.in_order())
      self.assertEqual( [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], self.__bst.to_list())
      self.assertEqual('[ 5, 3, 2, 1, 4, 8, 6, 7, 11, 10, 12 ]', self.__bst.pre_order())
      self.assertEqual('[ 1, 2, 4, 3, 7, 6, 10, 12, 11, 8, 5 ]', self.__bst.post_order())
      self.assertEqual(4, self.__bst.get_height())
      
   #tests different traversals of a binary search tree that requires two rotations (right case then right left case) after a removal
   def test_removal_right_rightleft_two(self):
      self.__bst.insert_element(5)
      self.__bst.insert_element(3)
      self.__bst.insert_element(10)
      self.__bst.insert_element(2)
      self.__bst.insert_element(4)
      self.__bst.insert_element(8)
      self.__bst.insert_element(12)
      self.__bst.insert_element(1)
      self.__bst.insert_element(6)
      self.__bst.insert_element(9)
      self.__bst.insert_element(11)
      self.__bst.insert_element(7)
      self.__bst.remove_element(4)
      self.assertEqual('[ 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12 ]', self.__bst.in_order())
      self.assertEqual( [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12], self.__bst.to_list())
      self.assertEqual('[ 8, 5, 2, 1, 3, 6, 7, 10, 9, 12, 11 ]', self.__bst.pre_order())
      self.assertEqual('[ 1, 3, 2, 7, 6, 5, 9, 11, 12, 10, 8 ]', self.__bst.post_order())
      self.assertEqual(4, self.__bst.get_height())
      
   #tests different traversals of a binary search tree that requires two rotations (left case then left right case) after a removal
   def test_removal_left_leftright_two(self):
      self.__bst.insert_element(8)
      self.__bst.insert_element(3)
      self.__bst.insert_element(10)
      self.__bst.insert_element(1)
      self.__bst.insert_element(5)
      self.__bst.insert_element(9)
      self.__bst.insert_element(11)
      self.__bst.insert_element(2)
      self.__bst.insert_element(4)
      self.__bst.insert_element(7)
      self.__bst.insert_element(12)
      self.__bst.insert_element(6)
      self.__bst.remove_element(9)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12 ]', self.__bst.in_order())
      self.assertEqual( [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], self.__bst.to_list())
      self.assertEqual('[ 5, 3, 1, 2, 4, 8, 7, 6, 11, 10, 12 ]', self.__bst.pre_order())
      self.assertEqual('[ 2, 1, 4, 3, 6, 7, 10, 12, 11, 8, 5 ]', self.__bst.post_order())
      self.assertEqual(4, self.__bst.get_height())
   
   #tests different traversals of a binary search tree that requires two rotations (right left case twice) after a removal
   def test_removal_rightleft_two(self):
      self.__bst.insert_element(5)
      self.__bst.insert_element(2)
      self.__bst.insert_element(10)
      self.__bst.insert_element(1)
      self.__bst.insert_element(4)
      self.__bst.insert_element(8)
      self.__bst.insert_element(12)
      self.__bst.insert_element(3)
      self.__bst.insert_element(6)
      self.__bst.insert_element(9)
      self.__bst.insert_element(11)
      self.__bst.insert_element(7)
      self.__bst.remove_element(1)
      self.assertEqual('[ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]', self.__bst.in_order())
      self.assertEqual( [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], self.__bst.to_list())
      self.assertEqual('[ 8, 5, 3, 2, 4, 6, 7, 10, 9, 12, 11 ]', self.__bst.pre_order())
      self.assertEqual('[ 2, 4, 3, 7, 6, 5, 9, 11, 12, 10, 8 ]', self.__bst.post_order())
      self.assertEqual(4, self.__bst.get_height())
      
   #tests different traversals of a binary search tree that requires two rotations (right left case then left case) after a removal
   def test_removal_rightleft_left_two(self):
      self.__bst.insert_element(5)
      self.__bst.insert_element(2)
      self.__bst.insert_element(8)
      self.__bst.insert_element(1)
      self.__bst.insert_element(4)
      self.__bst.insert_element(6)
      self.__bst.insert_element(10)
      self.__bst.insert_element(3)
      self.__bst.insert_element(7)
      self.__bst.insert_element(9)
      self.__bst.insert_element(12)
      self.__bst.insert_element(11)
      self.__bst.remove_element(1)
      self.assertEqual('[ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]', self.__bst.in_order())
      self.assertEqual( [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], self.__bst.to_list())
      self.assertEqual('[ 8, 5, 3, 2, 4, 6, 7, 10, 9, 12, 11 ]', self.__bst.pre_order())
      self.assertEqual('[ 2, 4, 3, 7, 6, 5, 9, 11, 12, 10, 8 ]', self.__bst.post_order())
      self.assertEqual(4, self.__bst.get_height())
      
      
   #tests different traversals of a binary search tree that requires two rotations (left right case twice) after a removal
   def test_removal_leftright_two(self):
      self.__bst.insert_element(8)
      self.__bst.insert_element(3)
      self.__bst.insert_element(11)
      self.__bst.insert_element(1)
      self.__bst.insert_element(5)
      self.__bst.insert_element(9)
      self.__bst.insert_element(12)
      self.__bst.insert_element(2)
      self.__bst.insert_element(4)
      self.__bst.insert_element(7)
      self.__bst.insert_element(10)
      self.__bst.insert_element(6)
      self.__bst.remove_element(12)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ]', self.__bst.in_order())
      self.assertEqual( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], self.__bst.to_list())
      self.assertEqual('[ 5, 3, 1, 2, 4, 8, 7, 6, 10, 9, 11 ]', self.__bst.pre_order())
      self.assertEqual('[ 2, 1, 4, 3, 6, 7, 9, 11, 10, 8, 5 ]', self.__bst.post_order())
      self.assertEqual(4, self.__bst.get_height())
      
   #tests different traversals of a binary search tree that requires two rotations (left right case then right case) after a removal
   def test_removal_leftright_right_two(self):
      self.__bst.insert_element(8)
      self.__bst.insert_element(5)
      self.__bst.insert_element(11)
      self.__bst.insert_element(3)
      self.__bst.insert_element(7)
      self.__bst.insert_element(9)
      self.__bst.insert_element(12)
      self.__bst.insert_element(1)
      self.__bst.insert_element(4)
      self.__bst.insert_element(6)
      self.__bst.insert_element(10)
      self.__bst.insert_element(2)
      self.__bst.remove_element(12)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ]', self.__bst.in_order())
      self.assertEqual( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], self.__bst.to_list())
      self.assertEqual('[ 5, 3, 1, 2, 4, 8, 7, 6, 10, 9, 11 ]', self.__bst.pre_order())
      self.assertEqual('[ 2, 1, 4, 3, 6, 7, 9, 11, 10, 8, 5 ]', self.__bst.post_order())
      self.assertEqual(4, self.__bst.get_height())
   
   
     
   #P4 TEST CASES:
   
   #_________RAISING ERRORS TEST CASES_____________
      
   #tests if value error is raised when value the same as the root is inserted    
   def test_insert_same_root_value_ignore(self):
      self.__bst.insert_element(1)
      with self.assertRaises(ValueError):
         self.__bst.insert_element(1)
      self.assertEqual('[ 1 ]', str(self.__bst))
      
   #tests if value error is raised when value the same as a leaf node is inserted  
   def test_insert_same_leaf_value_ignore(self):
      self.__bst.insert_element(3)
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      with self.assertRaises(ValueError):
         self.__bst.insert_element(1)
      self.assertEqual('[ 1, 2, 3 ]', str(self.__bst))
    
   #tests if value error is raised when value is removed from an empty binary search tree  
   def test_remove_empty_bst_ignore(self):
      with self.assertRaises(ValueError):
         self.__bst.remove_element(1)
      self.assertEqual('[ ]', str(self.__bst))
      
   #tests if value error is raised when value is removed that does not exist in a binary search tree with values in it 
   def test_remove_bst_ignore(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(1)
      self.__bst.insert_element(2)
      with self.assertRaises(ValueError):
         self.__bst.remove_element(3)
      self.assertEqual('[ 1, 2, 4 ]', str(self.__bst))
      
              
   #_________INSERTION TEST CASES (INORDER)_____________
   
   #tests in order traversal of an empty binary search tree
   def test_empty_bst_inorder(self):
      self.assertEqual('[ ]', self.__bst.in_order())
   
   #tests in order traversal of a binary search tree after 1 value has been inserted into it   
   def test_insert_1_bst_inorder(self):
      self.__bst.insert_element(1)
      self.assertEqual('[ 1 ]', self.__bst.in_order())
      
   #tests in order traversal of a binary search tree after 3 values have been inserted into it   
   def test_insert_3_bst_inorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.assertEqual('[ 1, 2, 3 ]', self.__bst.in_order())
      
   #tests in order traversal of a binary search tree after 7 values have been inserted into it   
   def test_insert_7_bst_inorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.insert_element(5)
      self.__bst.insert_element(7)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7 ]', self.__bst.in_order())
  
  
           
   #_________INSERTION TEST CASES (PREORDER)_____________
   
   #tests pre order traversal of an empty binary search tree
   def test_empty_bst_preorder(self):
      self.assertEqual('[ ]', self.__bst.pre_order())
   
   #tests pre order traversal of a binary search tree after 1 value has been inserted into it   
   def test_insert_1_bst_preorder(self):
      self.__bst.insert_element(1)
      self.assertEqual('[ 1 ]', self.__bst.pre_order())
      
   #tests pre order traversal of a binary search tree after 3 values have been inserted into it   
   def test_insert_3_bst_preorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.assertEqual('[ 2, 1, 3 ]', self.__bst.pre_order())
      
   #tests pre order traversal of a binary search tree after 7 values have been inserted into it   
   def test_insert_7_bst_preorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.insert_element(5)
      self.__bst.insert_element(7)
      self.assertEqual('[ 4, 2, 1, 3, 6, 5, 7 ]', self.__bst.pre_order())
   
   
   
   #_________INSERTION TEST CASES (POSTORDER)_____________
   
   #tests post order traversal of an empty binary search tree
   def test_empty_bst_postorder(self):
      self.assertEqual('[ ]', self.__bst.post_order())
   
   #tests post order traversal of a binary search tree after 1 value has been inserted into it   
   def test_insert_1_bst_postorder(self):
      self.__bst.insert_element(1)
      self.assertEqual('[ 1 ]', self.__bst.post_order())
      
   #tests post order traversal of a binary search tree after 3 values have been inserted into it   
   def test_insert_3_bst_postorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.assertEqual('[ 1, 3, 2 ]', self.__bst.post_order())
      
   #tests post order traversal of a binary search tree after 7 values have been inserted into it   
   def test_insert_7_bst_postorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.insert_element(5)
      self.__bst.insert_element(7)
      self.assertEqual('[ 1, 3, 2, 5, 7, 6, 4 ]', self.__bst.post_order())
      
      
    
   #_________GET HEIGHT TEST CASES_____________
    
   #tests height of an empty binary search tree
   def test_empty_bst_height(self):
      self.assertEqual(0, self.__bst.get_height())
      
   #tests height of a binary search tree with 1 value inserted into it
   def test_insert_1_bst_height(self):
      self.__bst.insert_element(1)
      self.assertEqual(1, self.__bst.get_height())
      
   #tests height of a binary search tree with 3 values inserted into it on the left side
   def test_insert_3_bst_left_height(self):
      self.__bst.insert_element(3)
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.assertEqual(2, self.__bst.get_height())
   
   #tests height of a binary search tree with 3 values inserted into it on the right side
   def test_insert_3_bst_right_height(self):
      self.__bst.insert_element(1)
      self.__bst.insert_element(2)
      self.__bst.insert_element(3)
      self.assertEqual(2, self.__bst.get_height())
      
   #tests height of a binary search tree with 3 values inserted into it 
   def test_insert_3_bst_height(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.assertEqual(2, self.__bst.get_height())
      
   #tests height of a binary search tree with 5 values inserted into it 
   def test_insert_5_bst_height(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.assertEqual(3, self.__bst.get_height())
      
   #tests height of a binary search tree after removing a node with no children   
   def test_0_children_bst_remove_height(self):
      self.__bst.insert_element(1)
      self.__bst.remove_element(1)
      self.assertEqual(0, self.__bst.get_height())
      
   #tests height of a binary search after removing a node with 1 child on its left
   def test_1_left_child_bst_remove_height(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.remove_element(2)
      self.assertEqual(1, self.__bst.get_height())
      
   #tests height of a binary search after removing a node with 1 child on its right
   def test_1_right_child_bst_remove_height(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.remove_element(2)
      self.assertEqual(1, self.__bst.get_height())
      
   #tests height of a binary search after removing a node with 2 children
   def test_2_children_bst_remove_height(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual(2, self.__bst.get_height())
      
   
   #_________REMOVE TEST CASES (INORDER)_____________
   
   #tests in order traversal of a binary search tree that has its root value removed when it has no children   
   def test_0_children_bst_remove_root_inorder(self):
      self.__bst.insert_element(1)
      self.__bst.remove_element(1)
      self.assertEqual('[ ]', self.__bst.in_order())
      
   #tests in order traversal of a binary search tree that has its root value removed when it has 1 child on its left
   def test_1_left_child_bst_remove_root_inorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1 ]', self.__bst.in_order())
      
   #tests in order traversal of a binary search tree that has its root value removed when it has 1 child on its right
   def test_1_right_child_bst_remove_root_inorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual('[ 3 ]', self.__bst.in_order())
      
   #tests in order traversal of a binary search tree that has its root value removed when it has 2 children  
   def test_2_children_bst_remove_root_inorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1, 3 ]', self.__bst.in_order())
      
   #tests in order traversal of a binary search tree that has a non-root value removed when it has no children   
   def test_0_children_bst_remove_nonroot_inorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.remove_element(1)
      self.assertEqual('[ 2, 4, 6 ]', self.__bst.in_order())
      
   #tests in order traversal of a binary search tree that has a non-root value removed when it has 1 child on its left
   def test_1_left_child_bst_remove_nonroot_inorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1, 4, 6 ]', self.__bst.in_order())
      
   #tests in order traversal of a binary search tree that has a non-root value removed when it has 1 child on its right
   def test_1_right_child_bst_remove_nonroot_inorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(7)
      self.__bst.remove_element(6)
      self.assertEqual('[ 2, 4, 7 ]', self.__bst.in_order())
      
   #tests in order traversal of a binary search tree that has a non-root value removed when it has 2 children  
   def test_2_children_bst_remove_nonroot_inorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1, 3, 4, 6 ]', self.__bst.in_order())
      
      
      
   #_________REMOVE TEST CASES (PREORDER)_____________
   
   #tests pre order traversal of a binary search tree that has its root value removed when it has no children   
   def test_0_children_bst_remove_root_preorder(self):
      self.__bst.insert_element(1)
      self.__bst.remove_element(1)
      self.assertEqual('[ ]', self.__bst.pre_order())
      
   #tests pre order traversal of a binary search tree that has its root value removed when it has 1 child on its left
   def test_1_left_child_bst_remove_root_preorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1 ]', self.__bst.pre_order())
      
   #tests pre order traversal of a binary search tree that has its root value removed when it has 1 child on its right
   def test_1_right_child_bst_remove_root_preorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual('[ 3 ]', self.__bst.pre_order())
      
   #tests pre order traversal of a binary search tree that has its root value removed when it has 2 children  
   def test_2_children_bst_remove__root_preorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual('[ 3, 1 ]', self.__bst.pre_order())
      
   #tests pre order traversal of a binary search tree that has a non-root value removed when it has no children   
   def test_0_children_bst_remove_nonroot_preorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.remove_element(1)
      self.assertEqual('[ 4, 2, 6 ]', self.__bst.pre_order())
      
   #tests pre order traversal of a binary search tree that has a non-root value removed when it has 1 child on its left
   def test_1_left_child_bst_remove_nonroot_preorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.remove_element(2)
      self.assertEqual('[ 4, 1, 6 ]', self.__bst.pre_order())
      
   #tests pre order traversal of a binary search tree that has a non-root value removed when it has 1 child on its right
   def test_1_right_child_bst_remove_nonroot_preorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(7)
      self.__bst.remove_element(6)
      self.assertEqual('[ 4, 2, 7 ]', self.__bst.pre_order())
      
   #tests pre order traversal of a binary search tree that has a non-root value removed when it has 2 children  
   def test_2_children_bst_remove_nonroot_preorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual('[ 4, 3, 1, 6 ]', self.__bst.pre_order())
      
      
      
   #_________REMOVE TEST CASES (POSTORDER)_____________
   
   #tests pre order traversal of a binary search tree that has its root value removed when it has no children   
   def test_0_children_bst_remove_root_postorder(self):
      self.__bst.insert_element(1)
      self.__bst.remove_element(1)
      self.assertEqual('[ ]', self.__bst.post_order())
      
   #tests post order traversal of a binary search tree that has its root value removed when it has 1 child on its left
   def test_1_left_child_order_bst_remove_root_postorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1 ]', self.__bst.post_order())
      
   #tests post order traversal of a binary search tree that has its root value removed when it has 1 child on its right
   def test_1_right_child_order_bst_remove_root_postorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual('[ 3 ]', self.__bst.post_order())
      
   #tests post order traversal of a binary search tree that has its root value removed when it has 2 children  
   def test_2_children_bst_remove_root_postorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1, 3 ]', self.__bst.post_order())
      
   #tests post order traversal of a binary search tree that has a non-root value removed when it has no children   
   def test_0_children_bst_remove_nonroot_postorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.remove_element(1)
      self.assertEqual('[ 2, 6, 4 ]', self.__bst.post_order())
      
   #tests post order traversal of a binary search tree that has a non-root value removed when it has 1 child on its left
   def test_1_left_child_bst_remove_nonroot_postorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1, 6, 4 ]', self.__bst.post_order())
      
   #tests post order traversal of a binary search tree that has a non-root value removed when it has 1 child on its right
   def test_1_right_child_bst_remove_nonroot_postorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(7)
      self.__bst.remove_element(6)
      self.assertEqual('[ 2, 7, 4 ]', self.__bst.post_order())
      
   #tests post order traversal of a binary search tree that has a non-root value removed when it has 2 children  
   def test_2_children_bst_remove_nonroot_postorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1, 3, 6, 4 ]', self.__bst.post_order())
           
if __name__ == '__main__':
   unittest.main()
