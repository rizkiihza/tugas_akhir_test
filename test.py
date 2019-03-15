from experiment import Experiment

experiment = Experiment()

def modulo4(n):
    if n % 2 == 0:
        experiment.flag("n%2==0")
        if n % 4 == 0:
            experiment.flag("n%4==0")
            return 0
        if n % 4 == 2:
            experiment.flag("n%4==2")
            return 1
    if n % 2 == 1:
        experiment.flag("n%2==1")
        if n % 4 == 1:
            experiment.flag("n%4==1")
            return 1
        if n % 4 == 3:
            experiment.flag("n%4==3")
            return 3

if __name__ == '__main__':
    label = int(input("label: "))
    n = int(input("n: "))

    experiment.start_experiment(label)
    modulo4(n)
    experiment.end_experiment()
