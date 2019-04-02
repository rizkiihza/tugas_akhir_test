from experiment import Experiment
from random import randint

experiment = Experiment()
  
class Solution():
    def _lis(self, arr , n ): 
    
        # Base Case 
        if n == 1 : 
            experiment.flag("n == 1")
            return 1
    
        else: 
            experiment.flag("n != 1")

        # maxEndingHere is the length of LIS ending with arr[n-1] 
        maxEndingHere = 0
    
        """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2] 
        IF arr[n-1] is maller than arr[n-1], and max ending with 
        arr[n-1] needs to be updated, then update it"""
        for i in range(1, n): 
            res = self._lis(arr , i) 
            if arr[i-1] < arr[n-1] and res+1 > maxEndingHere: 
                experiment.flag("arr[i-1] < arr[n-1] and res + 1 > maxEndingHere")
                maxEndingHere = res +1
            else:
                experiment.flag("arr[i-1] >= arr[n-1] or res + 1 <= maxEndingHere")
    
        # Compare maxEndingHere with overall maximum. And 
        # update the overall maximum if needed 
        if self.maximum > maxEndingHere:
            experiment.flag("self.maximum > maxEndingHere")
        else:
            experiment.flag("self.maximum <= maxEndingHere")

        self.maximum = max(self.maximum , maxEndingHere) 
    
        return maxEndingHere 
    
    def lis(self, arr): 
    
        # lenght of arr 
        n = len(arr) 
    
        # maximum variable holds the result 
        self.maximum = 0
    
        # The function _lis() stores its result in maximum 
        self._lis(arr , n) 
        
        if self.maximum > 0:
            experiment.flag("self.maximum > 0")
        else:
            experiment.flag("self.maximum == 0")

        return self.maximum 

if __name__ == '__main__':
    n = int(input("num : "))
    
    for i in range(n):
        label = randint(0, 1)

        if label == 0:
            n1 = randint(5, 10)

            nums1 = []

            start = randint(1, 60)
            for i in range(n1):
                nums1.append(start - i)

            label = -1
        else:
            n1 = randint(5, 10)

            nums1 = []

            start = randint(1, 3)
            for i in range(n1):
                nums1.append(start + i)

        print(label)
        experiment.start_experiment(label)
        
        Solution().lis(nums1)

        experiment.end_experiment()