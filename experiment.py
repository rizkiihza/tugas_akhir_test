import json 
import redis

from constant import REDIS_KEY

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

        self.add_to_redis(result)
        
    def add_to_redis(self, data):
        redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)
        json_value = redis_db.get(REDIS_KEY)

        if json_value is None:
            result = []
        else:
            result = json.loads(json_value)

        result.append(data)

        json_value = json.dumps(result)
        redis_db.set(REDIS_KEY, json_value)
        



