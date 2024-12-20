"""
The aim of this exercise is to print out the
JSON string with key-value pair "Me" : 800 added to it.

"""
import json


# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    # Add your code here
    salaries_obj = json.loads(salaries_json)
    salaries_obj[name] = salary
    new_sal = json.dumps(salaries_obj)
    return new_sal

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])
