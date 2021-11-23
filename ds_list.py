word_list = []


def add_word(word):
    word_list.append(word)
    print(word_list)


def contains_word(word):
    return word in word_list


def remove_word_from_list(word):
    word_list.remove(word)


def remove_at_end():
    print(word_list.pop())  # By default pop's the last item


def remove_at_index(index):
    print(word_list.pop(index))


def concatenate_to_list(new_list):
    new_list = word_list + new_list
    print(new_list)


print("Present" if contains_word("aa") else "Not Present")
add_word("aa")
add_word("abcd")
print("Present" if contains_word("aa") else "Not Present")
print("Present" if contains_word("abcd") else "Not Present")
remove_word_from_list("aa")
print("Present" if contains_word("aa") else "Not Present")
