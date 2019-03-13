import json
import redis 

from constant import REDIS_KEY

class Compiler(object):
    @staticmethod
    def process_data():
        data = Compiler.read_data_from_redis()
        
        predicates = Compiler.list_all_predicates(data)

        data = Compiler.convert_predicates_to_set(data)

        compiled_data = Compiler.get_compiled_data(data, predicates)
        return compiled_data

    @staticmethod
    def read_data_from_redis():
        redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)

        json_value = redis_db.get(REDIS_KEY)

        return json.loads(json_value)

    @staticmethod
    def list_all_predicates(data):
        predicate_set = set()

        for elem in data:
            for predicate in elem["predicates"]:
                predicate_set.add(predicate)
        

        return list(predicate_set)


    @staticmethod
    def convert_predicates_to_set(data):
        for elem in data:
            elem["predicates"] = set(elem["predicates"])


    @staticmethod
    def get_compiled_data(data, predicates):
        predicate_id_dict = Compiler.get_predicate_id_dictionary(predicates)

        num_of_predicates = len(predicates)

        compiled_data = {}

        for i in range(len(data)):
            compiled_data.append([0 for _ in range(num_of_predicates)])
            elem = data[i]
            for predicate in elem["predicates"]:
                predicate_id = predicate_id_dict[predicate]
                compiled_data[i][predicate_id] = 1

            compiled_data[i].append(elem["label"])

        return compiled_data

    @staticmethod
    def get_predicate_id_dictionary(predicates):
        current = 0
        predicate_id_dictionary = {}

        for predicate in predicates:
            predicate_id_dictionary[predicate] = current
            current += 1

        return predicate_id_dictionary
