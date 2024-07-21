def main() :
    path_to_file = 'books/frankenstein.txt'
    text = get_text(path_to_file)
    num_words = count_words(text)
    char_count = count_chars(text)
    char_count_list = prepare_report(char_count)
    print_report(path_to_file, num_words, char_count_list)

def count_words(text:str):
    words = text.split()
    return len(words)


def get_text(path:str):
    with open('books/frankenstein.txt') as f:
        return f.read()


def count_chars(text:str):
    text = text.lower()
    count = {}
    for char in text:
        count[char] = count.get(char, 0) + 1

    return count


def prepare_report(char_count:dict):
    char_counts_list = [{'alphabet': i , 'num' : char_count[i]} for i in char_count.keys() if i.isalpha()]
    char_counts_list.sort(reverse=True, key=sort_by_num)
    return char_counts_list


def sort_by_num(item_dict:dict):
    return item_dict['num']


def print_report(path:str, num_word:int, char_count_list:list):
    print(f'--- Begin report of {path} ---')
    print(f'{num_word} words found in the document')

    for i in char_count_list:
        print(f"The '{i['alphabet']}' character was found {i['num']} times")

main()
