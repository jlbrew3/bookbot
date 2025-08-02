def sort_on(items):
    return items["num"]

def get_num_words(text):
    return len(text.split())

def char_dict(text):
    text = text.lower()
    dict = {}
    for char in text:
        dict[char] = dict.get(char, 0) + 1
    return dict

def sort_dict(dict_to_sort):
    sorted_list = []
    for key,value in dict_to_sort.items():
        temp_dict = dict.fromkeys(["char","num"],0)
        temp_dict["char"] = key
        temp_dict["num"] = value
        sorted_list.append(temp_dict)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list 
    #print(sorted_list)
