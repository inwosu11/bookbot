import sys
from stats import num_of_words, character_count,character_st
def main():
	if len(sys.argv) == 2:
		book_path = sys.argv[1]
		text = get_book_text(book_path)
		numberOfWords = num_of_words(text)
		dict_char = character_count(text)
		crazy_lst = character_st(dict_char)
		print(f"Found {numberOfWords} total words")
		for item in crazy_lst:
        		# sorted_rows already filters to a–z (see stats.py below)
        		print(f"{item['char']}: {item['num']}")
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)	
def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

main()

