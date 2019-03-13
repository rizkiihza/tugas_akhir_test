
class Compiler(object):
    @staticmethod
    def compile():
        data = []
        predicates = Compiler.list_all_predicates(data)

        data = Compiler.convert_predicates_to_set(data)

        compiled_data = Compiler.get_compiled_data(data, predicates)
        return compiled_data

    @staticmethod
    def list_all_predicates(data):
        predicate_set = set()

        for key in data:
            elem = data[key]
            for predicate in elem["predicates"]:
                predicate_set.add(predicate)
        

        return list(predicate_set)


    @staticmethod
    def convert_predicates_to_set(data):
        for key in data:
            elem = data[key]
            elem["predicates"] = set(elem["predicates"])


    @staticmethod
    def get_compiled_data(data, predicates):
        predicate_id_dict = Compiler.get_predicate_id_dictionary(predicates)

        num_of_predicates = len(predicates)

        compiled_data = {}

        for key in data:
            compiled_data[key] = [0 for _ in range(num_of_predicates)]
            elem = data[key]
            for predicate in elem["predicates"]:
                predicate_id = predicate_id_dict[predicate]
                compiled_data[key][predicate_id] = 1

            compiled_data[key].append(elem["label"])

        return compiled_data

    @staticmethod
    def get_predicate_id_dictionary(predicates):
        current = 0
        predicate_id_dictionary = {}

        for predicate in predicates:
            predicate_id_dictionary[predicate] = current
            current += 1

        return predicate_id_dictionary
