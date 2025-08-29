def word_count(text):
    word_list = text.split()
    count = len(word_list)
    return count

def character_count(text):
    text=text.lower()
    char_count = {}
    for char in text:
        if(char not in char_count):
            char_count[char] = 1
        elif(char in char_count):
            char_count[char] += 1
    return char_count

def sort_on(items):
    return items["num"]

def report_sort(text):
    char_dict = character_count(text)
    report_list = []
    for keys in char_dict:
        if keys.isalpha():
            to_append = {"char": keys, "num": char_dict[keys]}
            report_list.append(to_append)
    report_list.sort(reverse=True, key=sort_on)
    return report_list