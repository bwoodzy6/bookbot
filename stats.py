def get_num_words(string):
    words = string.split()
    return len(words)

def char_frequency(string):
    freq_dict = {}
    for char in string:
        char = char.lower()
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

def sort_on(items):
    return items["num"]

def sorted_dict_list(dict):
    dict_list = []
    for key in dict:
        dict_list.append({"char": key, "num": dict[key]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list