def count_words(book_text):
    words = len(book_text.split())
    return words

def count_characters(book_text):
    unique_characters = {}
    lower_case_text = book_text.lower()

    for character in lower_case_text:
        if character in unique_characters:
            unique_characters[character] += 1
        else:
            unique_characters[character] = 1
        #print(character)
    return unique_characters

def sort_characters(characters_dict):
    sorted_list = []
    for entry in characters_dict:
        sorted_list.append({"character": entry, "count": characters_dict[entry]})
    sorted_list.sort(key=lambda x: x["count"], reverse=True)
    return sorted_list