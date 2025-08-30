def get_num_words(contents):
    print("----------- Word Count ----------")
    words = contents.split()
    return len(words)
    
def get_num_chars(contents):
    char_count = {}
    contents = contents.lower()
    for char in contents:
        char_count[char] = char_count.get(char, 0) + 1
    for char in char_count:
        print(f"'{char}': {char_count.get(char, 0)}")

def sort_on(items):
    return items["num"]

def sorted_list(contents):
    print("--------- Character Count -------")
    char_count = {}
    contents = contents.lower()
    for char in contents:
        char_count[char] = char_count.get(char, 0) + 1
    char_list = [{"char": char, "num": num} for char, num in char_count.items()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list