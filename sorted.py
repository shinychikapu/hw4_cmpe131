def sort_dictionary(my_dict:dict):
    try:
        key_list = list(my_dict.keys())
        key_list.sort()
        new_list = [(key,my_dict[key][0]) for key in key_list]
        return new_list
    except:
        raise TypeError

print(sort_dictionary({'Dundir' : (8888888888, 24) , 'Garrik' : (6518828882, 32) , 'Vinncent' : (1231231234, 20)}))