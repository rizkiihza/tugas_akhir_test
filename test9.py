from experiment import Experiment
from random import randint

experiment = Experiment()

class Graph(object):
    def __init__(self, n):
        self.n = n
        self.edges = [set() for _ in range(self.n+1)]

    def add_edge(self, n1, n2):
        if n1 > self.n:
            experiment.flag("n1 > self.n")
            return
        experiment.flag("n1 <= self.n")

        if n2 > self.n:
            experiment.flag("n2 > self.n")
            return
        experiment.flag("n2 <= self.n")

        self.edges[n1].add(n2)
        self.edges[n2].add(n1)

    def search(self, n1, n2):
        self.visited = [False for _ in range(self.n+1)]
        return self.search_recurs(n1, n2)

    def search_recurs(self, current, end):
        if current == end:
            experiment.flag("current == end")
            return True
        experiment.flag("current != end")

        self.visited[current] = True
        self.found = False

        for i in range(n1):
            if len(self.edges[current]) > i:
                experiment.flag("edges[current] > %d" % i)
            else:
                experiment.flag("edges[current] <= %d" % i)

        for neighbour in list(self.edges[current])[:2]:
            if not self.visited[neighbour]:
                experiment.flag("not visited[neighbour]")
                self.found = self.found or self.search_recurs(neighbour, end)
            else:
                experiment.flag("visited[neighbour]")

        if self.found:
            experiment.flag("found == True")
        else:
            experiment.flag("found == False")
        return self.found

if __name__ == '__main__':

    n = int(input("num : "))
    
    for i in range(n):
        label = randint(0, 1)

        if label == 0:
            n1 = randint(50, 100)

            graph1 = Graph(n1)
            start = 20
            edges = []

            for i in range(n1+1):
                edges.append((start, i))

            label = -1
        else:
            n1 = randint(50, 100)

            graph1 = Graph(n1)
            start = 20

            edges = []

            for i in range(n1):
                edges.append((i, i + 1))
            

        print(label)
        experiment.start_experiment(label)
        

        for edge in edges:
            graph1.add_edge(edge[0], edge[1])

        res = graph1.search(start, n1)
        print(res)
        print()

        experiment.end_experiment()