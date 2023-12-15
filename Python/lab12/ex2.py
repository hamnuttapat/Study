dict = {'s5301':'Fred','s5302':'Harry','s5303':'John','s5304':'Fred','s5305':'Harry'}
def find_duplicates(data_dict):
    result = {}
    for key, value in data_dict.items():
        for sec_key, sec_value in data_dict.items():
            if key != sec_key and value == sec_value:
                result[key] = value
    print(result)
find_duplicates(dict)