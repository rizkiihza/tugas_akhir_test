from experiment import Experiment
from random import randint
from math import inf

import random

experiment = Experiment()

class MinHeap(object):
    def __init__(self, size):
        self.size = size
        self.arr = [inf for _ in range(size)]
        self.fill = 0

    def parent(self, idx):
        return (idx - 1) // 2

    def right(self, idx):
        return 2 * idx + 2
    def left(self, idx):
        return 2 * idx + 1

    def insert(self, val):
        if self.fill == self.size:
            experiment.flag("fill == size")
            return
        experiment.flag("fill < size")
    
        self.arr[self.fill] = val
        self.heapify(self.fill)
        self.fill += 1
    

    def heapify(self, idx):
        if idx == 0:
            experiment.flag("idx == 0")
            return
        experiment.flag("idx != 0")
        while self.arr[idx] < self.arr[self.parent(idx)]:
            if idx == 0:
                experiment.flag("while: idx == 0")
                break
            else:
                experiment.flag("while: idx != 0")
                self.arr[idx], self.arr[self.parent(idx)] = self.arr[self.parent(idx)], self.arr[idx]
                idx = self.parent(idx)
        
        
        
        
    def pop(self):
        if self.fill == 0:
            experiment.flag("fill == 0")
            return None
        experiment.flag("fill != 0")

        result = self.arr[0]
        self.arr[0] = inf

        self.heapify_pop()
        self.fill -= 1
        return result

    def heapify_pop(self):
        idx = 0
        while True:
            left, right = self.left(idx), self.right(idx)
            if left >= self.size and right >= self.size:
                experiment.flag("left >= size and right >= size")
                break
            
            
            elif right >= self.size:
                experiment.flag("left < size or right < size")
                experiment.flag("right >= size")
                if self.arr[idx] > self.arr[left]:    
                    experiment.flag("right >= size and arr[idx] > arr[left]")
                    self.arr[idx], self.arr[left] = self.arr[left], self.arr[idx]
                    idx = left
                else:
                    experiment.flag("right >= size and arr[idx] <= arr[left]")
                    break
            
            elif self.arr[idx] <= self.arr[left] and self.arr[idx] <= self.arr[right]:
                experiment.flag("arr[idx] <= arr[left] and arr[idx] <= arr[right]")
                break
            else:
                experiment.flag("arr[idx] < arr[left] or arr[idx] < arr[right]")
                min_idx = left if self.arr[left] < self.arr[right] else right

                self.arr[idx], self.arr[min_idx] = self.arr[min_idx], self.arr[idx]
                idx = min_idx
        
if __name__ == '__main__':
    n = int(input("num : "))
    
    for i in range(n):
        label = randint(0, 1)

        if label == 0:
            n1 = randint(50, 100)

            arr = [i for i in range(n1)]
            arr = sorted(arr, reverse = True)
            
            label = -1
        else:
            n1 = randint(50, 100)

            arr = [i for i in range(n1)]
            arr = sorted(arr)

        print(label)
        experiment.start_experiment(label)
        
        heap = MinHeap(n1)

        for val in arr:
            heap.insert(val)

        result = []

        while True:
            front = heap.pop()
            if front is None:
                break
            result.append(front)

        experiment.end_experiment()