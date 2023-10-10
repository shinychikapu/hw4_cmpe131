def sort_dictionary(my_dict:dict):
    try:
        key_list = list(my_dict.keys())
        key_list.sort()
        new_list = [(key,my_dict[key][0]) for key in key_list]
        return new_list
    except:
        print("Please input a dictionary")

# print(sort_dictionary({'Tom' : (5464512, 24) , 'Sara' : (5446987, 32) , 'Mary' : (1557896, 20)}))