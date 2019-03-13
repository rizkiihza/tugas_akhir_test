import json 

class Experiment(object):

    def start_experiment(self, label):
        self.label
        self.predicate_set = set()

    def flag(self, predicate):
        self.predicate_set.add(predicate)

    def end_experiment(self):
        result = {}

        result["label"] = self.label
        result["predicates"] = []

        for predicate in self.predicate_set:
            result["predicates"].append(predicate)



