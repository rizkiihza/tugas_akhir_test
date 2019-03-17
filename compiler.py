import json
import redis 

from constant import REDIS_KEY

class Compiler(object):

    @staticmethod
    def process_data():
        data = Compiler.read_data_from_redis()

        if data is None:
            return None, None
        
        predicates = Compiler.list_all_predicates(data)

        data = Compiler.convert_predicates_to_set(data)
    
        compiled_data, predicate_id_dict = Compiler.get_compiled_data_and_predicate_dict(data, predicates)

        return compiled_data, predicate_id_dict

    @staticmethod
    def read_data_from_redis():
        redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)

        json_value = redis_db.get(REDIS_KEY)

        return None if json_value is None else json.loads(json_value)

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
        return data


    @staticmethod
    def get_compiled_data_and_predicate_dict(data, predicates):
        predicate_id_dict = Compiler.get_predicate_id_dictionary(predicates)

        num_of_predicates = len(predicates)

        compiled_data = {}

        for i in range(len(data)):
            compiled_data[i] = [0 for _ in range(num_of_predicates)]
            elem = data[i]
            for predicate in elem["predicates"]:
                predicate_id = predicate_id_dict[predicate]
                compiled_data[i][predicate_id-1] = 1

            compiled_data[i].append(elem["label"])

        return compiled_data, predicate_id_dict

    @staticmethod
    def get_predicate_id_dictionary(predicates):
        current = 1
        predicate_id_dictionary = {}

        for predicate in predicates:
            predicate_id_dictionary[predicate] = current
            current += 1

        return predicate_id_dictionary

    @staticmethod
    def write_dictionary_to_file(dictionary, filename):
        with open(filename, 'w') as out:
            out.write(json.dumps(dictionary))

    @staticmethod
    def write_compiled_data_to_text_file(compiled_data, filename):
        with open(filename, "w") as out:
            for key in compiled_data:
                data = compiled_data[key]
                for val in data[:-1]:
                    out.write(str(val) +",")
                out.write(str(data[-1]) + "\n")

if __name__ == '__main__':
    predicate_dict_filename = "output/predicate_dict.json"
    data_dict_filename = "output/data.json"
    data_text_filename = "output/data.txt"


    compiled_data, predicate_id_dict = Compiler.process_data()

    if compiled_data is None:
        print("data is empty")
        
    else:
        for predicate in predicate_id_dict:
                print(predicate, ":", predicate_id_dict[predicate])

        for data in compiled_data:
            print(data, ": ", compiled_data[data])

        Compiler.write_dictionary_to_file(predicate_id_dict, predicate_dict_filename)
        Compiler.write_dictionary_to_file(compiled_data, data_dict_filename)
        Compiler.write_compiled_data_to_text_file(compiled_data, data_text_filename)


    