dict = {'a': '1', 'b':'2', 'c':'1', 'd':'3', 'e':'1', 'f':'2'}
def reverse (data_dict):
    result = {}
    for key, value in data_dict.items():
        if value not in result:
            result[value] = [key]
        else:
            result[value].append(key)
    print(result)

input_dict = {'a': '1', 'b':'2', 'c':'1', 'd':'3', 'e':'1', 'f':'2'}
reverse(input_dict)