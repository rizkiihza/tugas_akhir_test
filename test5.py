from experiment import Experiment
from random import randint

experiment = Experiment()

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        num_dict= {}
        
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            experiment.flag("n1 > n2")
        elif n1 < n2:
            experiment.flag("n1 < n2")
        else:
            experiment.flag("n1 = n2")

        for i in nums1:
            if i not in num_dict:
                experiment.flag("%d not in num_dict" % (i))
                num_dict[i]=1
            else:
                experiment.flag("%d in num_dict" % (i))
                num_dict[i]+=0
                
        #print num_dict
        
        for j in nums2:
            if j in num_dict and num_dict[j]>0:
                experiment.flag("%d in num_dict and num_dict[%d]>0" % (j, j))
                num_dict[j]-=1
                ans.append(j)
            else:
                experiment.flag("%d not in num_dict or num_dict[%d] <= 0" % (j, j))
        
        return ans

if __name__ == '__main__':
    n = int(input("num : "))
    
    for i in range(n):
        label = randint(0, 1)

        if label == 0:
            n1 = randint(5, 10)
            n2 = randint(5, 10)

            nums1 = []
            nums2 = []

            start = randint(30, 60)
            for i in range(n1):
                nums1.append(start + i // 2)

            for i in range(n2):
                nums2.append(2 + start + i // 2)

            label = -1
        else:
            n1 = randint(5, 10)
            n2 = randint(5, 10)

            nums1 = []
            nums2 = []

            start = randint(30, 60)
            for i in range(n1):
                nums1.append(start + i)

            for i in range(n2):
                nums2.append(2 + start + i)

        print(label)
        experiment.start_experiment(label)
        
        Solution().intersect(nums1, nums2)

        experiment.end_experiment()