def num_of_words(text_From_Book):
        number = text_From_Book.split()
        return len(number)

def character_count(text_from_book):
	characters = dict()
	text = text_from_book.lower()
	for char in text:
		if char in characters:
			characters[char] = characters[char] + 1
		else:
			characters[char] = 1
	return characters

def sort_on(item):
	return item["num"]

def character_st(sorts_dict):
	dlist = []
	for key, value in sorts_dict.items():
		if key.isalpha():
			dlist.append({"char": key, "num": value})
	dlist.sort(reverse=True, key=sort_on)
	return dlist
