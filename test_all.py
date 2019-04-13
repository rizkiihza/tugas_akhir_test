import os
import os 
import sys
import subprocess 

import pandas as pd

from collections import defaultdict
from sys import argv

if __name__ == '__main__':
    if len(argv) < 4:
        print("need 3 argument")
        sys.exit()
    program_jar = "program.jar"

    file_destination = argv[1]
    predicate_limit = argv[2]
    size_limit = argv[3]


    files =os.listdir("output/data_text")

    names = []

    for f in files:
        names.append(f.split("_")[1].split(".")[0])

    for name in names:
        print(name)


    data = defaultdict(lambda: [])

    for name in names:
        data_name = "output/data_text/data_%s.txt" % (name)
        bug_predicate_name = "output/data_predicate_bug/bug_%s.txt" % (name)

        command = "java -Xms10g -Xmx10g -jar %s -s %s %s %s %s" % (program_jar, data_name, bug_predicate_name, predicate_limit, size_limit)
        print("################################################################")
        result = subprocess.run(command.split(" "), stdout=subprocess.PIPE).stdout.decode("utf-8")

        print(result)
        try:
            result = result.split("\n")
            result = [s for s in result if len(s) > 0]

            for s in result:
                splitted_s = s.split("|")

                if s == "number of predicate is above predicateLimit":
                    break
                if len(splitted_s) == 1:
                    continue

                while splitted_s[1][0] == " ":
                    splitted_s[1] = splitted_s[1][1:]
                
                data[splitted_s[0]].append(splitted_s[1])
        except Exception as e:
            print(e)
        print("################################################################")

    for key in data:
        print(key, ":", data[key], " N: ", len(data[key]))
    df = pd.DataFrame.from_dict(data)

    df.to_csv(file_destination)