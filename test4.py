from experiment import Experiment
from random import randint

experiment = Experiment()

def lcs(X, Y): 
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
  
    if m > n:
        experiment.flag("m > n")
    elif m < n:
        experiment.flag("m < n")
    else:
        experiment.flag("m == n")

    # declaring the array for storing the dp values 
    L = [[None for _ in range(n+1)] for _ in range(m + 1)] 
  
    """Following steps build L[m + 1][n + 1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m + 1): 
        for j in range(n + 1):
            if i > j: 
                experiment.flag("i > j")
            elif i < j:
                experiment.flag("i < j")
            else:
                experiment.flag("i == j")

            if i == 0 or j == 0:
                experiment.flag("i == 0 or j == 0")
                if i == 0:
                    experiment.flag("i == 0")
                if j == 0:
                    experiment.flag("j == 0")
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                experiment.flag("X[i-1] == Y[j-1] equal")
                L[i][j] = L[i-1][j-1]+1
            else: 
                experiment.flag("X[i-1] != Y[j-1] not equal")
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[m][n] 

if __name__ == '__main__':
    n = int(input("num : "))
    
    for i in range(n):
        label = randint(0, 1)

        if label == 0:
            num1 = randint(5, 10)
            num2 = randint(5, 10)

            s1 = []
            s2 = []

            for i in range(num1):
                s1.append(chr(randint(50, 120)))

            for i in range(num2):
                if i < num1:
                    s2.append(s1[i])
                else:
                    s2.append(chr(randint(50, 120)))

            label = -1
            s1 = "".join(s1)
            s2 = "".join(s2)
        else:
            num1 = randint(5, 100)
            num2 = randint(5, 100)

            s1 = []
            s2 = []

            for i in range(num1):
                s1.append(chr(randint(50, 120)))

            while len(s2) < num2:
                c = chr(randint(50, 120))
                if c in s1:
                    continue
                else:
                    s2.append(c)
            
            s1 = "".join(s1)
            s2 = "".join(s2)

        print(label)
        experiment.start_experiment(label)
        
        lcs(s1, s2)

        experiment.end_experiment()