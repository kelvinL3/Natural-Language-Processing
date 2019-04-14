import re

def length_of_document(lyric_as_string):
	return len(re.findall(r"[\w']+", lyric_as_string))
	
# if __name__ == "__main__":
# 	print(length_of_document(""))