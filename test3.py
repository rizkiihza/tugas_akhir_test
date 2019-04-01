from experiment import Experiment

from random import randint

experiment = Experiment()

class BST:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def __str__(self):
        return "[%s, %s, %s]" % (self.left, str(self.val), self.right)

    def isEmpty(self):
        if self.left is None:
            experiment.flag("isEmpty: self.left is None")
        if self.right is None:
            experiment.flag("isEmpty: self.right is None")
        if self.val is None:
            experiment.flag("isEmpty: self.val is None")
        return self.left == self.right == self.val == None

    def insert(self, val):
        if self.isEmpty():
            experiment.flag("insert: isEmpty")
            self.val = val
        elif val < self.val:
            experiment.flag("insert: val < self.val")
            if self.left is None:
                experiment.flag("insert: val < self.val and self.left is None")
                self.left = BST(val)
            else:
                experiment.flag("insert: val < self.val and self.left is not None")
                self.left.insert(val)
        else:
            experiment.flag("insert: val >= self.val")
            if self.right is None:
                experiment.flag("insert: val >= self.val and self.right is None")
                # self.right = BST(val)
            else:
                experiment.flag("insert: val >= self.val and self.right is not None")
                self.right.insert(val)

if __name__ == '__main__':
    n = int(input("num : "))
    
    for i in range(n):
        label = randint(0, 1)

        if label == 0:
            num = randint(5, 100)
            start = randint(100, 200)

            nums = []

            for i in range(num):
                nums.append(start + i)

            label = -1
        else:
            num = randint(5, 100)
            start = randint(100, 200)

            nums = []

            for i in range(num):
                nums.append(start - i)
        print(label)
        bst = BST()
        experiment.start_experiment(label)
        
        for val in nums:
            bst.insert(val)

        experiment.end_experiment()