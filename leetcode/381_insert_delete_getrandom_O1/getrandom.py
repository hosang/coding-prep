from collections import defaultdict
from random import randrange

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.val_to_idx = defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        idx = len(self.nums)
        self.nums.append(val)
        new_val = val not in self.val_to_idx or len(self.val_to_idx[val]) == 0
        self.val_to_idx[val].add(idx)
        return new_val

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        last = len(self.nums) - 1
        if val not in self.val_to_idx or len(self.val_to_idx[val]) == 0:
            return False
        idx = self.val_to_idx[val].pop()
        if idx != last:
            self.nums[idx] = self.nums[last]
            bk = self.val_to_idx[self.nums[idx]]
            bk.remove(last)
            bk.add(idx)
        self.nums.pop()
        return True
        
    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.nums[randrange(len(self.nums))]
