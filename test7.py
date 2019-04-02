from experiment import Experiment
from random import randint

experiment = Experiment()

# Python3 program to to maximize  
# array sum after k operations. 
  
# This function does k operations on array 
# in a way that maximize the array sum. 
# index --> stores the index of current  
# minimum element for j'th operation 
def maximumSum(arr, n, k): 
    if arr is None:
        return 0
        experiment.flag("arr is None")
    else:
        experiment.flag("arr is not None")

    if k <= 0:
        experiment.flag("k <= 0")
    elif k > n:
        experiment.flag("k > n")
    else:
        experiment.flag("k <= n")

    # Modify array K number of times 
    for i in range(1, k + 1): 
      
        minimum = +2147483647
        index = -1
  
        # Find minimum element in array for 
        # current operation and modify it 
        # i.e; arr[j] --> -arr[j] 
        for j in range(n): 
          
            if arr[j] < minimum: 
                experiment.flag("arr[%d] < min" % (j))
                minimum = arr[j] 
                index = j 
  
        # this the condition if we find 0 as 
        # minimum element, so it will useless to 
        # replace 0 by -(0) for remaining operations 
        if minimum == 0: 
            experiment.flag("minimum = 0")
            break
        if minimum > 0:
            experiment.flag("minimum > 0")
        if minimum < 0:
            experiment.flag("minimum < 0")
      
  
    # Calculate sum of array 
    total_sum = 0
    for i in range(n): 
        total_sum += arr[i] 
    return total_sum
  
# Driver program 
if __name__ == '__main__':
    n = int(input("num : "))
    
    for i in range(n):
        label = randint(0, 1)

        if label == 0:
            n1 = randint(5, 10)

            nums1 = []

            start = randint(1,1)
            for i in range(n1):
                nums1.append(start - i)

            label = -1
        else:
            coin = randint(0, 1)
            if coin == 0:
                nums1 = None
            else:
                n1 = randint(5, 10)

                nums1 = []

                start = randint(1, 3)
                for i in range(n1):
                    nums1.append(start + i)

        print(label)
        experiment.start_experiment(label)
        
        if nums1 is None:
            maximumSum(nums1, 0, 20)
        else:
            maximumSum(nums1, len(nums1), 20)

        experiment.end_experiment()