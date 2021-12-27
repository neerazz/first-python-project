word_list = []


def add_word(word):
    word_list.append(word)
    print(word_list)


def add_word_at(word, idx):
    word_list.insert(idx, word)
    print(word_list)


def update_word_at(word, idx):
    word_list[idx] = word
    print(word_list)


def contains_word(word):
    return word in word_list


def remove_word_from_list(word):
    word_list.remove(word)


def remove_at_end():
    print(word_list.pop())  # By default, pop's the last item


def remove_at_index(index):
    print(word_list.pop(index))


def concatenate_to_list(new_list):
    new_list = word_list + new_list
    print(new_list)


print("Present" if contains_word("aa") else "Not Present")
add_word("aa")
add_word("abcd")
add_word_at("zzzz", 0)
update_word_at("uuuu", 0)
print("Present" if contains_word("aa") else "Not Present")
print("Present" if contains_word("abcd") else "Not Present")
remove_word_from_list("aa")
print("Present" if contains_word("aa") else "Not Present")
