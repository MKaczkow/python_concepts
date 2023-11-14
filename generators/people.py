# Using code from
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Generators
# by Corey Schafer

import mem_profile
import random
import time


def main():
    names = ["John", "Corey", "Adam", "Steve", "Rick", "Thomas"]
    majors = ["Math", "Engineering", "CompSci", "Arts", "Business"]

    print("Memory (Before): {}Mb".format(mem_profile.memory_usage_psutil()))

    def people_list(num_people):
        result = []
        for i in xrange(num_people):
            person = {
                "id": i,
                "name": random.choice(names),
                "major": random.choice(majors),
            }
            result.append(person)
        return result

    def people_generator(num_people):
        for i in xrange(num_people):
            person = {
                "id": i,
                "name": random.choice(names),
                "major": random.choice(majors),
            }
            yield person

    # t1 = time.clock()
    # people = people_list(1000000)
    # t2 = time.clock()

    t1 = time.clock()
    people = people_generator(1000000)
    t2 = time.clock()

    print(f"Memory (After) : {mem_profile.memory_usage_psutil()}Mb")
    print(f"Took {t2-t1} Seconds")


if __name__ == "main":
    main()
